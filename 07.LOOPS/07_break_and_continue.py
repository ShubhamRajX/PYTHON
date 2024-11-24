for i in range(100):
    print(i)
    if(i == 3):
        break       # this will print 0, 1, 2, and 3
    
    
for i in range(0, 100):
    if(i == 34):
        break       # Exit the loop right now
    print(i)


for i in range(100):
    if(i == 34):
        continue        # Skip this iteration
    print(i)    

for i in range(4):
    print("Shubham")
    if(i==2):           # if i is 2, the iteration is skipped
        continue
    print(i)