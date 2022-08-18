myExt={"py": "Python",
    "java": "Java",
    "c": "C",
    "cc": "C++",
    "db": "Database File",
    "js": "JavaScript"}

fname=input("Enter your filename: ")
ext=fname.split(".")
for i in myExt:
    if(ext[1] == i):
        print(myExt[i])
