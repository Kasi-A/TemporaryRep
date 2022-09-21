import sys
#2. Користувач задає розміри прямокутного паралелепіпеда. Програма повинна обчислити об´єм і площу поверхні прямокутного паралелепіпеда. 
def paral(a,b,c):
    print ("S = ", 2 *(a*b + b*c + a*c))
    print ("V = ", a*b*c)


a = int(sys.argv[1]) 
b = int(sys.argv[2]) 
c = int(sys.argv[3]) 

paral(a,b,c)






