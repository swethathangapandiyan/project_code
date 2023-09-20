a=("apple",3,"banana","cherry","berry")
print(a)
a1=tuple("swetha")
print(a1)
print(a[::-1])
print(a[1:5:2])
print(a[-1:-4:-1])
print(a[-5:-1])
print(a[-3:-2])
print(a[2::])
i=0
b=len(a)
while b>i:
    print(a[i])
    i=i+1

for x in a:
    print(x)

i="7"+"7"
print(i)
name="swetha"
print(name)
a1=name.replace('t','d')
print(a1)
b=("jack",)
a+=b
print(a)
tuple=("swetha",2,4,5*3-2)*3
print(tuple)
fruits = ("apple", "banana", "cherry")

(green, *yellow, red) = a

print(green)
print(yellow)
print(red)
b=list(a)
b.append("swetha")
print(b)
b=a.index("banana")
print(b)

