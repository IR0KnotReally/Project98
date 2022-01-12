def swapFileData():
    with open("sample1.txt","r") as a:
        data_a=a.read()
    with open("sample2.txt","r") as b:
        data_b=b.read()
    with open("sample1.txt","w") as a:
        a.write(data_b)
    with open("sample2.txt","w") as b:
        b.write(data_a)           
    #filedata1=open("sample1.txt")
    #filedata2=open("sample2.txt")
    #print(filedata.read())
    #lines=filedata1.readlines()
    
    #for i in lines:
        #print(i)
   # name="this is code.py"
    #print(name.split())    

swapFileData()

def countwords():
    file=open("sample1.txt")
    numberofwords=0
    lines=file.readlines()
    for i in lines:
        word=i.split()
        numberofwords=numberofwords+len(word)
    print(numberofwords)

countwords()