def swapFileData():
    with open("sample1.txt","r") as a:
        data_a=a.read()
    with open("sample2.txt","r") as b:
        data_b=b.read()
    with open("sample1.txt","w") as a:
        a.write(data_b)
    with open("sample2.txt","w") as b:
        b.write(data_a)         

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
