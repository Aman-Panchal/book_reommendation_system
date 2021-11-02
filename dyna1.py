import os
import requests
import pandas as pd
import csv

class gbooks():
    googleapikey="AIzaSyC2Ol0vngXZ3kxFO2ygSOethWGLjOiN4k0"
    def per(self,value):
        googleapikey="AIzaSyC2Ol0vngXZ3kxFO2ygSOethWGLjOiN4k0"
        global parms,r,rj
        parms = {"q":value, 'key':self.googleapikey}
        r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
        global l
        l=0
        rj = r.json()
        for i in (rj["items"]):
            try:
                k=repr(i["volumeInfo"]["title"])
                print("{} {}".format(l,k))
                l+=1
            except:
                pass

    def der(self,value):
        googleapikey="AIzaSyC2Ol0vngXZ3kxFO2ygSOethWGLjOiN4k0"
        global parms,r,rj
        parms = {"q":value, 'key':self.googleapikey}
        r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
        global l
        l=0
        rj = r.json()
        for i in (rj["items"]):
            try:
                k=repr(i["volumeInfo"]["title"])
                print("{} {}".format(l,k))
                l+=1
            except:
                pass

    def mer(self,value):
        googleapikey="AIzaSyC2Ol0vngXZ3kxFO2ygSOethWGLjOiN4k0"
        global parms,r,rj
        parms = {"q":value, 'key':self.googleapikey}
        r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
        global l
        l=0
        rj = r.json()
        for i in (rj["items"]):
            try:
                k=repr(i["volumeInfo"]["title"])
                print("{} {}".format(l,k))
                l+=1
            except:
                pass

    
    def search(self, value):
        parms = {"q":value, 'key':self.googleapikey}
        r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
        print (r.url)
        rj = r.json()
        print (rj["totalItems"])
        b=[]
        j=0
        for i in rj["items"]:
            try:
                a=[repr(i["volumeInfo"]["title"])]
                print("{} {}".format(j,a))
                j+=1
                b.append(a)
            except:
                pass
        
        
        x=int(input(" enter choice "))
        def week(x):
            
            if(x==0):
                bk.sear(b[0])
            if(x==1):          
                bk.sear(b[1])
            if(x==2):
                bk.sear(b[2])
            if(x==3):               
                bk.sear(b[3])
            if(x==4):
                bk.sear(b[4])
            if(x==5):
                bk.sear(b[5])
            if(x==6):
                bk.sear(b[6])
            if(x==7):
                bk.sear(b[7])
            if(x==8):
                bk.sear(b[8])
            if(x==9):
                bk.sear(b[9])

        week(x)
       # print(b)
    def sear(self,value):
        googleapikey="AIzaSyC2Ol0vngXZ3kxFO2ygSOethWGLjOiN4k0"
        global parms,r,rj
        parms = {"q":value, 'key':self.googleapikey}
        r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
        print (r.url)
        rj = r.json()
        
        for i in (rj["items"]):
            try:
                print("TITLE:")
                print(repr(i["volumeInfo"]["title"]))
                print("AUTHOR:")
                print(repr(i["volumeInfo"]["authors"]))
                print("PUBLISH DATE")
                print(repr(i["volumeInfo"]["publishedDate"]))               
                print("AVERAGE RATING")
                print(repr(i["volumeInfo"]["averageRating"]))
                print("DESCRIPTION")
                print(repr(i["volumeInfo"]["description"]))
                print("PAGECOUNT")
                print(repr(i["volumeInfo"]["pageCount"]))
                print("LANGUAGE")
                print(repr(i["volumeInfo"]["language"]))
                print("IMAGE LINKS")
                print(repr(i["volumeInfo"]["imageLinks"]))
                global ab,bc,cd
                ab=[repr(i["volumeInfo"]["categories"])]
                bc=[repr(i["volumeInfo"]["authors"])]
                cd=[repr(i["volumeInfo"]["language"])]
                break
                
            except:
                pass
        
        
    
        
        
                
    
    
if __name__ == "__main__":
    bk = gbooks()
    
    global bum,num
    num=int(input("enter user id"))
    bum=input("enetr book")
    cooks=pd.read_csv("search.csv",header=0)
    cooks.columns=['userID','bookTitle','categories','authors','language']
    global cu
    print("1")
    if(any(cooks.userID==num)):
        print("2")

        cu=cooks[cooks.userID==num]
        cu=cu.drop(columns=['userID','bookTitle','authors','language'])
        cu=cu.to_numpy()
        cu=cu[0,0]
        print("ACCORDING TO HISTORY")
        print('CATEGORIES')
        bk.per(cu)
        print("3")
        cu=cooks[cooks.userID==num]
        cu=cu.drop(columns=['userID','bookTitle','categories','language'])
        cu=cu.to_numpy()
        cu=cu[0,0]
        print("4")
        print('AUTHORS')
        bk.der(cu)

        cu=cooks[cooks.userID==num]
        cu=cu.drop(columns=['userID','bookTitle','categories','authors'])
        cu=cu.to_numpy()
        cu=cu[0,0]
        
        print('LANGUAGE')
        bk.mer(cu)
        fields = ['userID','bookTitle','categories','authors','language']
        print("5")
        with open("search.csv", 'a') as csvfile:
            print("6")
            file_is_empty = os.stat('search.csv').st_size == 0
            writer = csv.DictWriter(csvfile, fieldnames = fields)
            bookTitle=bookTitle+bum
            categories=categories+ab
            authors=authors+bc
            language=language+cd
            
            
        

    else:
        def csv(z,c,d):
            print("7")
            fields = ['userID','bookTitle','categories','authors','language']
            file_exists = os.path.isfile("search.csv")
            mydict = [{'userID':num,'bookTitle':bum,'categories':ab,'authors':bc,'language':cd}]
            with open("search.csv", 'a') as csvfile: 
                file_is_empty = os.stat('search.csv').st_size == 0
                writer = csv.DictWriter(csvfile, fieldnames = fields)
                if file_is_empty:
                    writer.writeheader()
                writer.writerows(mydict)
        
    
    bk.search(bum)
  
    
         
