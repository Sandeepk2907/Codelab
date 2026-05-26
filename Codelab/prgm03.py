import os 
path=input("Enter File Path:")
count=0
for file in os.listdir(path):
    if file.endswith(".txt"):
        count+=1
print(".txt File Found",count)