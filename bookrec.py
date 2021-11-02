import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
books = pd.read_csv('BX-Books.csv', sep=';', error_bad_lines=False, encoding="latin-1")
books.columns = ['ISBN', 'bookTitle', 'bookAuthor', 'yearOfPublication', 'publisher', 'imageUrlS', 'imageUrlM', 'imageUrlL']
users = pd.read_csv('BX-Users.csv', sep=';', error_bad_lines=False, encoding="latin-1")
users.columns = ['userID', 'Location', 'Age']
ratings = pd.read_csv('BX-Book-Ratings.csv', sep=';', error_bad_lines=False, encoding="latin-1")
ratings.columns = ['userID', 'ISBN', 'bookRating']

z=pd.DataFrame(ratings)
z=z.drop(columns=['userID'])
y=pd.merge(z, books , on='ISBN')

rating_count = pd.DataFrame(y.groupby('bookAuthor')['bookRating'].count())
r=rating_count.sort_values('bookRating', ascending=False).head()

a=r.drop(columns = ['bookRating'])
a=a.astype(object)
a.reset_index(inplace=True)

average_rating = pd.DataFrame(y.groupby('bookAuthor')['bookRating'].mean())
average_rating['ratingCount'] = pd.DataFrame(y.groupby('bookAuthor')['bookRating'].count())

most_rated_books_summary = pd.merge(a, books , on='bookAuthor')

rating_count = pd.DataFrame(y.groupby('yearOfPublication')['bookRating'].count())
r=rating_count.sort_values('bookRating', ascending=False)

a=r.drop(columns = ['bookRating'])
a=a.astype(object)
a.reset_index(inplace=True)

average_rating = pd.DataFrame(y.groupby('yearOfPublication')['bookRating'].mean())
average_rating['ratingCount'] = pd.DataFrame(y.groupby('yearOfPublication')['bookRating'].count())
average_rating.sort_values('ratingCount', ascending=False)

most_rated_books_summary = pd.merge(a, books , on='yearOfPublication')

rating_count = pd.DataFrame(ratings.groupby('ISBN')['bookRating'].count())
r=rating_count.sort_values('bookRating', ascending=False)

a=r.drop(columns = ['bookRating'])
a=a.astype(object)
a.reset_index(inplace=True)


most_rated_books_summary = pd.merge(a, books , on='ISBN')

average_rating = pd.DataFrame(ratings.groupby('ISBN')['bookRating'].mean())
average_rating['ratingCount'] = pd.DataFrame(ratings.groupby('ISBN')['bookRating'].count())
average_rating.sort_values('ratingCount', ascending=False)

with open("search.csv", 'a') as csvfile: 
    fields = ['userID','bookTitle', 'ISBN'] 
    writer = csv.DictWriter(csvfile, fieldnames = fields)
    writer.writeheader()

num=input("enter user id")
bum=input("enter book")

fum=books.drop(columns = ['bookAuthor', 'yearOfPublication', 'publisher', 'imageUrlS', 'imageUrlM', 'imageUrlL'])
fum.columns = ['ISBN', 'bookTitle']
fum.bookTitle=fum.bookTitle.astype(object)
fum.ISBN=fum.ISBN.astype(object)
fu=fum[fum.bookTitle=='Clara Callan']
fu=fu.drop(columns=['bookTitle'])
fu=fu.to_numpy()
fu=fu[0,0]

fields = ['userID','bookTitle', 'ISBN'] 
mydict = [{'userID':num,'bookTitle':bum, 'ISBN':fu}]
with open("search.csv", 'a') as csvfile: 
    writer = csv.DictWriter(csvfile, fieldnames = fields)
    #writer.writeheader() 
    writer.writerows(mydict)
cooks=pd.read_csv("search.csv",header=0)

cooks.bookTitle=cooks.bookTitle.astype(object)
cooks.ISBN=cooks.ISBN.astype(object)
cooks.userID=cooks.userID.astype(object)

cooks.columns=['userID','bookTitle','ISBN']
cu=cooks[cooks.userID==num]
cu=cu.drop(columns=['bookTitle','ISBN'])
cu=cu.to_numpy()
cu=cu[0,0]

loca=users.drop(columns = ['Age'])
loca.columns = ['userID', 'Loocation']
loca.serID=loca.userID.astype(object)
loc=loca[loca.userID==num]
loc=loc.drop(columns=['userID'])
loc=loc.to_numpy()
loc=loc[0,0]

