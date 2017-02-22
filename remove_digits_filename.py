import os

def renamer():
    files = os.listdir("/home/argon/Desktop/prank/")
    starter_dir = os.getcwd()
    os.chdir("/home/argon/Desktop/prank/")

    for file in files:
        os.rename(file, (file.translate(None, "0123456789")))

    os.chdir(starter_dir) 
renamer()
