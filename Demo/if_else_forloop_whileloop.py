# if,else,elif,forLoop,whileLoop


# If,Elif,Else
if 5 > 3:
    print("5 is greater than 3!")

num = 1
if num > 0:
    print("This is a Positive number")
elif num == 0:
    print("Num is zero")
else:
    Print("This is Negative number")


# For Loop

num = [1,2,3,4,5]
sum =0
for val in num:
    sum=sum+1
    print("Total is", sum)


fruits = ["Apple","Orange","grapes"]
for val in fruits:
    print(val)
else:
    print("No fruits left")


num = 10
sum = 0
i = 1
while i<num:
    sum=sum+1
    i=i+1
    print("Total is:", sum)