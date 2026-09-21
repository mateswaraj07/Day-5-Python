# program to reverse a number
n = int(input("Enter a Positive Integer: "))
reverse = 0
while n !=0:
    digit = n % 10
    reverse = reverse*10+digit
    n = n//10
print("Reverse:", reverse," ")

#Take the last digit, add it to the reverse number, 
#remove the last digit from the original number, and repeat until the number becomes 0.