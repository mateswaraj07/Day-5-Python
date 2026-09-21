#count number of digits
#eg input: 1,2,3,4 o/p: 4

n = int(input("Enter a Positive Integer: "))
count = 0
if n==0:
    count=1
else:
    while n > 0:
        n = n // 10
        count = count + 1
print("Number of digits:", count)

#Every time we divide the number by 10, one digit is removed, and we increase count by 1.