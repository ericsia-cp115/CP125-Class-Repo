# Lab 01 Exercise 2: Camping Logistics
import math

def calculate_tent_cost(participants, tent_capacity, tent_price):
    total_tents= math.ceil(participants/tent_capacity)
    total_price= total_tents * tent_price
    return print (total_price)

calculate_tent_cost(12,4,100)
calculate_tent_cost(13,4,100)