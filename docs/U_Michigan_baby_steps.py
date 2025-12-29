#01. Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 
#You should use input to read a string and float() to convert the string to a number. 
#Do not worry about error checking or bad user data.

# Horas input string e conversao a numero
hrs = input ("Enter Hours:")
hrs = float(hrs)


# rate input string e conversao a numero
rate = input ("Enter rate:")
rate = float(rate)

pay = hrs * rate

print ("Pay:" , pay)

-----------------------------------------------------------------------------------------

#02. Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. 
#Do not worry about error checking the user input - assume the user types numbers properly. 

# Horas input string e conversao a numero
hrs = input ("Enter Hours:")
hrs = float(hrs)

# rate input string e conversao a numero
rate = input ("Enter rate:")
rate = float(rate)

# logica de pagamento
if hrs <= 40 :
    pay = hrs * rate
    print("Pay" , pay)
else :
    pay = 40 * rate
    tax = (hrs - 40) * (rate * 1.5)
    extrapay = pay + tax
    print("Pay" , extrapay)
print("Thank you")


-------------------------------------------------------------------------------------------------------

#3.Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85. 

score = input("Enter Score: ")


try:
    rate = float(score)
    except:
    print ("Invalid input")

if rate < 0.0 :
    print ("Out of range")    
elif rate > 1.0 :
    print ("Out of range") 
elif rate >= 0.9 :
    print ("A")
elif rate >= 0.8 :
    print ("B")
elif rate >= 0.7 :
    print ("C")
elif rate >= 0.6 :
    print ("D")
elif rate < 0.6 :
    print ("F")

---------------------------------------------------------------------------------------------------------------------------------
