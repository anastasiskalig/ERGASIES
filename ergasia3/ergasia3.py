Dictionary = {}

n = int(input("subscriptions: "))

f = 0  
f = int(input("foros: ")) 

def my_function(alfa, bhssta):
    telikitimi = 0
    telikitimi2 = 0
    for i in values:
        s = int(i)
        telikitimi = telikitimi + s
        
        telikitimi2 = (telikitimi + telikitimi) * (f/100)
        return(telikitimi2)
 
for i in range(n):
    k = input("Enter key: ")
    v = input("Enter Value: ")
    Dictionary.update({k:v})
    
    print(Dictionary)
    
values = Dictionary.values()
print(values) 

my_function(values, f)