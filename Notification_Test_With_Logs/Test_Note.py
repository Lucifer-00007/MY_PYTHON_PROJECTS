from time import time 

watersecs=1*10
Coldrinksecs=1*10 +3
Coffeesecs=1*10 +7


init_water=time()
init_cd=time()
init_cf=time()

def log_Check(item, item_time):
  if item=="Water":
    with open("My_water_Log.txt","a") as f:
      f.write(f"\n[{item_time}], {item}")
  
  elif item=="Coldrink":
    with open("My_colddrink_Log.txt","a") as f:
      f.write(f"\n[{item_time}], {item}")
  
  else:     
    with open("My_coffee_Log.txt","a") as f:
      f.write(f"\n[{item_time}], {item}")



while True:
  if time() - init_water > watersecs:
      print("\nWater Drinking time. Enter 'drank' to rest the alarm.","time:",time())      
      init_water = time()
      log_Check("Water", init_water)
  
  if time() - init_cd > Coldrinksecs:
      print("\n\ncoldrink Drinking time. Enter 'drank' to rest the alarm.","time:",time())
      init_cd = time()
      log_Check("Coldrink", init_cd)
  
  if time() - init_cf > Coffeesecs:
      print("\n\n\nCoffee Drinking time. Enter 'drank' to rest the alarm.","time:",time())
      init_cf = time()
      log_Check("Coffee", init_cf)









