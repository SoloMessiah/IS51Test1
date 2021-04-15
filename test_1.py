"""

Our program will figure out which payment option, in terms of dollars, will give us the most return.
The first option, is getting paid 100 dollars per day, for ten days.
The second option is getting paid one dollar the first day, but doubling the amount for a total of 10 days.
We will use funtions, named funtion1 and function2 respectively, to calculate the total amount for each option.

The first function, function1 will give us $100 * 10 days.
The second function, function2 will use a loop that occurs 10 times, with the amount being doubled per loop, and finally getting the sum of the 10 loops.

If the first option is better, the program will output to the user "Option 1 is better."
If the second option is better, the program will output to the user "Option 2 is better."
If both option one and option two are equal, the program will output to the user "Option 1 and Option 2 pays the same."

"""


"""

# option1

    return 100 * 10

# option2

    totalMoney = 1
    list1 = []

    loop 10 times
        Add totalMoney to list1
        totalMoney *= 2
    
    sum = sum of list
    return sum

# main

    money1 = option1
    money2 = option2

    if money1 > money2
        "Option 1 is better."
    if money1 == money2
        "Option 1 and Option 2 pays the same."
    else
        "Option 2 is better."

main

"""


def option1():

    return 100 * 10


def option2():

    totalMoney = 1
    list1 = []

    for i in range(0, 10):
        list1.append(totalMoney)
        totalMoney *= 2

    # print(list1)

    totalPay = sum(list1)
    return totalPay


def main():

    results = ""
    money1 = option1()
    money2 = option2()

    if money1 > money2:
        results = "Option 1 is better."
    if money1 == money2:
        results = "Option 1 and Option 2 pays the same."
    else:
        results = "Option 2 is better."

    print(results)


main()
