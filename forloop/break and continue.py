for i in range(10):
    if i%2==0:
        continue
    print(i)

for i in range(20):
    while i%2==0:
        print(i)
        i=i+1
        break