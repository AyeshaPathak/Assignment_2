'''
File: store.py
Description: This module contains the testing done on various methods from various classes from other modules.
Author: Ayesha Pathak
ID: 1104095812
Username: patay096
This is my own work as defined by the University's Academic Misconduct Policy.
'''

import pytest
from bubble_tea import BubbleTea
from milk_tea import MilkTea 
from fruit_tea import FruitTea
from hot_tea import HotTea 
from sparkling_tea import SparklingTea
from frozen_tea import FrozenTea


class TestMilkOrder:
    @pytest.fixture
    def test_milk_order(self, drink_name, size, ice_level, sugar_level, tea_type):
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
      assert drink_name.sugar_level in ("Low", "Medium", "Large")

      if tea_type in (MilkTea.milk_menu_dict[drink_name]):
        print("This drink contains", tea_type)
      elif tea_type not in (MilkTea.milk_menu_dict[drink_name]):
        print("This drink does not contain", tea_type)
