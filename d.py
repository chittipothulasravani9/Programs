n=int(input("enter the number"))
for i in range(n):
    spaces=" "*(n-i)
    stars="* "*i
    print(spaces+stars)
    
for i in range(n):
    spaces=" "*i
    stars="* "*(n-i)
    print(spaces+stars)
