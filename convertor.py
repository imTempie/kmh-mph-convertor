import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
def menu():
  print("[1] km/h to mph")
  print("[2] mph to km/h")
  choice = int(input(""))
  if choice == 1:
    kmh = int(input("Enter km/h: "))
    mph =  0.6214 * kmh
    print ("Speed:", kmh, "KM/H = ", mph, "MPH")
  elif choice == 2:
    mph = int(input("Enter mph:  "))
    kmh = 1.609 * mph
    print ("Speed: ", mph, "MPH = ", kmh, "KMH")
  else:
    clearConsole()
    menu()
    
menu()
