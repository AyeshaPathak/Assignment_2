'''
File: hot_tea.py
Description: This module contains the polymorphic class HotTea and its methods for adding and removing toppings.
Author: Ayesha Pathak
ID: 1104095812
Username: patay096
This is my own work as defined by the University's Academic Misconduct Policy.
'''


from bubble_tea import BubbleTea


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
  store_earning = 0

  def add_topping(self, topping_name, drink_name): 
    if drink_name in HotTea.hot_menu_dict:
      extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
      if topping_name in (HotTea.hot_menu_dict[drink_name]) and topping_name in HotTea.topping_list:
        while extra_topping not in ("Yes", "No"):
          extra_topping = input("This topping is already on this drink. Would you like to add extra? [Yes/No]")
        if extra_topping == "Yes":
          HotTea.order_cost = HotTea.order_cost + (HotTea.topping_price_dict[topping_name])
          print("You have added extra", topping_name, "to", drink_name)
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
      print("Your total after toppings is: $", HotTea.order_cost)
    elif additional_choice == "No":
      print("Your total after toppings is: $", HotTea.order_cost)
    
  

  def remove_topping(self, topping_name, drink_name):
    if drink_name in HotTea.hot_menu_dict:
      if topping_name in (HotTea.hot_menu_dict[drink_name]) and topping_name in HotTea.topping_list:
        print("You are choosing to remove", topping_name, "from", drink_name)
        minus_topping = input("Would you like to remove this topping from the drink? [Yes/No]")
        while minus_topping not in ("Yes", "No"):
          minus_topping = input("Would you like to remove this topping from the drink? [Yes/No]")
        if minus_topping == "Yes":
          print("You have removed", topping_name, "from", drink_name)
        elif minus_topping == "No":
          print(topping_name, "will not be removed from", drink_name)
      elif topping_name not in HotTea.topping_list[drink_name]:
        print(topping_name, "is not on", drink_name)


  def __str__(self):
    return f"{self.__topping_name} is removed from or added to {self.__drink_name} after filtering through {HotTea.hot_menu_dict} and {HotTea.topping_list}"
