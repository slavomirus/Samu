# TODO: Exceptions (Advanced)
# TODO: Pace/Speed (Advanced) -> Homework
# TODO: Algorithm for making numbers equal -> if user puts a large number find a solution to make it quicker than subtracting/adding one number
# TODO: tip: - u can add/substract larger number than 1 or use different operations, division/multiplication etc.
# TODO:

nameVar = input("Give me a number\n")

while type(nameVar) != int:
    try:
        nameVar = int(input("Give me a number\n"))
    except:
        print("That's not a number")