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
  topping_price_dict = {"Custard" : 1.00, "Mousse" : 2.40, "Pearls" : 1.20, "Cookie Crumb" : 0.75, "Mixed Jellies" : 0.35, "Herbal Jelly" : 0.45, "Coconut Jelly" : 0.50, "Aloe Vera" : 0.70, "Mango Popping Pearls" : 0.40, "Strawberry Popping Pearls" : 0.40, "Apple Popping Pearls" : 0.40}

  fruit_topping = ["Mango", "Lychee", "Apple", "Grape", "Melon", "Grapefruit", "Lemon", "Guava", "PassionFruit", "Strawberry", "Pomegranate", "Peach", "Tropical", "Watermelon"]
  flavour_topping = ["Mint Choc", "Thai", "Salted Caramel", "Roasted", "Earl Grey", "Vanilla", "Assam", "Hazelnut", "Oolong", "Jasmine", "Matcha", "Premium", "Taro", "Chocolate"]
  fruit_topping_dict = {"Mango" : 0.30, "Lychee" : 0.10, "Apple" : 0.20, "Grape" : 0.40, "Melon" : 0.50, "Grapefruit" : 0.10, "Lemon" : 0.30, "Guava" : 0.20, "PassionFruit" : 0.25, "Strawberry" : 0.20, "Pomegranate" : 0.45, "Peach" : 0.10, "Tropical" : 0.65, "Watermelon" : 0.35}
  flavour_topping_dict = {"Mint Choc" : 0.30, "Thai" : 0.35, "Salted Caramel" : 0.20, "Roasted" : 0.40, "Earl Grey" : 0.50, "Vanilla" : 0.10, "Assam" : 0.30, "Hazelnut" : 0.20, "Oolong" : 0.25, "Jasmine" : 0.20, "Matcha" : 0.45, "Premium" : 0.10, "Taro" : 0.65, "Chocolate" : 0.40}

  order_cost = 4.50

  def add_topping(self, topping_name, drink_name): 
    if drink_name in MilkTea.milk_menu_dict:
      if topping_name in (MilkTea.milk_menu_dict[drink_name]) and topping_name in MilkTea.topping_list:
        extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
        while extra_topping not in ("Yes", "No"):
          if extra_topping == "Yes":
            MilkTea.order_cost = MilkTea.order_cost + (MilkTea.topping_price_dict[topping_name])
            print("You have added extra", topping_name, "to", drink_name)
            print("Your final order is:", drink_name,":", (MilkTea.milk_menu_dict[drink_name]), "+",topping_name)
          elif extra_topping == "No":
            print(topping_name, "will not be added as an extra topping to", drink_name)
      if topping_name not in (MilkTea.milk_menu_dict[drink_name]) and topping_name in MilkTea.topping_list:
        MilkTea.order_cost = MilkTea.order_cost + (MilkTea.topping_price_dict[topping_name])
        print("You have added", topping_name, "to", drink_name)
      elif topping_name not in MilkTea.topping_list:
        print(topping_name , "is not available as a topping for", drink_name)

    additional_choice = input("Would you like to add any additonal toppings or flavours to your drink? [Yes/No]")
    if additional_choice == "Yes":
      option = input("Fruit or Flavour? [Fruit/Flavour]")
      if option == "Fruit":
        print("Fruit choices:", MilkTea.fruit_topping)
        print(" ")
        choose_fruit =  input("What fruit do you want to add to your drink?")
        if choose_fruit in (MilkTea.fruit_topping):
          print("You have added", choose_fruit, "to", drink_name)
          MilkTea.order_cost = MilkTea.order_cost + (MilkTea.fruit_topping_dict[choose_fruit])
      elif option == "Flavour":
        print("Flavour choices:", MilkTea.flavour_topping)
        print(" ")
        choose_flavour =  input("What flavour do you want to add to your drink?")
        if choose_flavour in (MilkTea.flavour_topping):
          print("You have added", choose_flavour, "to", drink_name)
          MilkTea.order_cost = MilkTea.order_cost + (MilkTea.flavour_topping_dict[choose_flavour])
      print("Your total is:", MilkTea.order_cost)
    elif additional_choice == "No":
      print("Your total is:", MilkTea.order_cost)



  def remove_topping(self, topping_name, drink_name):
    if drink_name in MilkTea.milk_menu_dict: 
      if topping_name in (MilkTea.milk_menu_dict[drink_name]) and topping_name in MilkTea.topping_list:
        print("You are choosing to remove", topping_name, "from", drink_name)
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
  fruit_menu_dict = {"Mango and Passion Tea": ["Frozen Mango", "Passion Fruit", "Mango Popping Pearls", "Green Tea"], "Strawberry Ice Blend": ["Frozen Strawberries", "Ice Cream", "Strawberry Infused Tea", "Strawberry Popping Pearls"], "Lemon and Blueberry Frenzy": ["Lemon Citrus Tea", "Blueberry Tea", "Lemon Extract"]}
  fruit_tea_name = ["Mango and Passion Tea", "Strawberry Ice Blend", "Lemon and Blueberry Frenzy"]
  topping_list = ["Custard", "Mousse", "Pearls", "Cookie Crumb", "Mixed Jellies", "Herbal Jelly", "Coconut Jelly, Aloe Vera", "Mango Popping Pearls", "Strawberry Popping Pearls", "Apple Popping Pearls"] 
  topping_price_dict = {"Custard" : 1.00, "Mousse" : 2.40, "Pearls" : 1.20, "Cookie Crumb" : 0.75, "Mixed Jellies" : 0.35, "Herbal Jelly" : 0.45, "Coconut Jelly" : 0.50, "Aloe Vera" : 0.70, "Mango Popping Pearls" : 0.40, "Strawberry Popping Pearls" : 0.40, "Apple Popping Pearls" : 0.40}
  
  fruit_topping = ["Mango", "Lychee", "Apple", "Grape", "Melon", "Grapefruit", "Lemon", "Guava", "PassionFruit", "Strawberry", "Pomegranate", "Peach", "Tropical", "Watermelon"]
  flavour_topping = ["Mint Choc", "Thai", "Salted Caramel", "Roasted", "Earl Grey", "Vanilla", "Assam", "Hazelnut", "Oolong", "Jasmine", "Matcha", "Premium", "Taro", "Chocolate"]
  fruit_topping_dict = {"Mango" : 0.30, "Lychee" : 0.10, "Apple" : 0.20, "Grape" : 0.40, "Melon" : 0.50, "Grapefruit" : 0.10, "Lemon" : 0.30, "Guava" : 0.20, "PassionFruit" : 0.25, "Strawberry" : 0.20, "Pomegranate" : 0.45, "Peach" : 0.10, "Tropical" : 0.65, "Watermelon" : 0.35}
  flavour_topping_dict = {"Mint Choc" : 0.30, "Thai" : 0.35, "Salted Caramel" : 0.20, "Roasted" : 0.40, "Earl Grey" : 0.50, "Vanilla" : 0.10, "Assam" : 0.30, "Hazelnut" : 0.20, "Oolong" : 0.25, "Jasmine" : 0.20, "Matcha" : 0.45, "Premium" : 0.10, "Taro" : 0.65, "Chocolate" : 0.40}

  order_cost = 4.50

  def add_topping(self, topping_name, drink_name): 
    if drink_name in FruitTea.fruit_menu_dict:
      extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
      if topping_name in (FruitTea.fruit_menu_dict[drink_name]) and topping_name in FruitTea.topping_list:
        while extra_topping not in ("Yes", "No"):
          extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
        if extra_topping == "Yes":
          FruitTea.order_cost = FruitTea.order_cost + (FruitTea.topping_price_dict[topping_name])
          print("You have added extra", topping_name, "to", drink_name)
          print("Your final order is:", drink_name,":", (FruitTea.fruit_menu_dict[drink_name]), "+",topping_name)
        elif extra_topping == "No":
          print(topping_name, "will not be added as an extra topping to", drink_name)
      if topping_name not in (FruitTea.fruit_menu_dict[drink_name]) and topping_name in FruitTea.topping_list:
        FruitTea.order_cost = FruitTea.order_cost + (FruitTea.topping_price_dict[topping_name])
        print("You have added", topping_name, "to", drink_name)
      elif topping_name not in FruitTea.topping_list:
        print(topping_name , "is not available as a topping for", drink_name)

    additional_choice = input("Would you like to add any additonal toppings or flavours to your drink? [Yes/No]")
    if additional_choice == "Yes":
      option = input("Fruit or Flavour? [Fruit/Flavour]")
      if option == "Fruit":
        print("Fruit choices:", FruitTea.fruit_topping)
        print(" ")
        choose_fruit =  input("What fruit do you want to add to your drink?")
        if choose_fruit in (FruitTea.fruit_topping):
          print("You have added", choose_fruit, "to", drink_name)
          FruitTea.order_cost = FruitTea.order_cost + (FruitTea.fruit_topping_dict[choose_fruit])
      elif option == "Flavour":
        print("Flavour choices:", FruitTea.flavour_topping)
        print(" ")
        choose_flavour =  input("What flavour do you want to add to your drink?")
        if choose_flavour in (FruitTea.flavour_topping):
          print("You have added", choose_flavour, "to", drink_name)
          FruitTea.order_cost = FruitTea.order_cost + (FruitTea.flavour_topping_dict[choose_flavour])
      print("Your total is:", FruitTea.order_cost)
    elif additional_choice == "No":
      print("Your total is:", FruitTea.order_cost)


  def remove_topping(self, topping_name, drink_name):
    if drink_name in FruitTea.fruit_menu_dict:
      if topping_name in (FruitTea.fruit_menu_dict[drink_name]) and topping_name in FruitTea.topping_list:
        print("You are choosing to remove", topping_name, "from", drink_name)
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
  topping_price_dict = {"Custard" : 1.00, "Mousse" : 2.40, "Pearls" : 1.20, "Cookie Crumb" : 0.75, "Mixed Jellies" : 0.35, "Herbal Jelly" : 0.45, "Coconut Jelly" : 0.50, "Aloe Vera" : 0.70, "Mango Popping Pearls" : 0.40, "Strawberry Popping Pearls" : 0.40, "Apple Popping Pearls" : 0.40}
  
  fruit_topping = ["Mango", "Lychee", "Apple", "Grape", "Melon", "Grapefruit", "Lemon", "Guava", "PassionFruit", "Strawberry", "Pomegranate", "Peach", "Tropical", "Watermelon"]
  flavour_topping = ["Mint Choc", "Thai", "Salted Caramel", "Roasted", "Earl Grey", "Vanilla", "Assam", "Hazelnut", "Oolong", "Jasmine", "Matcha", "Premium", "Taro", "Chocolate"]
  fruit_topping_dict = {"Mango" : 0.30, "Lychee" : 0.10, "Apple" : 0.20, "Grape" : 0.40, "Melon" : 0.50, "Grapefruit" : 0.10, "Lemon" : 0.30, "Guava" : 0.20, "PassionFruit" : 0.25, "Strawberry" : 0.20, "Pomegranate" : 0.45, "Peach" : 0.10, "Tropical" : 0.65, "Watermelon" : 0.35}
  flavour_topping_dict = {"Mint Choc" : 0.30, "Thai" : 0.35, "Salted Caramel" : 0.20, "Roasted" : 0.40, "Earl Grey" : 0.50, "Vanilla" : 0.10, "Assam" : 0.30, "Hazelnut" : 0.20, "Oolong" : 0.25, "Jasmine" : 0.20, "Matcha" : 0.45, "Premium" : 0.10, "Taro" : 0.65, "Chocolate" : 0.40}

  order_cost = 4.50

  def add_topping(self, topping_name, drink_name): 
    if drink_name in SparklingTea.sparkling_menu_dict:
      extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
      if topping_name in (SparklingTea.sparkling_menu_dict[drink_name]) and topping_name in SparklingTea.topping_list:
        while extra_topping not in ("Yes", "No"):
          extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
        if extra_topping == "Yes":
          SparklingTea.order_cost = SparklingTea.order_cost + (SparklingTea.topping_price_dict[topping_name])
          print("You have added extra", topping_name, "to", drink_name)
          print("Your final order is:", drink_name,":", (SparklingTea.sparkling_menu_dict[drink_name]), "+",topping_name)
        elif extra_topping == "No":
          print(topping_name, "will not be added as an extra topping to", drink_name)
      if topping_name not in (SparklingTea.sparkling_menu_dict[drink_name]) and topping_name in SparklingTea.topping_list:
        SparklingTea.order_cost = SparklingTea.order_cost + (SparklingTea.topping_price_dict[topping_name])
        print("You have added", topping_name, "to", drink_name)
      elif topping_name not in SparklingTea.topping_list:
        print(topping_name , "is not available as a topping for", drink_name)

    additional_choice = input("Would you like to add any additonal toppings or flavours to your drink? [Yes/No]")
    if additional_choice == "Yes":
      option = input("Fruit or Flavour? [Fruit/Flavour]")
      if option == "Fruit":
        print("Fruit choices:", SparklingTea.fruit_topping)
        print(" ")
        choose_fruit =  input("What fruit do you want to add to your drink?")
        if choose_fruit in (SparklingTea.fruit_topping):
          print("You have added", choose_fruit, "to", drink_name)
          SparklingTea.order_cost = SparklingTea.order_cost + (SparklingTea.fruit_topping_dict[choose_fruit])
      elif option == "Flavour":
        print("Flavour choices:", SparklingTea.flavour_topping)
        print(" ")
        choose_flavour =  input("What flavour do you want to add to your drink?")
        if choose_flavour in (SparklingTea.flavour_topping):
          print("You have added", choose_flavour, "to", drink_name)
          SparklingTea.order_cost = SparklingTea.order_cost + (SparklingTea.flavour_topping_dict[choose_flavour])
      print("Your total is:", SparklingTea.order_cost)
    elif additional_choice == "No":
      print("Your total is:", SparklingTea.order_cost)


  def remove_topping(self, topping_name, drink_name):
    if drink_name in SparklingTea.sparkling_menu_dict:
      if topping_name in (SparklingTea.sparkling_menu_dict[drink_name]) and topping_name in SparklingTea.topping_list:
        print("You are choosing to remove", topping_name, "from", drink_name)
        minus_topping = input("Would you like to remove this topping from the drink? [Yes/No]")
        while minus_topping not in ("Yes", "No"):
          minus_topping = input("Would you like to remove this topping from the drink? [Yes/No]")
        if minus_topping == "Yes":
          print("You have removed", topping_name, "from", drink_name)
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
  topping_price_dict = {"Custard" : 1.00, "Mousse" : 2.40, "Pearls" : 1.20, "Cookie Crumb" : 0.75, "Mixed Jellies" : 0.35, "Herbal Jelly" : 0.45, "Coconut Jelly" : 0.50, "Aloe Vera" : 0.70, "Mango Popping Pearls" : 0.40, "Strawberry Popping Pearls" : 0.40, "Apple Popping Pearls" : 0.40}

  fruit_topping = ["Mango", "Lychee", "Apple", "Grape", "Melon", "Grapefruit", "Lemon", "Guava", "PassionFruit", "Strawberry", "Pomegranate", "Peach", "Tropical", "Watermelon"]
  flavour_topping = ["Mint Choc", "Thai", "Salted Caramel", "Roasted", "Earl Grey", "Vanilla", "Assam", "Hazelnut", "Oolong", "Jasmine", "Matcha", "Premium", "Taro", "Chocolate"]
  fruit_topping_dict = {"Mango" : 0.30, "Lychee" : 0.10, "Apple" : 0.20, "Grape" : 0.40, "Melon" : 0.50, "Grapefruit" : 0.10, "Lemon" : 0.30, "Guava" : 0.20, "PassionFruit" : 0.25, "Strawberry" : 0.20, "Pomegranate" : 0.45, "Peach" : 0.10, "Tropical" : 0.65, "Watermelon" : 0.35}
  flavour_topping_dict = {"Mint Choc" : 0.30, "Thai" : 0.35, "Salted Caramel" : 0.20, "Roasted" : 0.40, "Earl Grey" : 0.50, "Vanilla" : 0.10, "Assam" : 0.30, "Hazelnut" : 0.20, "Oolong" : 0.25, "Jasmine" : 0.20, "Matcha" : 0.45, "Premium" : 0.10, "Taro" : 0.65, "Chocolate" : 0.40}

  order_cost = 4.50

  def add_topping(self, topping_name, drink_name): 
    if drink_name in HotTea.hot_menu_dict:
      extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
      if topping_name in (HotTea.hot_menu_dict[drink_name]) and topping_name in HotTea.topping_list:
        while extra_topping not in ("Yes", "No"):
          extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
        if extra_topping == "Yes":
          HotTea.order_cost = HotTea.order_cost + (HotTea.topping_price_dict[topping_name])
          print("You have added extra", topping_name, "to", drink_name)
          print("Your final order is:", drink_name,":", (HotTea.hot_menu_dict[drink_name]), "+",topping_name)
        elif extra_topping == "No":
          print(topping_name, "will not be added as an extra topping to", drink_name)
      if topping_name not in (HotTea.hot_menu_dict[drink_name]) and topping_name in HotTea.topping_list:
        HotTea.order_cost = HotTea.order_cost + (HotTea.topping_price_dict[topping_name])
        print("You have added", topping_name, "to", drink_name)
      elif topping_name not in HotTea.topping_list:
        print(topping_name , "is not available as a topping for", drink_name)

    additional_choice = input("Would you like to add any additonal toppings or flavours to your drink? [Yes/No]")
    if additional_choice == "Yes":
      option = input("Fruit or Flavour? [Fruit/Flavour]")
      if option == "Fruit":
        print("Fruit choices:", HotTea.fruit_topping)
        print(" ")
        choose_fruit =  input("What fruit do you want to add to your drink?")
        if choose_fruit in (HotTea.fruit_topping):
          print("You have added", choose_fruit, "to", drink_name)
          HotTea.order_cost = HotTea.order_cost + (HotTea.fruit_topping_dict[choose_fruit])
      elif option == "Flavour":
        print("Flavour choices:", HotTea.flavour_topping)
        print(" ")
        choose_flavour =  input("What flavour do you want to add to your drink?")
        if choose_flavour in (HotTea.flavour_topping):
          print("You have added", choose_flavour, "to", drink_name)
          HotTea.order_cost = HotTea.order_cost + (HotTea.flavour_topping_dict[choose_flavour])
      print("Your total is:", HotTea.order_cost)
    elif additional_choice == "No":
      print("Your total is:", HotTea.order_cost)

  def remove_topping(self, topping_name, drink_name):
    if drink_name in HotTea.hot_menu_dict:
      if topping_name in (HotTea.hot_menu_dict[drink_name]) and topping_name in HotTea.topping_list:
        print("You are choosing to remove", topping_name, "from", drink_name)
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
  topping_price_dict = {"Custard" : 1.00, "Mousse" : 2.40, "Pearls" : 1.20, "Cookie Crumb" : 0.75, "Mixed Jellies" : 0.35, "Herbal Jelly" : 0.45, "Coconut Jelly" : 0.50, "Aloe Vera" : 0.70, "Mango Popping Pearls" : 0.40, "Strawberry Popping Pearls" : 0.40, "Apple Popping Pearls" : 0.40}
  
  fruit_topping = ["Mango", "Lychee", "Apple", "Grape", "Melon", "Grapefruit", "Lemon", "Guava", "PassionFruit", "Strawberry", "Pomegranate", "Peach", "Tropical", "Watermelon"]
  flavour_topping = ["Mint Choc", "Thai", "Salted Caramel", "Roasted", "Earl Grey", "Vanilla", "Assam", "Hazelnut", "Oolong", "Jasmine", "Matcha", "Premium", "Taro", "Chocolate"]
  fruit_topping_dict = {"Mango" : 0.30, "Lychee" : 0.10, "Apple" : 0.20, "Grape" : 0.40, "Melon" : 0.50, "Grapefruit" : 0.10, "Lemon" : 0.30, "Guava" : 0.20, "PassionFruit" : 0.25, "Strawberry" : 0.20, "Pomegranate" : 0.45, "Peach" : 0.10, "Tropical" : 0.65, "Watermelon" : 0.35}
  flavour_topping_dict = {"Mint Choc" : 0.30, "Thai" : 0.35, "Salted Caramel" : 0.20, "Roasted" : 0.40, "Earl Grey" : 0.50, "Vanilla" : 0.10, "Assam" : 0.30, "Hazelnut" : 0.20, "Oolong" : 0.25, "Jasmine" : 0.20, "Matcha" : 0.45, "Premium" : 0.10, "Taro" : 0.65, "Chocolate" : 0.40}

  order_cost = 4.50

  def add_topping(self, topping_name, drink_name): 
    if drink_name in FrozenTea.frozen_menu_dict:
      extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
      if topping_name in (FrozenTea.frozen_menu_dict[drink_name]) and topping_name in FrozenTea.topping_list:
        while extra_topping not in ("Yes", "No"):
          extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
        if extra_topping == "Yes":
          FrozenTea.order_cost = FrozenTea.order_cost + (FrozenTea.topping_price_dict[topping_name])
          print("You have added extra", topping_name, "to", drink_name)
          print("Your final order is:", drink_name,":", (FrozenTea.frozen_menu_dict[drink_name]), "+",topping_name)
        elif extra_topping == "No":
          print(topping_name, "will not be added as an extra topping to", drink_name)
      if topping_name not in (FrozenTea.frozen_menu_dict[drink_name]) and topping_name in FrozenTea.topping_list:
        FrozenTea.order_cost = FrozenTea.order_cost + (FrozenTea.topping_price_dict[topping_name])
        print("You have added", topping_name, "to", drink_name)
      elif topping_name not in FrozenTea.topping_list:
        print(topping_name , "is not available as a topping for", drink_name)

    additional_choice = input("Would you like to add any additonal toppings or flavours to your drink? [Yes/No]")
    if additional_choice == "Yes":
      option = input("Fruit or Flavour? [Fruit/Flavour]")
      if option == "Fruit":
        print("Fruit choices:", FrozenTea.fruit_topping)
        print(" ")
        choose_fruit =  input("What fruit do you want to add to your drink?")
        if choose_fruit in (FrozenTea.fruit_topping):
          print("You have added", choose_fruit, "to", drink_name)
          FrozenTea.order_cost = FrozenTea.order_cost + (FrozenTea.fruit_topping_dict[choose_fruit])
      elif option == "Flavour":
        print("Flavour choices:", FrozenTea.flavour_topping)
        print(" ")
        choose_flavour =  input("What flavour do you want to add to your drink?")
        if choose_flavour in (FrozenTea.flavour_topping):
          print("You have added", choose_flavour, "to", drink_name)
          FrozenTea.order_cost = FrozenTea.order_cost + (FrozenTea.flavour_topping_dict[choose_flavour])
      print("Your total is:", FrozenTea.order_cost)
    elif additional_choice == "No":
      print("Your total is:", FrozenTea.order_cost)


  def remove_topping(self, topping_name, drink_name):
    if drink_name in FrozenTea.frozen_menu_dict:
      if topping_name in (FrozenTea.frozen_menu_dict[drink_name]) and topping_name in FrozenTea.topping_list:
        print("You are choosing to remove", topping_name, "from", drink_name)
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
    store_earning = 0
    order_history = []

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
          elif drink_name in MilkTea.milk_menu_dict:
            print("This drink contains the following toppings:", (MilkTea.milk_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "Medium", "Low", "Medium", "green tea", "Cookie Crumb", 10)
            add_remove.milk_order()
          elif drink_name in SparklingTea.sparkling_menu_dict:
            print("This drink contains the following toppings:", (SparklingTea.sparkling_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "Medium", "Low", "Medium", "green tea", "Cookie Crumb", 10)
            add_remove.sparkling_order()
          elif drink_name in HotTea.hot_menu_dict:
            print("This drink contains the following toppings:", (HotTea.hot_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "Medium", "Low", "Medium", "green tea", "Cookie Crumb", 10)
            add_remove.hot_order()
          elif drink_name in FrozenTea.frozen_menu_dict:
            print("This drink contains the following toppings:", (FrozenTea.frozen_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "Medium", "Low", "Medium", "green tea", "Cookie Crumb", 10)
            add_remove.frozen_order()
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
          elif drink_name in MilkTea.milk_menu_dict:
            print("This drink contains the following toppings:", (MilkTea.milk_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "Large", "Low", "Medium", "Green Tea", "Cookie Crumb", 10)
            add_remove.milk_order("Classic Milk Tea", "Large", "Low", "Medium", "Black Tea")
          elif drink_name in HotTea.hot_menu_dict:
            print("This drink contains the following toppings:", (HotTea.hot_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "Medium", "Low", "Medium", "green tea", "Cookie Crumb", 10)
            add_remove.hot_order()
          elif drink_name in FrozenTea.frozen_menu_dict:
            print("This drink contains the following toppings:", (FrozenTea.frozen_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "Medium", "Low", "Medium", "green tea", "Cookie Crumb", 10)
            add_remove.frozen_order()
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
          elif drink_name in SparklingTea.sparkling_menu_dict:
            print("This drink contains the following toppings:", (SparklingTea.sparkling_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
            add_remove.sparkling_order()
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
          elif drink_name in MilkTea.milk_menu_dict:
            print("This drink contains the following toppings:", (MilkTea.milk_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
            add_remove.milk_order()
          elif drink_name in HotTea.hot_menu_dict:
            print("This drink contains the following toppings:", (HotTea.hot_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
            add_remove.hot_order()
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
          elif drink_name in MilkTea.milk_menu_dict:
            print("This drink contains the following toppings:", (MilkTea.milk_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
            add_remove.milk_order()
          elif drink_name in FrozenTea.frozen_menu_dict:
            print("This drink contains the following toppings:", (FrozenTea.frozen_menu_dict[drink_name]))
            add_remove = Store("Classic Milk Tea", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
            add_remove.frozen_order()
        else:
          print("This drink is not available on our menu for this selection")



 # ask addtional things from attributes 
 # pricing 
  # show final order and order total and display thank you message 


#bubble_tea = MilkTea("Green Tea Strawberry Matcha Latte", "medium", "low", "medium", "green tea", "Cookie Crumb", 10)
#bubble_tea.add_topping("Pearls", "Classic Milk Tea")
#bubble_tea.remove_topping("Cookie Crumb", "Cookie Crumble")

store = Store("Classic Milk Tea", "Medium", "Low", "Medium", "green tea", "Cookie Crumb", 10)
store.order_drink("Classic Milk Tea")

