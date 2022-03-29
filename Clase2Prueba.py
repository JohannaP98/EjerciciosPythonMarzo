num = 30

for i in range (1,num+1):
     if i%3==0 and i%5!=0:
         print(i,"Fizz")
     elif i%5==0 and i%3!=0:
         print(i,"Buzz")
     elif i%3==0 and i%5==0:
         print(i,"FizzBuzz")

# for i in range(1,num+1):
#     if i%3==0 and i%5!=0:
#         print (i,"Fizz")
#     else:
#             if i%5==0 and i%3!=0:
#                 print (i,"Buzz")
#             else:
#                 if i%3==0 and i%5==0:
#                  print (i,"FizzBuzz")
