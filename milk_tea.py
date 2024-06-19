'''
File: milk_tea.py
Description: This module contains the polymorphic class MilkTea and its methods for adding and removing toppings.
Author: Ayesha Pathak
ID: 1104095812
Username: patay096
This is my own work as defined by the University's Academic Misconduct Policy.
'''


from bubble_tea import BubbleTea


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
  store_earning = 0


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
      print("Your total after toppings is: $", MilkTea.order_cost)
    elif additional_choice == "No":
      print("Your total after toppings is: $", MilkTea.order_cost)



  def remove_topping(self, topping_name, drink_name):
    if drink_name in MilkTea.milk_menu_dict: 
      if topping_name in (MilkTea.milk_menu_dict[drink_name]) and topping_name in MilkTea.topping_list:
        print("You are choosing to remove", topping_name, "from", drink_name)
        minus_topping = input("Would you like to remove this topping from the drink? [Yes/No]")
        while minus_topping not in ("Yes", "No"):
          minus_topping = input("Would you like to remove this topping from the drink? [Yes/No]")
        if minus_topping == "Yes":
          print("You have removed", topping_name, "from", drink_name)
        elif minus_topping == "No":
          print(topping_name, "will not be removed from", drink_name)
      elif topping_name not in MilkTea.topping_list[drink_name]:
        print(topping_name, "is not on", drink_name)
          
      
  def __str__(self):
    return f"{self.__topping_name} is removed from or added to {self.__drink_name} after filtering through {MilkTea.milk_menu_dict} and {MilkTea.topping_list}"
