# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 10:13:47 2018

@author: Marco Hassan
"""

###############################
# Homework 6
# Name: Marco Hassan
# Student ID: 981745755
###############################


#########################################
# Question 1 - do not delete this comment
#########################################

def mult(x,y):
    if y == 1:
        return x
    return x + mult(x,y-1)

## TEST
##mult(4,5)

#########################################
# Question 2 - do not delete this comment
#########################################
 
def rec_sum(a_1,d,n) :
    if n == 1:
        return a_1 
    return a_1 + mult(d,n-1) + rec_sum(a_1,d,n-1)
    
## TEST
## rec_sum(2,2,4)


#########################################
# Question 3 - do not delete this comment
#########################################

def find_max_modulo(numbers,m):
        
    if len(numbers) == 1:
        if numbers[0]%m==0:
            return numbers[0]
        else:
            return -1
    
    if len(numbers) == 0:
        return -1
           
    if numbers[0]%m==0:
        if numbers[0] > find_max_modulo(numbers[1:], m):
            return numbers[0]
        else:
            return find_max_modulo(numbers[1:], m)
    
    else:
        return find_max_modulo(numbers[1:], m)

 
## TEST    
#print(find_max_modulo([9, 20, 10], 2)) 
#print(find_max_modulo([17, 7, 2, 3, 14], 7))
#print(find_max_modulo([9, 18, 2, 3], 7))
#print(find_max_modulo([], 1))






    
    
    
    
    
    
    