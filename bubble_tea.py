  # add remove_topping method later
  # then string methods in all polymorphic classes 
  # then work on pricing method in store multiple inheritance class 
  # then testing stuff 
  # then divide into deperate modules with headers for each module 


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

  @abstractmethod
  def remove_topping(self, topping_name, drink_name):
    pass

  @abstractmethod
  def __str__(self):
    pass


class MilkTea(BubbleTea):
  def __init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price):
    super().__init__(drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
  milk_menu_dict = {"Green Tea Strawberry Matcha Latte": ["Matcha", "Milk", "Green Tea", "Ice", "Frozen Starwberries", "Strawberry Infused Tea"], "Classic Milk Tea": ["Sweetened Black Tea", "Milk", "Pearls"], "Cookie Crumble": ["Blended Oreo", "Milk", "Whipped Cream", "Cookie Crumb"], "Choco Blast": ["Chocolate Sauce", "Milk", "Shredded Chocolate"]}
  milk_tea_name = ["Green Tea Strawberry Matcha Latte", "Classic Milk Tea", "Cookie Cumble", "Choco Blast"]
  topping_list = ["Custard", "Mousse", "Pearls", "Cookie Crumb", "Mixed Jellies", "Herbal Jelly", "Coconut Jelly, Aloe Vera", "Mango Popping Pearls", "Strawberry Popping Pearls", "Apple Popping Pearls"] 

  def add_topping(self, topping_name, drink_name): 
    if drink_name in MilkTea.milk_menu_dict:
      extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
      if topping_name in (MilkTea.milk_menu_dict[drink_name]) and topping_name in MilkTea.topping_list:
        while extra_topping not in ("Yes", "No"):
          extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
        if extra_topping == "Yes":
          print("You have added extra", topping_name, "to", drink_name)
          print("Your final order is:", drink_name,":", (MilkTea.milk_menu_dict[drink_name]), "+",topping_name)
        elif extra_topping == "No":
          print(topping_name, "will not be added as an extra topping to", drink_name)
      elif topping_name not in MilkTea.topping_list:
        print(topping_name , "is not available as a topping for", drink_name)


  def remove_topping(self, topping_name, drink_name):
    if drink_name in MilkTea.milk_menu_dict:
      print("Your drink order contains the following toppings:", MilkTea.milk_menu_dict[drink_name])
      if topping_name in (MilkTea.milk_menu_dict[drink_name]) and topping_name in MilkTea.topping_list:
        minus_topping = input("Would you like to remove this topping from the drink? [Yes/No]")
        while minus_topping not in ("Yes", "No"):
          minus_topping = input("Would you like to remove this topping from the drink? [Yes/No]")
        if minus_topping == "Yes":
          print("You have removed", topping_name, "from", drink_name)
          print("Your final order is:", drink_name, ":", MilkTea.milk_menu_dict[drink_name], "-",topping_name)
        elif minus_topping == "No":
          print(topping_name, "will not be removed from", drink_name)
      elif topping_name not in MilkTea.topping_list[drink_name]:
        print(topping_name, "is not on", drink_name)
          
      
  def __str__(self):
    return f"{self.__topping_name} is removed from or added to {self.__drink_name} after filtering through {MilkTea.milk_menu_dict} and {MilkTea.topping_list}"



class FruitTea(BubbleTea):
  def __init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price):
    super().__init__(drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
  fruit_menu_dict = {"Mango and Passion Tea": ["Frozen Mango", "Passion Fruit", "Mango Popping Pearls"], "Strawberry Ice Blend": ["Frozen Strawberries", "Ice Cream", "Strawberry Infused Tea", "Strawberry Popping Pearls"], "Lemon and Blueberry Frenzy": ["Lemon Citrus Tea", "Blueberry Tea", "Lemon Extract"]}
  fruit_tea_name = ["Mango and Passion Tea", "Strawberry Ice Blend", "Lemon and Blueberry Frenzy"]
  topping_list = ["Custard", "Mousse", "Pearls", "Cookie Crumb", "Mixed Jellies", "Herbal Jelly", "Coconut Jelly, Aloe Vera", "Mango Popping Pearls", "Strawberry Popping Pearls", "Apple Popping Pearls"] 

  def add_topping(self, topping_name, drink_name): 
    if drink_name in FruitTea.fruit_menu_dict:
      extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
      if topping_name in (FruitTea.fruit_menu_dict[drink_name]) and topping_name in FruitTea.topping_list:
        while extra_topping not in ("Yes", "No"):
          extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
        if extra_topping == "Yes":
          print("You have added extra", topping_name, "to", drink_name)
          print("Your final order is:", drink_name,":", (FruitTea.fruit_menu_dict[drink_name]), "+",topping_name)
        elif extra_topping == "No":
          print(topping_name, "will not be added as an extra topping to", drink_name)
      elif topping_name not in FruitTea.topping_list:
        print(topping_name , "is not available as a topping for", drink_name)


  def remove_topping(self, topping_name, drink_name):
    if drink_name in FruitTea.fruit_menu_dict:
      print("Your drink order contains the following toppings:", FruitTea.fruit_menu_dict[drink_name])
      if topping_name in (FruitTea.fruit_menu_dict[drink_name]) and topping_name in FruitTea.topping_list:
        minus_topping = input("Would you like to remove this topping from the drink? [Yes/No]")
        while minus_topping not in ("Yes", "No"):
          minus_topping = input("Would you like to remove this topping from the drink? [Yes/No]")
        if minus_topping == "Yes":
          print("You have removed", topping_name, "from", drink_name)
          print("Your final order is:", drink_name, ":", FruitTea.fruit_menu_dict[drink_name], "-",topping_name)
        elif minus_topping == "No":
          print(topping_name, "will not be removed from", drink_name)
      elif topping_name not in FruitTea.topping_list[drink_name]:
        print(topping_name, "is not on", drink_name)

  def __str__(self):
    return f"{self.__topping_name} is removed from or added to {self.__drink_name} after filtering through {FruitTea.fruit_menu_dict} and {FruitTea.topping_list}"



class SparklingTea(BubbleTea):
  def __init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price):
    super().__init__(drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
  sparkling_menu_dict = {"Ginger Rose Tea": ["Ginger Extract", "Rose Tea"], "Watermelon Tea": ["Watermelon Tea", "Lemon Citrus Extract", "Herbal Jelly"]}
  sprakling_tea_name = ["Ginger Rose Tea", "Watermelon Tea"]
  topping_list = ["Custard", "Mousse", "Pearls", "Cookie Crumb", "Mixed Jellies", "Herbal Jelly", "Coconut Jelly, Aloe Vera", "Mango Popping Pearls", "Strawberry Popping Pearls", "Apple Popping Pearls"] 

  def add_topping(self, topping_name, drink_name): 
    if drink_name in SparklingTea.sparkling_menu_dict:
      extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
      if topping_name in (SparklingTea.sparkling_menu_dict[drink_name]) and topping_name in SparklingTea.topping_list:
        while extra_topping not in ("Yes", "No"):
          extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
        if extra_topping == "Yes":
          print("You have added extra", topping_name, "to", drink_name)
          print("Your final order is:", drink_name,":", (SparklingTea.sparkling_menu_dict[drink_name]), "+",topping_name)
        elif extra_topping == "No":
          print(topping_name, "will not be added as an extra topping to", drink_name)
      elif topping_name not in SparklingTea.topping_list:
        print(topping_name , "is not available as a topping for", drink_name)


  def remove_topping(self, topping_name, drink_name):
    if drink_name in SparklingTea.sparkling_menu_dict:
      print("Your drink order contains the following toppings:", SparklingTea.sparkling_menu_dict[drink_name])
      if topping_name in (SparklingTea.sparkling_menu_dict[drink_name]) and topping_name in SparklingTea.topping_list:
        minus_topping = input("Would you like to remove this topping from the drink? [Yes/No]")
        while minus_topping not in ("Yes", "No"):
          minus_topping = input("Would you like to remove this topping from the drink? [Yes/No]")
        if minus_topping == "Yes":
          print("You have removed", topping_name, "from", drink_name)
          print("Your final order is:", drink_name, ":", SparklingTea.sparkling_menu_dict[drink_name], "-",topping_name)
        elif minus_topping == "No":
          print(topping_name, "will not be removed from", drink_name)
      elif topping_name not in SparklingTea.topping_list[drink_name]:
        print(topping_name, "is not on", drink_name)


  def __str__(self):
    return f"{self.__topping_name} is removed from or added to {self.__drink_name} after filtering through {SparklingTea.sparkling_menu_dict} and {SparklingTea.topping_list}"



class HotTea(BubbleTea):
  def __init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price):
    super().__init__(drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
  hot_menu_dict = {"Ruby Grapefruit and Honey": ["Honey", "Grapefruit", "Honey", "Black Tea"], "Earl Grey Black Tea": ["Earl Grey Tea", "Black Tea"]}
  hot_tea_name = ["Ruby Grapefruit and Honey", "Earl Grey Black Tea"]
  topping_list = ["Custard", "Mousse", "Pearls", "Cookie Crumb", "Mixed Jellies", "Herbal Jelly", "Coconut Jelly, Aloe Vera", "Mango Popping Pearls", "Strawberry Popping Pearls", "Apple Popping Pearls"] 
  
  def add_topping(self, topping_name, drink_name): 
    if drink_name in HotTea.hot_menu_dict:
      extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
      if topping_name in (HotTea.hot_menu_dict[drink_name]) and topping_name in HotTea.topping_list:
        while extra_topping not in ("Yes", "No"):
          extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
        if extra_topping == "Yes":
          print("You have added extra", topping_name, "to", drink_name)
          print("Your final order is:", drink_name,":", (HotTea.hot_menu_dict[drink_name]), "+",topping_name)
        elif extra_topping == "No":
          print(topping_name, "will not be added as an extra topping to", drink_name)
      elif topping_name not in HotTea.topping_list:
        print(topping_name , "is not available as a topping for", drink_name)


  def remove_topping(self, topping_name, drink_name):
    if drink_name in HotTea.hot_menu_dict:
      print("Your drink order contains the following toppings:", HotTea.hot_menu_dict[drink_name])
      if topping_name in (HotTea.hot_menu_dict[drink_name]) and topping_name in HotTea.topping_list:
        minus_topping = input("Would you like to remove this topping from the drink? [Yes/No]")
        while minus_topping not in ("Yes", "No"):
          minus_topping = input("Would you like to remove this topping from the drink? [Yes/No]")
        if minus_topping == "Yes":
          print("You have removed", topping_name, "from", drink_name)
          print("Your final order is:", drink_name, ":", HotTea.hot_menu_dict[drink_name], "-",topping_name)
        elif minus_topping == "No":
          print(topping_name, "will not be removed from", drink_name)
      elif topping_name not in HotTea.topping_list[drink_name]:
        print(topping_name, "is not on", drink_name)


  def __str__(self):
    return f"{self.__topping_name} is removed from or added to {self.__drink_name} after filtering through {HotTea.hot_menu_dict} and {HotTea.topping_list}"




class FrozenTea(BubbleTea):
  def __init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price):
    super().__init__(drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
  frozen_menu_dict = {"Lychee Frozen": ["Frozen Lychee", "Mixed Jellies"], "Mango Frozen": ["Frozen mango"]}
  frozen_tea_name = ["Lychee Frozen", "Mango Frozen"]
  topping_list = ["Custard", "Mousse", "Pearls", "Cookie Crumb", "Mixed Jellies", "Herbal Jelly", "Coconut Jelly, Aloe Vera", "Mango Popping Pearls", "Strawberry Popping Pearls", "Apple Popping Pearls"] 

  def add_topping(self, topping_name, drink_name): 
    if drink_name in FrozenTea.frozen_menu_dict:
      extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
      if topping_name in (FrozenTea.frozen_menu_dict[drink_name]) and topping_name in FrozenTea.topping_list:
        while extra_topping not in ("Yes", "No"):
          extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
        if extra_topping == "Yes":
          print("You have added extra", topping_name, "to", drink_name)
          print("Your final order is:", drink_name,":", (FrozenTea.frozen_menu_dict[drink_name]), "+",topping_name)
        elif extra_topping == "No":
          print(topping_name, "will not be added as an extra topping to", drink_name)
      elif topping_name not in FrozenTea.topping_list:
        print(topping_name , "is not available as a topping for", drink_name)


  def remove_topping(self, topping_name, drink_name):
    if drink_name in FrozenTea.frozen_menu_dict:
      print("Your drink order contains the following toppings:", FrozenTea.frozen_menu_dict[drink_name])
      if topping_name in (FrozenTea.frozen_menu_dict[drink_name]) and topping_name in FrozenTea.topping_list:
        minus_topping = input("Would you like to remove this topping from the drink? [Yes/No]")
        while minus_topping not in ("Yes", "No"):
          minus_topping = input("Would you like to remove this topping from the drink? [Yes/No]")
        if minus_topping == "Yes":
          print("You have removed", topping_name, "from", drink_name)
          print("Your final order is:", drink_name, ":", FrozenTea.frozen_menu_dict[drink_name], "-",topping_name)
        elif minus_topping == "No":
          print(topping_name, "will not be removed from", drink_name)
      elif topping_name not in FrozenTea.topping_list[drink_name]:
        print(topping_name, "is not on", drink_name)


  def __str__(self):
    return f"{self.__topping_name} is removed from or added to {self.__drink_name} after filtering through {FrozenTea.frozen_menu_dict} and {FrozenTea.topping_list}"


class Store(MilkTea, FruitTea, SparklingTea, HotTea, FrozenTea, BubbleTea):
  def __inti__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price):
    BubbleTea.__init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
    MilkTea.__init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
    FruitTea.__init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
    SparklingTea.__init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
    HotTea.__init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
    FrozenTea.__init__(self, drink_name, size, ice_level, sugar_level, tea_type, topping_name, price)
    topping_price_dict = {"Custard" : "$1.00", "Mousse" : "$2.40", "Pearls" : "$1.20", "Cookie Crumb" :"$0.75", "Mixed Jellies" : "$0.35", "Herbal Jelly" : "$0.45", "Coconut Jelly" : "$0.50", "Aloe Vera" : "$0.70", "Mango Popping Pearls" : "$0.40", "Strawberry Popping Pearls" : "$0.40", "Apple Popping Pearls" : "$0.40"}
    store_earning = []
    order_history = []

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
          elif drink_name in MilkTea.milk_menu_dict:
            print("This drink contains the following toppings:", (MilkTea.milk_menu_dict[drink_name]))
          elif drink_name in SparklingTea.sparkling_menu_dict:
            print("This drink contains the following toppings:", (SparklingTea.sparkling_menu_dict[drink_name]))
          elif drink_name in HotTea.hot_menu_dict:
            print("This drink contains the following toppings:", (HotTea.hot_menu_dict[drink_name]))
          elif drink_name in FrozenTea.frozen_menu_dict:
            print("This drink contains the following toppings:", (FrozenTea.frozen_menu_dict[drink_name]))
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
          elif drink_name in MilkTea.milk_menu_dict:
            print("This drink contains the following toppings:", (MilkTea.milk_menu_dict[drink_name]))
          elif drink_name in HotTea.hot_menu_dict:
            print("This drink contains the following toppings:", (HotTea.hot_menu_dict[drink_name]))
          elif drink_name in FrozenTea.frozen_menu_dict:
            print("This drink contains the following toppings:", (FrozenTea.frozen_menu_dict[drink_name]))
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
          elif drink_name in SparklingTea.sparkling_menu_dict:
            print("This drink contains the following toppings:", (SparklingTea.sparkling_menu_dict[drink_name]))
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
          elif drink_name in MilkTea.milk_menu_dict:
            print("This drink contains the following toppings:", (MilkTea.milk_menu_dict[drink_name]))
          elif drink_name in HotTea.hot_menu_dict:
            print("This drink contains the following toppings:", (HotTea.hot_menu_dict[drink_name]))
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
          elif drink_name in MilkTea.milk_menu_dict:
            print("This drink contains the following toppings:", (MilkTea.milk_menu_dict[drink_name]))
          elif drink_name in FrozenTea.frozen_menu_dict:
            print("This drink contains the following toppings:", (FrozenTea.frozen_menu_dict[drink_name]))
        else:
          print("This drink is not available on our menu for this selection")



  # choosing what type of drink to order - depending on choice show a list of drinks (done)
  # display the topping's on the drink (done)
  # ask if customer wants to remove or add a topping 
  # if either then show either method then show final drink order 
  # ask if another drink needs to be ordered (if yes then it loops, if not then it continues)
  # ask addtional things from attributes 
  # if not then continue to display final drink order 
  # show total and display thank you message 


#bubble_tea = MilkTea("Green Tea Strawberry Matcha Latte", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
#bubble_tea.add_topping("Pearls", "Classic Milk Tea")
#bubble_tea.remove_topping("Cookie Crumb", "Cookie Crumble")

store = Store("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
store.order_drink("Classic Milk Tea")

# 9 days worth of commits done (one more remaining to meet mark)