#Version 0.5

import pandas as pd
import numpy as np

#Reads csv data file

df = pd.read_csv("TheZoo.csv", sep = ",")

#Define AND search func

def AND_search(df,list_of_keywords):
    index_arr = np.array([]) 
    for keyword in list_of_keywords:
        index = df[df==keyword].dropna(how='all').index.values
        index_arr = index if index_arr.size == 0 else np.intersect1d(index_arr,index)
    print(df.loc[index_arr.astype(int)])

#Define OR search func

def OR_search(df,list_of_keywords):
    index_arr = np.array([]) 
    for keyword in list_of_keywords:
        index = df[df==keyword].dropna(how='all').index.values
        index_arr = np.unique(np.concatenate((index_arr,index),0))
    print(df.loc[indyeex_arr.astype(int)])

#Use or Close the program
    
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
                keylist = []
                i = 0
                while 1:
                    i +=1
                    key = input("Enter value or enter s to start search %d: "%i)
                    if key == "s":
                        break
                    keylist.append(key)
                AND_search(df,keylist)
                
#OR_search code. Prints according to vers notes.
                
        elif filt.lower() == "or search":
                keylist = []
                i = 0
                while i < 2:
                    i += 1
                    key = input("Enter value %d: "%i)
                    keylist.append(key)
                OR_search(df,keylist)
                
#Closes Program if user entered no at start
                
    else:
         if start == "no":
            print("Closing the Gate!")
            break
            
                                 
                

