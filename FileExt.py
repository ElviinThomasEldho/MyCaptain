import os
file_name = input("Input the Filename : ")
filename, file_extension = os.path.splitext(file_name)

print("The extension of the file is : ", end="")

if file_extension==".py":
    print("Python")
elif file_extension==".cpp":
    print("C++")
elif file_extension==".txt":
    print("Text File")
elif file_extension==".docx":
    print("Document")
elif file_extension==".ppt":
    print("Presentation")