counts1 = ratings['userID'].value_counts()
ratings = ratings[ratings['userID'].isin(counts1[counts1 >= 200].index)]
counts = ratings['bookRating'].value_counts()
ratings = ratings[ratings['bookRating'].isin(counts[counts >= 100].index)]

ratings_pivot = ratings.pivot(index='userID', columns='ISBN').bookRating
userID = ratings_pivot.index
ISBN = ratings_pivot.columns
print(ratings_pivot.shape)

bones_ratings = ratings_pivot[cu]
similar_to_bones = ratings_pivot.corrwith(bones_ratings)
corr_bones = pd.DataFrame(similar_to_bones, columns=['pearsonR'])
corr_bones.dropna(inplace=True)
corr_summary = corr_bones.join(average_rating['ratingCount'])
c=corr_summary[corr_summary['ratingCount']>=300].sort_values('pearsonR', ascending=False).head(10)

b=r.drop(columns = ['personR','ratingCount'])
b=b.astype(object)
b.reset_index(inplace=True)

corr_books = pd.merge(b, books, on='ISBN')
corr_books

combine_book_rating = pd.merge(ratings, books, on='ISBN')
columns = ['yearOfPublication', 'publisher', 'bookAuthor', 'imageUrlS', 'imageUrlM', 'imageUrlL']
combine_book_rating = combine_book_rating.drop(columns, axis=1)

combine_book_rating = combine_book_rating.dropna(axis = 0, subset = ['bookTitle'])

book_ratingCount = (combine_book_rating.
     groupby(by = ['bookTitle'])['bookRating'].
     count().
     reset_index().
     rename(columns = {'bookRating': 'totalRatingCount'})
     [['bookTitle', 'totalRatingCount']]
    )

rating_with_totalRatingCount = combine_book_rating.merge(book_ratingCount, left_on = 'bookTitle', right_on = 'bookTitle', how = 'left')
rating_with_totalRatingCount.head()

pd.set_option('display.float_format', lambda x: '%.3f' % x)

popularity_threshold = 50
rating_popular_book = rating_with_totalRatingCount.query('totalRatingCount >= @popularity_threshold')

combined = rating_popular_book.merge(users, left_on = 'userID', right_on = 'userID', how = 'left')

us_canada_user_rating = combined[combined['Location'].str.contains(loc)]
us_canada_user_rating=us_canada_user_rating.drop('Age', axis=1)


from scipy.sparse import csr_matrix
us_canada_user_rating = us_canada_user_rating.drop_duplicates(['userID', 'bookTitle'])
us_canada_user_rating_pivot = us_canada_user_rating.pivot(index = 'bookTitle', columns = 'userID', values = 'bookRating').fillna(0)
us_canada_user_rating_matrix = csr_matrix(us_canada_user_rating_pivot.values)

from sklearn.neighbors import NearestNeighbors

model_knn = NearestNeighbors(metric = 'cosine', algorithm = 'brute')

query_index = np.random.choice(us_canada_user_rating_pivot.shape[0])
distances, indices = model_knn.kneighbors(us_canada_user_rating_pivot.iloc[query_index, :].values.reshape(1, -1), n_neighbors = 6)

query_index = np.random.choice(us_canada_user_rating_pivot.shape[0])
distances, indices = model_knn.kneighbors(us_canada_user_rating_pivot.iloc[query_index, :].values.reshape(1, -1), n_neighbors = 6)

for i in range(0, len(distances.flatten())):
    if i == 0:
        print('Recommendations for {0}:\n'.format(us_canada_user_rating_pivot.index[query_index]))
    else:
        print('{0}: {1}, with distance of {2}:'.format(i, us_canada_user_rating_pivot.index[indices.flatten()[i]], distances.flatten()[i]))

print ("recommendation  using matrix fact.")
X = us_canada_user_rating_pivot2.values.T
import sklearn
from sklearn.decomposition import TruncatedSVD

SVD = TruncatedSVD(n_components=12, random_state=17)
matrix = SVD.fit_transform(X)

import warnings
warnings.filterwarnings("ignore",category =RuntimeWarning)
corr = np.corrcoef(matrix)

us_canada_book_title = us_canada_user_rating_pivot2.columns
us_canada_book_list = list(us_canada_book_title)
coffey_hands = us_canada_book_list.index("Winter Solstice")

corr_coffey_hands  = corr[coffey_hands]
list(us_canada_book_title[(corr_coffey_hands>0.85)])
