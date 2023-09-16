# with open("file.txt", "w") as file:
#     file.write("Hello world!")
# with open("file.txt", "a") as file:
#     file.write(" Hello user!")
# with open("file.txt", "r") as file:
#     print(file.read())

import os


def file_collector(path):
    path = os.path.normpath(path)
    result = {"dirs": [], "files": []}
    for path, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            result["dirs"].append(dir)
        for file in filenames:
            result["files"].append(file)
    with open("skiper.txt", "w") as file:
        file.write("\n{:-<50}\n".format("Directories"))
        for dir in result["dirs"]:
            file.write(f"\t{dir}\n")
            file.write("\n{:-<50}".format("Files"))
        for files in result["files"]:
            file.write(f"\t{files}\n")


path = "C:\\Windows\\Web"
file_collector(path)
