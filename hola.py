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



s = "ABCDEFGHIJKLM"

result = s[0:4]

print (result)


person = {
    "name":"Richard",
    "age":"43",
    "favourite colour":"Yellow"
}
print(person["favourite colour"])


def count_upper_case(message):
    return (sum([2 for c in message if c.isupper()]) + sum([1 for c in message if c.islower()]))
    
print(count_upper_case("Hello World How Are You!?"))



message = "HelloWorld"

scores = [1, 2]

as_TF = [c.isupper() for c in message]
as_10 = [int(c) for c in as_TF]
as_scores = [scores[c] for c in as_10]
print(sum(as_scores))

--------------------------------------

def sumlist(l):
    if l = []:
        return 0
    retrun l[0] + sumlist(l[1:])
    
print(sumlist([1, 2, 5, 9, 13]))

def sumloop(l):
    total = 0
    for n in l:
        total +=n
    return total

---------------------------------------



[1, 2, 3]       same as     [i for i in range (4)]