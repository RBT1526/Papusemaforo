import threading as th  
## Defining a method  
def sctn():  
   print("SECTION FOR LIFE \n")  
S = th.Timer(5.0, sctn)  
S.start()  
print("Exit Program\n")