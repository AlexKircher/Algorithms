import math

def search_divisors(n):
    
    divs = [1,n]
    
    if math.sqrt(n).is_integer():
        
        divs.append(int(math.sqrt(n)))

        for i in range(2,int(math.sqrt(n))):

                if n%i==0:
                    
                    divs.append(i)
                    divs.append(n//i)
    else:
        
        for i in range(2,int(math.sqrt(n))+1):
            
                if n%i==0:
                    
                    divs.append(i)
                    divs.append(n//i)
                
    divs.sort()
    return divs

k = int(input())
print(search_divisors(k))
