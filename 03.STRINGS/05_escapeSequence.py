a = "Escape Sequence characters \n comprise of more than one character"

b = "Escape Sequence characters \t comprise of more than one character"

c = "Escape Sequence 'characters' comprise of more than one character" 

# c = "Escape Sequence "characters" comprise of more than one character"    #Error

d = 'Escape Sequence "characters" comprise of more than one character'

# d = 'Escape Sequence 'characters' comprise of more than one character'    #Error

e = "Escape Sequence \characters\ comprise of more than one character"

f = "Escape Sequence /characters/ comprise of more than one character" 

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)