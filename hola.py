def add(x,y):
    return x+y
print(add (2, 3))

def add(x,y):
    return x+y
print(add ("Dolmio", "Day"))

def num(x):
    if x > 10:
        return "BIIIIIIIIIG"
    else:
        return "small"
print(num(11))

def are_same(x,y):
    return x == y
print(are_same(5,4))

def size(x,y):
    if x > y:
        return "Bigger"
    if x < y:
        return "smaller"
    else:
        return "Samez"
print (size(9,9))

x=0
total=0
while x<=10:
    x = x+1
    total=total+x
print(total)

def contains(x, y, n):
    while x<=y:
        if x==n:
            return True
        x=x+1
    return False
print (contains(1,10,7))