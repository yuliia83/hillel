x = int(input("Enter five numbers:"))
y = x//1%10
c = x//10%10
b = x//100%10
v = x//1000%10
t = x//10000
w = t*1 + v*10 + b*100 + c*1000 + y*10000
print(w)

