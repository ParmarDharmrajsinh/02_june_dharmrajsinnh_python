import os 
# Create a new directory
os.mkdir("newfolder")



os.chdir("folder")
os.mkdir("folder/subfolder1")


os.remove("subfolder1")


os.removedirs("newfolder")
