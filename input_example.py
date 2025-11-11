# # TODO: Exceptions (Advanced)
# # TODO: Pace/Speed (Advanced) -> Homework
# # TODO: Algorithm for making numbers equal -> if user puts a large number find a solution to make it quicker than subtracting/adding one number
# # TODO: tip: - u can add/substract larger number than 1 or use different operations, division/multiplication etc.
# # TODO:
#
# nameVar = input("Give me a number\n")
#
# while type(nameVar) != int:
#     try:
#         nameVar = int(input("Give me a number\n"))
#     except:
#         print("That's not a number")


# file = "names.txt"
#
# with open(file, 'r') as text:
#     for line in text:
#         name_table = line.lower().split(';')
#
# with open("split_names.txt", 'w') as text:
#     for name in name_table:
#         text.write(name + '\n')
#
# look_names = ["Liam Hall", "Mia King", "Noah Scott", "Olivia Bell"]
#
# for name in look_names:
#     if name.lower() in name_table:
#         print(name)

# from pyautogui import *
# import pyautogui as p
# from time import sleep
#
# sleep(5)
# for i in range(1, 101):
#     typewrite(f"I love you {i}%\n")
#     p.press('enter')
#     #sleep(2)

# from pyautogui import typewrite
# from time import sleep
#
# file = "beeMovie.txt"
#
# sleep(10)
# with open(file, 'r') as text:
#     for line in text:
#         typewrite(line)

#TODO: Projects/Homework
#TODO: Usefull libraries -> random, math, time, qrcode
#TODO: 1. Geussing game - numbers
#TODO: 2. Guessing game - list/table with predefined words
#TODO: 3. BMI calculator
#TODO: 4. ATM (100 - 1 x 100 2 x 50 5 x 20) etc.
#TODO: 5. Password generator
#TODO: 6. TODO list
#TODO: 7. Palindrome checker
#TODO: 8. simple mail service (message with values given by user) e.g.( Hi (input_name), we are happy to welcome you in company. We are proud you applied for (name_of_job_like_chef_or_cashier)
#TODO: 9. simple calculator
#TODO: 10. simple shop simulator (you can pick items and it shows you how sum of money)
#TODO: 11. Click start click stop - and it measures time
#TODO: 12. Sorting algorithm for files (images, music, videos, etc.)
#TODO: 13. QR code generator