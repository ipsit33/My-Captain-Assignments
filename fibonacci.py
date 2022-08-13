num = [0,1]
n=int(input("Enter a number till which u want to get Fibonacci series: "))
i=2
while i<n:
    x=num[i-1] + num[i-2]
    num.append(x)
    i+=1

print(num)