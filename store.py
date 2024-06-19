'''
File: store.py
Description: This module contains the Store class which utilises information from all other classes for the ordering process.
Author: Ayesha Pathak
ID: 1104095812
Username: patay096
This is my own work as defined by the University's Academic Misconduct Policy.
'''


from bubble_tea import BubbleTea
from milk_tea import MilkTea 
from fruit_tea import FruitTea
from hot_tea import HotTea 
from sparkling_tea import SparklingTea
from frozen_tea import FrozenTea


class Store(MilkTea, FruitTea, SparklingTea, HotTea, FrozenTea, BubbleTea):
  def __inti__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price):
    BubbleTea.__init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
    MilkTea.__init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
    FruitTea.__init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
    SparklingTea.__init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
    HotTea.__init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
    FrozenTea.__init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)

  def milk_order(self, drink_name, size, ice_level, sugar_level, tea_type):
      topping_action = input("Would you like to add or remove any toppings from your drink selection? [Add/Remove]")
      if topping_action == "Add":
        bubble_tea = MilkTea("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
        bubble_tea.add_topping("Cookie Crumb", "Classic Milk Tea")
      elif topping_action == "Remove":
        bubble_tea = MilkTea("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
        bubble_tea.remove_topping("Pearls", "Classic Milk Tea")
      if size == "Small":
        print("Your drink will be prepared as size", size)
      elif size == "Medium":
        print("Your drink will be prepared as size", size)
        MilkTea.order_cost = MilkTea.order_cost + 0.85
      elif size == "Large":
        print("Your drink sill be prepared as size", size)
        MilkTea.order_cost = MilkTea.order_cost + 1.20

      if ice_level in ("Low", "Medium", "High"):
        print("Your drink will have", ice_level, "ice")
          
      if sugar_level in ("Low", "Medium", "Large"):
        print("Your drink will have", sugar_level, "sugar")

      if tea_type in (MilkTea.milk_menu_dict[drink_name]):
        print("This drink contains", tea_type)
      elif tea_type not in (MilkTea.milk_menu_dict[drink_name]):
        print("This drink does not contain", tea_type)




  
  def fruit_order(self, drink_name, size, ice_level, sugar_level, tea_type):
      topping_action = input("Would you like to add or remove any toppings from your drink selection? [Add/Remove]")
      if topping_action == "Add":
        bubble_tea = FruitTea("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
        bubble_tea.add_topping("Cookie Crumb", "Classic Milk Tea")
      elif topping_action == "Remove":
        bubble_tea = FruitTea("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
        bubble_tea.remove_topping("Pearls", "Classic Milk Tea")
      if size == "Small":
        print("Your drink will be prepared as size", size)
      elif size == "Medium":
        print("Your drink will be prepared as size", size)
        FruitTea.order_cost = FruitTea.order_cost + 0.85
      elif size == "Large":
        print("Your drink sill be prepared as size", size)
        FruitTea.order_cost = FruitTea.order_cost + 1.20

      if ice_level in ("Low", "Medium", "High"):
        print("Your drink will have", ice_level, "ice")
          
      if sugar_level in ("Low", "Medium", "Large"):
        print("Your drink will have", sugar_level, "sugar")

      if tea_type in (FruitTea.fruit_menu_dict[drink_name]):
        print("This drink contains", tea_type)
      elif tea_type not in (FruitTea.fruit_menu_dict[drink_name]):
        print("This drink does not contain", tea_type)



  def sparkling_order(self, drink_name, size, ice_level, sugar_level, tea_type):
      topping_action = input("Would you like to add or remove any toppings from your drink selection? [Add/Remove]")
      if topping_action == "Add":
        bubble_tea = SparklingTea("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
        bubble_tea.add_topping("Cookie Crumb", "Classic Milk Tea")
      elif topping_action == "Remove":
        bubble_tea = SparklingTea("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
        bubble_tea.remove_topping("Pearls", "Classic Milk Tea")
      if size == "Small":
        print("Your drink will be prepared as size", size)
      elif size == "Medium":
        print("Your drink will be prepared as size", size)
        SparklingTea.order_cost = SparklingTea.order_cost + 0.85
      elif size == "Large":
        print("Your drink sill be prepared as size", size)
        SparklingTea.order_cost = SparklingTea.order_cost + 1.20

      if ice_level in ("Low", "Medium", "High"):
        print("Your drink will have", ice_level, "ice")
          
      if sugar_level in ("Low", "Medium", "Large"):
        print("Your drink will have", sugar_level, "sugar")

      if tea_type in (SparklingTea.sparkling_menu_dict[drink_name]):
        print("This drink contains", tea_type)
      elif tea_type not in (SparklingTea.sparkling_menu_dict[drink_name]):
        print("This drink does not contain", tea_type)




  def hot_order(self, drink_name, size, ice_level, sugar_level, tea_type):
      topping_action = input("Would you like to add or remove any toppings from your drink selection? [Add/Remove]")
      if topping_action == "Add":
        bubble_tea = HotTea("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
        bubble_tea.add_topping("Cookie Crumb", "Classic Milk Tea")
      elif topping_action == "Remove":
        bubble_tea = HotTea("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
        bubble_tea.remove_topping("Pearls", "Classic Milk Tea")
      if size == "Small":
        print("Your drink will be prepared as size", size)
      elif size == "Medium":
        print("Your drink will be prepared as size", size)
        HotTea.order_cost = HotTea.order_cost + 0.85
      elif size == "Large":
        print("Your drink sill be prepared as size", size)
        HotTea.order_cost = HotTea.order_cost + 1.20

      if ice_level in ("Low", "Medium", "High"):
        print("Your drink will have", ice_level, "ice")
          
      if sugar_level in ("Low", "Medium", "Large"):
        print("Your drink will have", sugar_level, "sugar")

      if tea_type in (HotTea.hot_menu_dict[drink_name]):
        print("This drink contains", tea_type)
      elif tea_type not in (HotTea.hot_menu_dict[drink_name]):
        print("This drink does not contain", tea_type)



  def frozen_order(self, drink_name, size, ice_level, sugar_level, tea_type):
      topping_action = input("Would you like to add or remove any toppings from your drink selection? [Add/Remove]") # create different methods for each of these in same class
      if topping_action == "Add":
        bubble_tea = FrozenTea("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
        bubble_tea.add_topping("Cookie Crumb", "Classic Milk Tea")
      elif topping_action == "Remove":
        bubble_tea = FrozenTea("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
        bubble_tea.remove_topping("Pearls", "Classic Milk Tea")
      if size == "Small":
        print("Your drink will be prepared as size", size)
      elif size == "Medium":
        print("Your drink will be prepared as size", size)
        FrozenTea.order_cost = FrozenTea.order_cost + 0.85
      elif size == "Large":
        print("Your drink sill be prepared as size", size)
        FrozenTea.order_cost = FrozenTea.order_cost + 1.20

      if ice_level in ("Low", "Medium", "High"):
        print("Your drink will have", ice_level, "ice")
          
      if sugar_level in ("Low", "Medium", "Large"):
        print("Your drink will have", sugar_level, "sugar")

      if tea_type in (FrozenTea.frozen_menu_dict[drink_name]):
        print("This drink contains", tea_type)
      elif tea_type not in (FrozenTea.frozen_menu_dict[drink_name]):
        print("This drink does not contain", tea_type)




  def order_drink(self, drink_name):
    print("Welcome to The Bubble Tea Store")
    print("-------------------------------")
    drink_type_select = input("What would you like to order? [Milky, Fruity, Sparkling, Hot, Frozen]")
    if drink_type_select in ("Fruity"):
        print(FruitTea.fruit_tea_name)
        print(MilkTea.milk_tea_name)
        print(SparklingTea.sprakling_tea_name)
        print(HotTea.hot_tea_name)
        print(FrozenTea.frozen_tea_name)
        if (drink_name in FruitTea.fruit_tea_name) or (drink_name in MilkTea.milk_tea_name) or (drink_name in SparklingTea.sprakling_tea_name) or (drink_name in HotTea.hot_tea_name) or (drink_name in FrozenTea.frozen_tea_name):
          print(" ")
          print("You have chosen", drink_name)
          if drink_name in FruitTea.fruit_menu_dict:
            print("This drink contains the following toppings:", (FruitTea.fruit_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "Medium", "Low", "Medium", "green tea", "Cookie Crumb", 10)
            add_remove.fruit_order()
            print("Your total for", drink_name, "is: $", FruitTea.order_cost)
            print("Thank you for ordering!")
          elif drink_name in MilkTea.milk_menu_dict:
            print("This drink contains the following toppings:", (MilkTea.milk_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "Medium", "Low", "Medium", "green tea", "Cookie Crumb", 10)
            add_remove.milk_order()
            print("Your total for", drink_name, "is: $", MilkTea.order_cost)
            print("Thank you for ordering!")
          elif drink_name in SparklingTea.sparkling_menu_dict:
            print("This drink contains the following toppings:", (SparklingTea.sparkling_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "Medium", "Low", "Medium", "green tea", "Cookie Crumb", 10)
            add_remove.sparkling_order()
            print("Your total for", drink_name, "is: $", SparklingTea.order_cost)
            print("Thank you for ordering!")
          elif drink_name in HotTea.hot_menu_dict:
            print("This drink contains the following toppings:", (HotTea.hot_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "Medium", "Low", "Medium", "green tea", "Cookie Crumb", 10)
            add_remove.hot_order()
            print("Your total for", drink_name, "is: $", HotTea.order_cost)
            print("Thank you for ordering!")
          elif drink_name in FrozenTea.frozen_menu_dict:
            print("This drink contains the following toppings:", (FrozenTea.frozen_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "Medium", "Low", "Medium", "green tea", "Cookie Crumb", 10)
            add_remove.frozen_order()
            print("Your total for", drink_name, "is: $", FrozenTea.order_cost)
            print("Thank you for ordering!")
        else:
          print("This drink is not available on our menu for this selection")


    elif drink_type_select in ("Milky", "Fruity", "Sparkling", "Hot", "Frozen"):
      print("Drink menu for", drink_type_select, "drinks:")
      if drink_type_select in ("Milky"):
        print(MilkTea.milk_tea_name)
        print(FruitTea.fruit_tea_name)
        print(HotTea.hot_tea_name)
        print(FrozenTea.frozen_tea_name)
        if (drink_name in MilkTea.milk_tea_name) or (drink_name in FruitTea.fruit_tea_name) or (drink_name in HotTea.hot_tea_name) or (drink_name in FrozenTea.frozen_tea_name):
          print(" ")
          print("You have chosen", drink_name)
          if drink_name in FruitTea.fruit_menu_dict:
            print("This drink contains the following toppings:", (FruitTea.fruit_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "Medium", "Low", "Medium", "green tea", "Cookie Crumb", 10)
            add_remove.fruit_order()
            print("Your total for", drink_name, "is: $", FruitTea.order_cost)
            print("Thank you for ordering!")
          elif drink_name in MilkTea.milk_menu_dict:
            print("This drink contains the following toppings:", (MilkTea.milk_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "Large", "Low", "Medium", "Green Tea", "Cookie Crumb", 10)
            add_remove.milk_order("Classic Milk Tea", "Large", "Low", "Medium", "Black Tea")
            print("Your total for", drink_name, "is: $", MilkTea.order_cost)
            print("Thank you for ordering!")
          elif drink_name in HotTea.hot_menu_dict:
            print("This drink contains the following toppings:", (HotTea.hot_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "Medium", "Low", "Medium", "green tea", "Cookie Crumb", 10)
            add_remove.hot_order()
            print("Your total for", drink_name, "is: $", HotTea.order_cost)
            print("Thank you for ordering!")
            print("Your total for", drink_name, "is: $", HotTea.order_cost)
          elif drink_name in FrozenTea.frozen_menu_dict:
            print("This drink contains the following toppings:", (FrozenTea.frozen_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "Medium", "Low", "Medium", "green tea", "Cookie Crumb", 10)
            add_remove.frozen_order()
            print("Your total for", drink_name, "is: $", FrozenTea.order_cost)
            print("Thank you for ordering!")
        else:
          print("This drink is not available on our menu for this selection")


      elif drink_type_select == "Sparkling":
        print(SparklingTea.sprakling_tea_name)
        print(FruitTea.fruit_tea_name)
        if (drink_name in SparklingTea.sprakling_tea_name) or (drink_name in FruitTea.fruit_tea_name):
          print(" ")
          print("You have chosen", drink_name)
          if drink_name in FruitTea.fruit_menu_dict:
            print("This drink contains the following toppings:", (FruitTea.fruit_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
            add_remove.fruit_order()
            print("Your total for", drink_name, "is: $", FruitTea.order_cost)               
            print("Thank you for ordering!")
          elif drink_name in SparklingTea.sparkling_menu_dict:
            print("This drink contains the following toppings:", (SparklingTea.sparkling_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
            add_remove.sparkling_order()
            print("Your total for", drink_name, "is: $", SparklingTea.order_cost)
            print("Thank you for ordering!")
        else:
          print("This drink is not available on our menu for this selection")


      elif drink_type_select == "Hot":
        print(HotTea.hot_tea_name)
        print(MilkTea.milk_tea_name)
        print(FruitTea.fruit_tea_name)
        if (drink_name in MilkTea.milk_tea_name) or (drink_name in FruitTea.fruit_tea_name) or (drink_name in HotTea.hot_tea_name):
          print(" ")
          print("You have chosen", drink_name)
          if drink_name in FruitTea.fruit_menu_dict:
            print("This drink contains the following toppings:", (FruitTea.fruit_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
            add_remove.fruit_order()
            print("Your total for", drink_name, "is: $", FruitTea.order_cost)
            print("Thank you for ordering!")
          elif drink_name in MilkTea.milk_menu_dict:
            print("This drink contains the following toppings:", (MilkTea.milk_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
            add_remove.milk_order()
            print("Your total for", drink_name, "is: $", MilkTea.order_cost)
            print("Thank you for ordering!")
          elif drink_name in HotTea.hot_menu_dict:
            print("This drink contains the following toppings:", (HotTea.hot_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
            add_remove.hot_order()
            print("Your total for", drink_name, "is: $", HotTea.order_cost)
            print("Thank you for ordering!")
        else:
          print("This drink is not available on our menu for this selection")


      elif drink_type_select == "Frozen":
        print(FrozenTea.frozen_tea_name)
        print(MilkTea.milk_tea_name)
        print(FruitTea.fruit_tea_name)
        if (drink_name in FrozenTea.frozen_tea_name) or (drink_name in MilkTea.milk_tea_name) or (drink_name in FruitTea.fruit_tea_name):
          print(" ")
          print("You have chosen", drink_name)
          if drink_name in FruitTea.fruit_menu_dict:
            print("This drink contains the following toppings:", (FruitTea.fruit_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
            add_remove.fruit_order()
            print("Your total for", drink_name, "is: $", FruitTea.order_cost)
            print("Thank you for ordering!")
          elif drink_name in MilkTea.milk_menu_dict:
            print("This drink contains the following toppings:", (MilkTea.milk_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
            add_remove.milk_order()
            print("Your total for", drink_name, "is: $", MilkTea.order_cost)
            print("Thank you for ordering!")
          elif drink_name in FrozenTea.frozen_menu_dict:
            print("This drink contains the following toppings:", (FrozenTea.frozen_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
            add_remove.frozen_order()
            print("Your total for", drink_name, "is: $", FrozenTea.order_cost)
            print("Thank you for ordering!")
        else:
          print("This drink is not available on our menu for this selection")


  def __str__(self):
    return f"{self.__drink_name} is ordered with additional toppings such as {self.__topping_name} and the total {Store.order_cost} is returned"



store = Store("Classic Milk Tea", "Medium", "Low", "Medium", "green tea", "Cookie Crumb", 10)
store.order_drink("Classic Milk Tea")
