# after completed - divide classes into seperate modules 
# add a header to each module 
# add string method to each class 


from abc import ABC, abstractmethod


class BubbleTea(ABC):
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


  @abstractmethod
  def add_topping(self, topping_name, drink_name):
    pass


  # add remove_topping method later
    


class MilkTea(BubbleTea):
  def __init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price):
    super().__init__(drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
  milk_menu_dict = {"Green Tea Strawberry Matcha Latte": ["Matcha", "Milk", "Green Tea", "Ice", "Frozen Starwberries", "Strawberry Infused Tea"], "Classic Milk Tea": ["Sweetened Black Tea", "Milk", "Pearls"], "Cookie Crumble": ["Blended Oreo", "Milk", "Whipped Cream", "Cookie Crumb"], "Choco Blast": ["Chocolate Sauce", "Milk", "Shredded Chocolate"]} 

  def add_topping(self, topping_name, drink_name): 
    topping_list = ["Custard", "Mousse", "Pearls", "Cookie Crumb", "Mixed Jellies", "Herbal Jelly", "Coconut Jelly, Aloe Vera", "Mango Popping Pearls", "Strawberry Popping Pearls", "Apple Popping Pearls"] 

    if drink_name in MilkTea.milk_menu_dict:
      extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
      if topping_name in (MilkTea.milk_menu_dict[drink_name]) and topping_name in topping_list:
        while extra_topping not in ("Yes", "No"):
          extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
        if extra_topping == "Yes":
          print("You have added extra", topping_name, "to", drink_name)
          print("Your final order is:", drink_name,":", (MilkTea.milk_menu_dict[drink_name]), "+",topping_name)
        elif extra_topping == "No":
          print(topping_name, "will not be added as an extra topping to", drink_name)
      elif topping_name not in topping_list:
        print(topping_name , "is not available as a topping for", drink_name)


class FruitTea(BubbleTea):
  def __init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price):
    super().__init__(drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
  fruit_menu_dict = {"Mango and Passion Tea": ["Frozen Mango", "Passion Fruit", "Mango Popping Pearls"], "Strawberry Ice Blend": ["Frozen Strawberries", "Ice Cream", "Strawberry Infused Tea", "Strawberry Popping Pearls"], "Lemon and Blueberry Frenzy": ["Lemon Citrus Tea", "Blueberry Tea", "Lemon Extract"]}

  def add_topping(self, topping_name, drink_name): 
    topping_list = ["Custard", "Mousse", "Pearls", "Cookie Crumb", "Mixed Jellies", "Herbal Jelly", "Coconut Jelly, Aloe Vera", "Mango Popping Pearls", "Strawberry Popping Pearls", "Apple Popping Pearls"] 

    if drink_name in FruitTea.fruit_menu_dict:
      extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
      if topping_name in (FruitTea.fruit_menu_dict[drink_name]) and topping_name in topping_list:
        while extra_topping not in ("Yes", "No"):
          extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
        if extra_topping == "Yes":
          print("You have added extra", topping_name, "to", drink_name)
          print("Your final order is:", drink_name,":", (FruitTea.fruit_menu_dict[drink_name]), "+",topping_name)
        elif extra_topping == "No":
          print(topping_name, "will not be added as an extra topping to", drink_name)
      elif topping_name not in topping_list:
        print(topping_name , "is not available as a topping for", drink_name)



class SparklingTea(BubbleTea):
  def __init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price):
    super().__init__(drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
  sparkling_menu_dict = {"Ginger Rose Tea": ["Ginger Extract", "Rose Tea"], "Watermelon Tea": ["Watermelon Tea", "Lemon Citrus Extract", "Herbal Jelly"]}

  def add_topping(self, topping_name, drink_name): 
    topping_list = ["Custard", "Mousse", "Pearls", "Cookie Crumb", "Mixed Jellies", "Herbal Jelly", "Coconut Jelly, Aloe Vera", "Mango Popping Pearls", "Strawberry Popping Pearls", "Apple Popping Pearls"] 

    if drink_name in SparklingTea.sparkling_menu_dict:
      extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
      if topping_name in (SparklingTea.sparkling_menu_dict[drink_name]) and topping_name in topping_list:
        while extra_topping not in ("Yes", "No"):
          extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
        if extra_topping == "Yes":
          print("You have added extra", topping_name, "to", drink_name)
          print("Your final order is:", drink_name,":", (SparklingTea.sparkling_menu_dict[drink_name]), "+",topping_name)
        elif extra_topping == "No":
          print(topping_name, "will not be added as an extra topping to", drink_name)
      elif topping_name not in topping_list:
        print(topping_name , "is not available as a topping for", drink_name)



class HotTea(BubbleTea):
  def __init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price):
    super().__init__(drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
  hot_menu_dict = {"Ruby Grapefruit and Honey": ["Honey", "Grapefruit", "Honey", "Black Tea"], "Earl Grey Black Tea": ["Earl Grey Tea", "Black Tea"]}

  def add_topping(self, topping_name, drink_name): 
    topping_list = ["Custard", "Mousse", "Pearls", "Cookie Crumb", "Mixed Jellies", "Herbal Jelly", "Coconut Jelly, Aloe Vera", "Mango Popping Pearls", "Strawberry Popping Pearls", "Apple Popping Pearls"] 

    if drink_name in HotTea.hot_menu_dict:
      extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
      if topping_name in (HotTea.hot_menu_dict[drink_name]) and topping_name in topping_list:
        while extra_topping not in ("Yes", "No"):
          extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
        if extra_topping == "Yes":
          print("You have added extra", topping_name, "to", drink_name)
          print("Your final order is:", drink_name,":", (HotTea.hot_menu_dict[drink_name]), "+",topping_name)
        elif extra_topping == "No":
          print(topping_name, "will not be added as an extra topping to", drink_name)
      elif topping_name not in topping_list:
        print(topping_name , "is not available as a topping for", drink_name)



class FrozenTea(BubbleTea):
  def __init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price):
    super().__init__(drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
  frozen_menu_dict = {"Lychee Frozen": ["Frozen Lychee", "Mixed Jellies"], "Mango Frozen": ["Frozen mango"]}

  def add_topping(self, topping_name, drink_name): 
    topping_list = ["Custard", "Mousse", "Pearls", "Cookie Crumb", "Mixed Jellies", "Herbal Jelly", "Coconut Jelly, Aloe Vera", "Mango Popping Pearls", "Strawberry Popping Pearls", "Apple Popping Pearls"] 

    if drink_name in FrozenTea.frozen_menu_dict:
      extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
      if topping_name in (FrozenTea.frozen_menu_dict[drink_name]) and topping_name in topping_list:
        while extra_topping not in ("Yes", "No"):
          extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
        if extra_topping == "Yes":
          print("You have added extra", topping_name, "to", drink_name)
          print("Your final order is:", drink_name,":", (FrozenTea.frozen_menu_dict[drink_name]), "+",topping_name)
        elif extra_topping == "No":
          print(topping_name, "will not be added as an extra topping to", drink_name)
      elif topping_name not in topping_list:
        print(topping_name , "is not available as a topping for", drink_name)




class Store(MilkTea, FruitTea, SparklingTea, HotTea, FrozenTea, BubbleTea):
  def __inti__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price):
    BubbleTea.__init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
    MilkTea.__init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
    FruitTea.__init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
    SparklingTea.__init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
    HotTea.__init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
    FrozenTea.__init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)





bubble_tea = MilkTea("Green Tea and Matcha", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
bubble_tea.add_topping("Pearls", "Classic Milk Tea")
