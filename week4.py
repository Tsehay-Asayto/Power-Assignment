try:
    file=open("input.txt","a") 
    append=file.write("File handling in python")
    print("append is successes fully done")
    
    modify=open("output.txt","w")
    file=open("input.txt","r")
    power=file.read()
    modify.write(power)
    print("successes fully modify")
except FileNotFoundError:
    print("FileNotFoundError")
