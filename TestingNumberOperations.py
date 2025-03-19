import NumberOperations
num=int(input("Enter value for n"))
secondnum=int(input("Enter value for r"))
#answer=NumberOperations.Factorial(num)/secondnum
nf=(NumberOperations.Factorial(num))
rf=(NumberOperations.Factorial(secondnum))
nrf=(NumberOperations.Factorial(num-secondnum))
print(nf/(rf*(nrf)))

result=NumberOperations.createBooks()
print(result)
