#lambda 

# # also known as anonymous function (function has no name)

# # use ful when we need a fhort , throwaway function
# # something simple that we only use once





# #by general function call

# # def sort_by_age(students):
# #  return students[2]

# #  students_tuples = [
# #        ('john', 'a',14),
# #        ('jane','b',12),
# #        ('dave','b',10),
# #        ]

# #   sorted(student_tuples, key=sort_by_age) #sort by age
 

# #   #by lambda function call

# #   students_tuples = [
# #        ('john', 'a',14),
# #        ('jane','b',12),
# #        ('dave','b',10),
# #        ]

# #   sorted(student_tuples,key=lambda student: student[2])

# #  standard function

# #  def add_interest(amount, interest=5):
# #     returen amount*(1+interest/100)
# # add_interest(100)


# # lambda function

# # add_interest = lambda amount, interest=5: amount*(1+interest/100) #definition
# # add_interest(100)


# amounts = [100, 200, 300 ,500, 800]
# add_interest = lambda amount, interest=5:amount*(1+interest/100)#definition
# for amount in amounts:
#   print(add_interest(amount))




# amounts = [100, 200, 300 ,500, 800]
# add_interest = lambda amount, interest=5:amount*(1+interest/100)
# after_clac =[]
# for amount in amounts:
#   after_clac.append(add_interest(amount))
#   print(after_clac)




