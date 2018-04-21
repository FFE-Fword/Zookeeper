#Version 0.9

import pandas as pd
import numpy as np

#Reads csv data file

df = pd.read_csv("TheZoo.csv", sep = ",")

#Define AND search func

def AND_search(df):
    df = df[ (df[input("Enter 1st Category: ")] == str(input("Enter 1st Value: ")
        )) & (df[input("Enter 2nd Category: ")] == str(input("Enter 2nd Value: ")))]
    print(df)
    
#Define OR search func

def OR_search(df):
     df = df[ (df[input("Enter 1st Category: ")] == str(input("Enter 1st Value: ")
        )) | (df[input("Enter 2nd Category: ")] == str(input("Enter 2nd Value: ")))]
     print(df)
    

#Start Program
while True:
    start = input("Do you want to look in the Zoo? (Enter 'yes' or 'no'.) :")
    if start == "yes":
        
#Type of search
        
        filt = input("Quick Search , AND Search , OR Search: ")

#User enters a column and value to search for. Basic error handling.    
        
        if filt.lower() == "quick search":
            while True:
                try:
                    a = df[str(input("Enter A Category: "))] == str(input("Enter A Value: "))
                    break
                except:
                    print("Enter a pre-stored Category or Value ONLY!")       
            print(df[a])

#AND_search code. Prints according to current vers notes

        elif filt.lower() == "and search":
                AND_search(df)
                
#OR_search code. Prints according to vers notes.
                
        elif filt.lower() == "or search":
                OR_search(df)
                
#Closes Program if user entered no at start
                
    else:
         if start == "no":
            print("Closing the Gate!")
            break
            

