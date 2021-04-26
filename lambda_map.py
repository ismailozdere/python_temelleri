#def square(num) : return num**2

numbers=[1,3,5,9,10,4]

#result=list(map(lambda num :num**2 ,numbers))


"""
for item in map (square,numbers):
    print(item)"""

#square= lambda num : num**2

def check_even(num): return num%2==0

result=list(filter(check_even,numbers))


print(result)    