import os


"""
Give a path and find subtitle files in it and save subtitle path in a text file

Args:
    url (path): path of the desired folder
"""

with open("sub_path.txt", "w") as file:
    for path, subdirs, files in os.walk(rf"URL"):
        for filename in files:
            f = os.path.join(path, filename)
            if str(f)[-3:] == "srt":
                file.write(str(f) + "\n")
