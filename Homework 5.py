# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 09:37:20 2018

@author: Marco Hassan
"""
###############################
# Homework 5
# Name: Marco Hassan
# Student ID: 981745755
###############################


#########################################
# Question 1 - do not delete this comment
#########################################
def most_popular_character(my_string):
    char_freq = dict()
    for char in my_string:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    max_appearance = []
    for item in char_freq.items():
        if item[1] == max(char_freq.values()):
            max_appearance.append(item[0])

    if len(max_appearance) == 1:
        print(max_appearance[0])
        
    else:
        dict_ASCII = dict()
        for i in max_appearance:
            dict_ASCII[i] = ord(str(i))
        for item in dict_ASCII.items():
            if item[1] == min(dict_ASCII.values()):
                print(item[0])


#########################################
# Question 2 - do not delete this comment
#########################################
def sum_sparse_matrices(lst):
    dict_keys = dict()
    for dictionary in lst:
        for keys in dictionary:
            dict_keys[keys] =  dictionary.get(keys) + dict_keys.get(keys, 0)
    non_zero_entries = []
    for item in dict_keys.items():
        if item[1] != 0:
            non_zero_entries.append(item)
    return dict(non_zero_entries)
       

#########################################
# Question 3 - do not delete this comment
#########################################
#section a
def courses_per_student(tuples_lst):
    dict_names = dict()
    for tuples in tuples_lst:
        if tuples[0] in dict_names:
            dict_names[tuples[0]] = str(dict_names.get(tuples[0]) + " " + str(tuples[1])).lower() 
        if tuples[0] not in dict_names:
            dict_names[tuples[0]] = tuples[1]
        
    dict_final = dict()  
    for item in dict_names.items():
        dict_final[item[0].lower()] = item[1].split( )
            
    return(dict_final)


#section b
def hours_per_student(student_course, course_hours):
    dict_hours = dict()
    for person in student_course:
        dict_hours[person] = 0
        
    for person in student_course:
        subjects = student_course.get(person)
        
        for subject in subjects:
            dict_hours[person] += course_hours[subject]
    return(dict_hours)


#########################################
# Question 4 - do not delete this comment
#########################################
#section 1
def map_keys_to_values_list(k_lst, v_lst):
    dict_map = dict()
    for i in range(0, len(k_lst)):
        if k_lst[i] not in dict_map:
            dict_map[k_lst[i]] = str(v_lst[i])
        else:
            dict_map[k_lst[i]] = dict_map.get(k_lst[i]) + " " + str(v_lst[i])
    
    dict_final2 = dict()  
    for item in dict_map.items():
        dict_final2[item[0].lower()] = item[1].split( )
    
    return(dict_final2)

        
#section 2
def popular_in_list(lst, k):
    dict_occurrences = dict()
    for i in lst:
        dict_occurrences[i] = dict_occurrences.get(i, 0) + 1
    
    higher_than_threshold = []
    for item in dict_occurrences.items():
        if item[1] >= k:
            higher_than_threshold.append(item[0])
    
    return(higher_than_threshold)

#section 3
def map_keys_to_values_by_popularity(k_lst, v_lst, k):
    map_key = map_keys_to_values_list(k_lst, v_lst)
    dict_popular = dict()
    for item in map_key.items():
        dict_popular[item[0]] = popular_in_list(item[1],k)
    
    non_zero_entries = []
    for item in dict_popular.items():
        if len(item[1]) != 0:
            non_zero_entries.append(item)
    return dict(non_zero_entries)



    
#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
