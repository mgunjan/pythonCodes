

def prime_factor(n):
    factors=[]
    d=2

    if n < 0 or not(isinstance(n,int)):
        return None
    elif n == 0 or n== 1 or n==2 or n == 3:
        factors.append(n)
        return factors
    else:
        while(d*d<n):
            while(n>1):            
                while n%d==0:
                    factors.append(d)
                    n=n/d
                d+=1
            return factors

   
