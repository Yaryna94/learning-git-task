
items = [
 {'Name':'coffee', 'Quantity':'100', 'Unit':'pack', 'Unit_price':'25 PLN' },
 {'Name':'tee','Quantity':'200', 'Unit':'pack', 'Unit_price':'10 PLN'},
 {'Name':'aqwa','Quantity':'500', 'Unit':'bottle', 'Unit_price':'2.5 PLN'}, 
 ]

def get_items():
    print("Name\t\t\tQuantity\tUnit\tUnit Price (PLN)")
    print("----\t\t\t--------\t----\t-----------------")

    for item in items :
        print(item ["Name"], "\t\t\t", item ['Quantity'], "\t\t", item ['Unit'], "\t\t", item ['Unit_price'])

def add_items():
  print("Adding towarehouse...")
  



command_string = ""


while command_string != 'exit':
  
  command_string = input ("What would you like to do? : ")
 
  if command_string == 'exit':
    
    print ("Exiting... Bye!")

  if command_string == 'show':
   get_items()
   if command_string== 'add':
    add_items()

  

 

  


