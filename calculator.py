calculator = """
 _____________________
|  _________________  |
| |              0. | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|
"""
print(calculator)
def add(n1,n2):
  return n1+n2

def substract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

end=True
n1=float(input("Enter the First number: "))
while end:
  operator=input("+\n-\n*\n/\nChoose operation : ")
  n2=float(input("Enter the next number: "))
  calculator={
    '+':add(n1, n2),
    '-':substract(n1, n2),
    '*':multiply(n1, n2),
    '/':divide(n1, n2),
  }
  for operation in calculator:
    if operator==operation:
      answer=calculator[operation]
      print(f"{n1} {operator} {n2} = {calculator[operation]}")

  again=input(f"Want to continue with {answer} or exit: Type 'yes' or 'no' : ")
  if again == 'yes':
    n1=answer
  else:
    end=False
