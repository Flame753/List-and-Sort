
f = open(fileName, "a")
f.write("Now the file has something. ")
f.close()

f = open("demofile.txt", "r")
print(f.read())