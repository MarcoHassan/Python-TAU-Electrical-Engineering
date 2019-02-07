# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 10:14:15 2018

@author: Marco Hassan
"""
#########################################
# Marco Hassan
# 981745755
#########################################

#########################################
# Question 1 - do not delete this comment
#########################################
def to_str(b):
    if b == True:
        return "ball"
    else:
        return "regular"


class Pen:
    def __init__(self, company, diameter, inkLevel, price, isBallString):
        self.company = company
        self.diameter = float(diameter)
        self.inkLevel = float(inkLevel) # I assume as stated that the input is correct at no 0-10 limit implementation is necessary.
        self.price = float(price)
        if isBallString == "ball":
            self.isBallString = True
        else:
            self.isBallString = False

    def get_remaining_hours(self):
        if self.isBallString == True:
            return self.inkLevel / 1.25 * self.diameter
        else:
            return self.inkLevel / 2.5 * self.diameter

    def __repr__(self):
        return "|Company: " + self.company + ", Diameter: " + str(self.diameter) \
            + ", InkLevel: " + str(self.inkLevel) + ", Price:" + str(self.price) \
            + ", " + to_str(self.isBallString) + " pen|"

    def get_copy(self):
        return Pen(self.company, self.diameter, self.inkLevel, self.price, self.isBallString) 

    def __gt__(self, other):
        if self.price == other.price:
                return self.get_remaining_hours() > other.get_remaining_hours()
        else:
            return self.price > other.price

    def get_color(self):
        return "blue" 

#########################################
# Question 2 - do not delete this comment
#########################################
class Marker:
    def __init__(self, company, color, paintLevel, price):
        self.company = company
        self.color = color
        if paintLevel > 15 or paintLevel < 0:
            raise ValueError("The paint level is defined on a 0 to 15 interval")
        else:
            self.paintLevel = float(paintLevel)
        self.price = float(price)

    def __repr__(self):
        return "|Company: " + self.company + ", Color: " + str(self.color) \
            + ", PaintLevel: " + str(self.paintLevel) + ", Price: " + str(self.price) \
            + "|"

    def get_remaining_hours(self):
        return self.paintLevel/2

    # to avoid a problem of adding an object to itself, can use this
    def get_copy(self):
        return Marker(self.company, self.color, self.paintLevel, self.price)

    def get_color(self):
        return self.color


#########################################
# Questions 3 - do not delete this comment
#########################################

def sort_func(item):
    return item.company
                
class PencilCase:
    def __init__(self, stationary):
        self.stationary = stationary
        
    def add(self, item):
        self.stationary.append(item.get_copy())

    def get_stationary(self):
            return self.stationary ### this is very possibly wrong as self.stationary can be called straight without the function

    def __repr__(self):
        
        def print_stionary_sort():
            self.stationary.sort(key = sort_func)
            help = ""
            for i in self.get_stationary():
                help = help + str(i) + "\n"
            
        return "PencilCase has " + str(len(self.get_stationary())) + \
            " items. Contents:\n" \
            + help  
       
    def pop(self, hours):
        original = self.get_stationary()[:]
        lst = []
        y = -1
        for i in self.get_stationary():
            y += 1
            if i.get_remaining_hours() >= hours:
                lst.append([i.price, y])
            print(lst)
        
        if len(lst) == 0:
            print("No appropriate writing tool found")
            return None
        
        else:
            min_price = float("inf")
            key = -1
            for y in lst:
                if min_price > y[0]:
                    min_price = y[0]
                    key = y[1]
            
            self.get_stationary().remove(self.get_stationary()[key])
            return original[key]
        
    def get_colors(self):
        lst = []
        for i in self.get_stationary():
            lst.append(i.get_color())
        return lst

    def get_pens_for_test(self):
        pens = []
        for i in self.stationary:
            if type(i) == Pen:
                pens.append(i.get_copy())
        
        def price_key(item):
            return item.price
        pens.sort(key = price_key, reverse = True)
        
        selectedPens = []
        remainingHours = 0
        
        for j in range(0,len(pens)+1):
            if remainingHours > 3:
                return selectedPens
    
            elif j == len(pens):
                print("Need to buy pens, or load ink")
                return None
    
            else:
                remainingHours += pens[j].get_remaining_hours()*2
                selectedPens.append(pens[j])

