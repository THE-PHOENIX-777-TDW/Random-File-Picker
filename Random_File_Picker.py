import os, random, shutil

#Prompting user to enter number of files to select randomly along with directory
source=input("Enter the Source Directory : ")
dest=input("Enter the Destination Directory : ")
no_of_files=int(input("How many files do you wish to Select : "))

print("%"*30+"{ Details Of Transfer }"+"%"*30)
print("\n\nList of Files Moved to %s :-"%(dest))

#Using for loop to randomly choose multiple files
for i in range(no_of_files):
    #Variable random_file stores the name of the random file chosen
    random_file=random.choice(os.listdir(source))
    print("%d} %s"%(i+1,random_file))
    source_file="%s\%s"%(source,random_file)
    dest_file=dest
    #"shutil.move" function moves file from one directory to another
    shutil.move(source_file,dest_file)

print("\n\n"+"$"*27+"[ Files Moved Successfully ]"+"$"*28)
