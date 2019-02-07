###########################################
##Homework_1; Marco Hassan; ID: 981745755##
###########################################

#Exercise 1

question = input("Three numbers separated by a comma ',' \n")

a,b,c = question.split(',')

average = (float(a)+float(b)+float(c))/3

print("The average of your input numbers is ", average)

#Exercise 2

question = input("Enter three numbers separated by a comma representing: \nThe first term \nThe common fraction \nThe number of terms in the series \n")

a, r, n =  question.split(',')

a = float(a)
r = float(r)
n = float(n)



last_num = a*((1-r**n)/(1-r))

n = str(n)

print("The", n + "'th nuber in the series is", last_num)

#Exercise 3

question =input("The length of one side of the rectangular and the length of its diagonal sparated by a a commma \n")

side_1, diagonal = question.split(',')

side_2 = (float(diagonal)**2 - float(side_1)**2)**0.5

area = float(side_1) * side_2

perimeter = 2*(float(side_1)+side_2)

print("The Area is", area)

print("The Perimeter is", perimeter)

print("The other side is", side_2)

# Exercise 4

request = input("Insert a string with 20 characters \n")

print(str.upper(request[0:2])+request[-5:1:-1]+str.lower(request[-4:]))
