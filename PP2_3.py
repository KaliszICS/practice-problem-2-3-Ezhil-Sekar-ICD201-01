

def q1(): 
  #Write Assignment code here
 word = input("In: ")
 if word[-3:] == "ife":
    print("-ives")
 elif word[-2:] == "ey":
  print("-eys")
 elif word[-1:] == "y":
  print("-ies")
 else:
  print("-s")

def q2(): 
  #Write Assignment code here
  num = int(input("In: "))
  if num%2 == 0:
    print(f'{num} is positve')
  elif num%2 != 0:
    print(f'{num} is negative')


#Do not alter the following code
#Comment out the following code when running your tests

q1()
q2()
