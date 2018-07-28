textfile1=raw_input("file1 name:")
text1=open(textfile1,'r')
textfile2=raw_input("file2 name:")
text2=open(textfile2,'a+')
s1=text1.read()
text2.write(s1)
text2.seek(0,0)
s2=text2.read()
print s2
