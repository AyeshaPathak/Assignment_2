'''
File: bubble_tea.py
Description: This module contains the abstract class BubbleTea and its abstract methods.
Author: Ayesha Pathak
ID: 1104095812
Username: patay096
This is my own work as defined by the University's Academic Misconduct Policy.
'''

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