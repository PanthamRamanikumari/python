#1.concatenation
a="Hello"
b="World"
print(a+" "+b)

#2.repetation
s="Hi!"
print(s*3)

#3.indexing&sliding
s="Python"
print(s[0])  #first character
print(s[-1])  #last character
print(s[0:4])  #from index 0to3

#4.membership
s="Python programing"
print("Python" in s)
print("Java" not in s)grj

#5.string lenght
s="Python"
print(len(s))

#6.case conversion
s="PyThoN"
print(s.lower())
print(s.upper())
print(s.title())

#7.strip (remove spaces)
s=" Hello "
print(s.strip())

#8.replace
s="I Love You"
print(s.replace("You","myself"))

#9.split and join
s="a.b.c"
print(s.split(","))
words=['a','b','c']
print("-".join(words))

#10.find and count
s="banana"
print(s.find("na"))
print(s.count("a"))
