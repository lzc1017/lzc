from sys import argv
script,textfile=argv
text=open(textfile,'w')
line1="Hello!\n"
line2="I am Xiaoming."
line3="I am 5 years old.\n"
text.write(line1)
text.write(line2)
text.write('\n')
text.write(line3)
text.close()
