# Lab 01 Exercise 1: Road Trip Budgeter

def is_budget_sufficient(one_way_km, budget):
    total_distance = one_way_km*2
    fuel = total_distance/10
    cost = fuel*2


    if budget >= cost:
        return print ("True")

    else:
        return print ("False")

is_budget_sufficient(100,40)
is_budget_sufficient(100,39)