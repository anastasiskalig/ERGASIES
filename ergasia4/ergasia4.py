message = input("Enter message to encode: ")

print ("Decoded string (in ASCII):")
def conv_asc(x):
  return [ ord(x) for x in message ]
  
  

print (conv_asc(message))


def primenum(message):
  num = ''.join(str(ord(c)) for c in message)
  int_num = int(num)
  if  int_num > 1: 

   for i in range(2, int_num//2): 
           
       if (int_num % i) == 0: 
           return int_num, "is not a prime number" 
           break
   else: 
       return int_num, "is a prime number" 
  
  else: 
   return int_num, "is not a prime number"
   

print (primenum(message))