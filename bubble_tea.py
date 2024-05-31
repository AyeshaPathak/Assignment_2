from abc import ABC, abstractmethod


class TeaType:
  def __init__(self):
    # will hold the various types of teas someone can order (4 different dictionaries holding drink name and ingredients)
    pass 


class BubbleTea(ABC, TeaType): # then utilise the dictionaries in the methods in this class 
  def __init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price):
    self.__drink_name = drink_name
    self.__size = size 
    self.__ice_level = ice_level
    self.__sugar_level = sugar_level
    self.__tea_type = tea_type
    self.__topping_name = topping_name
    self.__price = price 

  def get_drink_name(self):
    return self.__drink_name
    
  def set_drink_name(self, drink_name):
    self.drink_name = drink_name    
    
  def get_topping_name(self):
    return self.__topping_name 
    
  def set_topping_name(self, topping_name): 
    self.topping_name = topping_name 
    
  def add_topping(self, topping_name, drink_name):
    topping_list = ["Custard", "Mousse", "Pearls", "Cookie Crumb", "Mixed Jellies", "Herbal Jelly", "Coconut Jelly, Aloe Vera", "Mango Popping Pearls", "Strawberry Popping Pearls", "Apple Popping Pearls"] 
    if topping_name in topping_list:
      extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
      while extra_topping not in ("Yes", "No"):
        extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
      if extra_topping == "Yes":
        print("You have added extra", topping_name, "to", drink_name)
      elif extra_topping == "No":
        print(topping_name, "will not be added as an extra topping to", drink_name)
    elif topping_name not in topping_list:
      print(topping_name , "is not available as a topping for", drink_name)

  @abstractmethod
  def remove_topping(self, topping_name, drink_name):
    pass

    


class MilkFruit(BubbleTea):
  def __init__(self):
    pass


class SparklingHot(BubbleTea):
  def __init__(self):
    pass


class Frozen(BubbleTea):
  def __init__(self):
    pass





bubble_tea = BubbleTea("Green Tea and Matcha", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
bubble_tea.add_topping("Pearls", "Green Tea and Matcha")