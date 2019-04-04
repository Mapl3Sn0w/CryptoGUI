


bs16 = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','a','b','c','d','e','f')
bs58 = ('1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
        
#Get set of 2 factors for a number; example 12 = (1,12),(2,6),(3,4),(4,3),(6,2),(12,1)
def factors(n):
    factors_list=[]
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            factors_list.append([i,n//i])
    return factors_list