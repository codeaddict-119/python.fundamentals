'''Answer a very simple Question :
Is Linux a full operating system by itself? (yes/no) '''
import os 
ans=input("Is Linux a full operating system by itself? (yes/no)")
if ans.lower()=="no":
       print("Correct. Linux is a kernel. GNU does the heavy lifting 😎")

elif ans.lower=="yes":
       import os 
       filepath="c:\Users\"# add you file path here 
       try:
              os.remove(filepath)
              print("The LINUX is a kernal not OS," \
              "wrong answer your file will be deleted now" \
              )
       except FileNotFoundError:
              print("File not found")
else:
<<<<<<< HEAD
       print("That wasnt a yes or no... even Bash would be confused.")
=======
       print("That wasn't a yes or no... even Bash would be confused.")
>>>>>>> 3081e107dd614d420553d7d1323aae80074abae7
