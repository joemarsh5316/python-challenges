def largestNumber():
    greatestNum = 0
    num1 = input("What number do you want to have as number ONE")
    num2 = input("What number do you want to have as number TWO ")
    num3 = input("what number do you want to have as number three")
    if num1 > num2:
        greatestNum = num1
    else:
        greatestNum = num2



   if num3 > greatestNum:
        greatestNum = num3
    else:
        greatestNum = greatestNum



   print(greatestNum)



largestNumber()
