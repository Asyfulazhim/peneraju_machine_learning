# Problem 8 Number to Words:

n = int(input("Enter Number: "))

one = ['zero','one','two','three','four','five','six','seven','eight','nine']
two = ['ten', 'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen', 'nineteen']
ten = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
hundreds = ['hundred','thousand','million', 'billion']

while (n != 0):
  if(n // 10**6 != 0): # million
    print(one[n // 10**6], hundreds[2],end = " ")
    n %= 10**6
  if(n // 10**5 != 0): # hundredth thousand
    if((n % 10**5)//10**4 == 0 and (n % 10**4)//10**3 == 0):
      print(one[n // 10**5], hundreds[0], hundreds[1],end = " ")
    else:
      print(one[n // 10**5], hundreds[0],end = " ")
    n %= 10**5
  elif(n // 10**4 != 0): #tenth thousand
    if((n % 10**4)//10**3 == 0):
      print(ten[n // 10**4], hundreds[1],end = " ")
    else:
      print(ten[n // 10**4], end = " ")
    n %= 10**4
  elif (n // 10**3 != 0): #thousand
    print(one[n // 10**3], hundreds[1],end = " ")
    n %= 10**3
  elif(n // 100 != 0):
    print(one[n // 100], hundreds[0],end = " ")
    n %= 100
  elif(n // 10 != 0):
    if n < 20:
      print(two[n % 10])
      break
    else:
      print(ten[n // 10], end = " ")
      n %= 10
  else:
    print(one[n])
    n = 0