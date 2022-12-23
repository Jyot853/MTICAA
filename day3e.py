import math
n=input()
total=0
for i in n:
    total += math.pow(int(i),len(n))
if int(n)==total:
    print(n,"is amastrong number")
else:
    print(n,"is not amastrong number")
        

output:

11 is not amastrong number
153 is amastrong number
