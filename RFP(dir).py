import os, random, shutil, sys

#Prompting user to enter number of files to select randomly along with directory
source=input("Enter the Source Directory:")
dest=input("Enter the Source Directory:")
no_of_files=int(input("Enter The Number of Files To Select : "))


print("\n^^^^^^^^^^^Details Of Transfer^^^^^^^^^^^")
print("\nList of Files Moved to %s :-"%(dest))


#Using for loop to randomly choose multiple files
for i in range(no_of_files):
    #variable random_file stores the name of the random file chosen
    random_file=random.choice(os.listdir(source))
    print("%d} %s"%(i+1,random_file))
    source_file="%s\%s"%(source,random_file)
    dest_file=dest
    #"shutil.move" function moves file from one directory to another
    shutil.move(source_file,dest_file)


print("\n---------Files Moved Successfully---------")

