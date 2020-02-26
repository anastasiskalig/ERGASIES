number = int(input("Give a number:")) 
number = number * 3
number = number + 1
def athroisma(y):
    a = 0
    while y:
        a += y % 10
        y //= 10
    return a
while athroisma(number) >= 10:
  number = (athroisma(number)) * 3
  number = (athroisma(number)) + 1
  def athroisma(y):
    a = 0
    while y:
        a += y % 10
        y //= 10
    return a
else:
  print (athroisma(number))