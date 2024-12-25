def fibo(n):
     for i in range(n) :
         if i ==0:
             l.append(1) 
             
         elif i==1:
             l.append(1) 
             
         else:
             l.append(l[-1]+l[-2])
     return(l)      
l=[]
x=int(input()) 
print(fibo(x))