def swap():
    data1= open("C:/Users/sanja/OneDrive/Desktop/Python/text1.txt","r").read()
    data2= open("C:/Users/sanja/OneDrive/Desktop/Python/text2.txt","r").read()
    open("C:/Users/sanja/OneDrive/Desktop/Python/text1.txt","w").write(data2)
    open("C:/Users/sanja/OneDrive/Desktop/Python/text2.txt","w").write(data1)
swap()
