#date: 11/29/2024
#author: keshithecoder
'''purpose: a script which can calculate simple statistical measures for simple data sets; 
            script allows using unlimited number of data points.'''


#pseudocode : get data to an array
#             ask for the statistical measure user need to calculate
#             calculate the measure using the appropriate formula
#             display the result

import math
import statistics


def welcome_banner(size):




    # Letter S
    pattern1 = []
    for i in range(size * 2 - 1):  # Total rows for the "S" pattern
        if i == 0 or i == size - 1 or i == size * 2 - 2:
            pattern1.append ("S" * size )  # Top, middle, and bottom rows
        elif i < size - 1:
            pattern1.append("S" )  # Left side of "S" for the top curve
        else:
            pattern1.append(" " * (size - 1) + "S")  # Right side of "S" for the bottom curve

    # Letter T
    pattern2 = []
    for j in range(size * 2 - 1):
        if j == 0:
            pattern2.append("T" * size)  # Top of "T"
        else:
            pattern2.append(" " * ((size - 1) // 2) + "T")  # Vertical line of "T"

    # Letter A
    pattern3 = []
    for k in range(size * 2 - 1):
        if k == (size * 2 - 2) // 2:
            pattern3.append("A" * size)  # Middle line of "A"
        elif k == 0:
            pattern3.append(" " * (size // 2) + "A" + " " * (size // 2))
        else:
            pattern3.append("A" + " " * (size - 2) + "A")  # Other rows of "A"

    # Letter C
    pattern5 = []
    for l in range(size * 2 - 1):
        if l == 0 or l == size * 2 - 2:
            pattern5.append("C" * size)  # Top and bottom rows of "C"
        else:
            pattern5.append("C")  # Vertical line of "C"

    # Letter L
    pattern7 = []
    for m in range(size * 2 - 1):
        if m == size * 2 - 2:
            pattern7.append("L" * size)  # Bottom row of "L"
        else:
            pattern7.append("L")  # Vertical line of "L"

    
    for row in range(size * 2 - 1):
        print(
            f"{pattern1[row]:<{size}}  {pattern2[row]:<{size}}  {pattern3[row]:<{size}}  {pattern2[row]:<{size}}  {pattern5[row]:<{size}}  {pattern3[row]:<{size}}  {pattern7[row]:<{size}}"
        )



size = 5
welcome_banner(size)


print("Welocme to statistical calculator!")

dataset = []



while True:
    x = (input("Enter your data set, each data seperated by a comma : "))
    data = [float(i) for i in x.split(",")] 
    dataset.extend(data)
    response = input((str(dataset) + " is the data set you entered. type Y to continue : ")).upper()
    
    if response == "Y":

        mean_ = statistics.mean(dataset)
        median_ = statistics.median(dataset)
        mode_ = statistics.mode(dataset)
        variance_ =statistics.variance(dataset)
        sd = statistics.stdev(dataset)

        print(" Mean : ",mean_)
        print("Median : ", median_)
        print("Mode : ", mode_)
        print("Variance : ", variance_)
        print(" Standard Deviation : ", sd)

        ans = input("Do you wish to calculate for another data set? yes/no  : ").lower()


        if ans == "yes":
            continue

        elif ans == "no":
            print('Thank you for using statistical calculator!')
            break

        else :
            print("Invalid input")

    else :
        dataset.clear()
        print("invalid input")
    



        

