from pathlib import Path 
 #Importing Path .What is importing ?Using a collection of useful code that some one has already written
 #Path represents a location on your omputer /file system
 # But Instead of treating these as ordinary strings(meaning the path), Python lets us work with them as Path objects.A Path object has many helpful functions built in.

current_dir=Path.cwd()
#Finding the current folder where the script is running from.cwd() stands for current working directory
#Suppise your script is inside Documents under Pyton folder, then cwd() will return the path to that folder. it returns Documents/Python
#now current_dir  stores that location of Documents/Python folder as a Path object. We can use this object to do many things like listing the files in that folder, checking if a file exists, creating new folders, and so on.
current_file=Path('_Files_').name
#skip = Path("Files").name .Let's go slowly.,Path("Files")creates a Path object.A Path object has many helpful functions built in.
#Think of it like making a label that points toFiles
# Then .name aks "What is the last part of this path"? example "Path("Documents/Assignments/Homework.pdf")"  the name is Hoemowork.pdf
print (f"Files in {current_dir}:")
for filepath in current_dir.iterdir():#iterdir()This means "Give me everything inside this folder."
    if filepath.name == current_file:
        continue
    print(f" - {filepath.name}")

    if filepath.is_file():# is_file()This means "Is this a file?"
       content=filepath.read_text(encoding='utf-8')# read_text()This means "Read the text content of this file." UTF-8 is a common way to encode text files. It can handle many different characters from different languages.
       print (f"  Content of {filepath.name}:")