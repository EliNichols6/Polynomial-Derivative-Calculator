print("This calculator takes the derivative of a polynomial function.")
print("The coefficients and powers must be whole numbers, and the powers must be greater than 1 or less than 0.")
print("Note: The derivative of something to the first power is just the coefficient.")
print("")
terms = int(input("How many terms are in your polynomial? "))
if terms > 20:
    print(
        "This calculator can only determine the derivative of polynomials limited to 20 terms. Please restart.")
    exit()

variable = str(input("What is the variable letter in your polynomial? "))
coefficients = []
powers = []
final_coefficients = []
final_powers = []


def terms_input():
    i = 1
    while i <= terms:
        if i == 1:
            after = "st "
        elif i == 2:
            after = "nd "
        elif i == 3:
            after = "rd "
        else:
            after = "th "
        i = str(i)
        n_coefficient = input("Enter your " + i + after + "term's coefficient")
        n_power = input("Enter your " + i + after + "term's power")
        coefficients.append(n_coefficient)
        powers.append(n_power)
        i = int(i)
        i += 1


terms_input()


def der_powers_and_coefficients():
    i = 0
    while i < len(powers):
        if int(powers[i]) > 1:
            n_power = int(int(powers[i]) - 1)
            n_coefficient = int(int(powers[i]) * int(coefficients[i]))
            final_powers.append(n_power)
            final_coefficients.append(n_coefficient)

        elif int(powers[i]) < 0:
            n_power = int(int(powers[i]) - 1)
            n_power = n_power * -1
            n_coefficient = int(int(powers[i]) * int(coefficients[i]))
            final_powers.append(n_power)
            final_coefficients.append(n_coefficient)

        else:
            final_powers.append(0)
            final_coefficients.append(int(coefficients[i]))

        i += 1


der_powers_and_coefficients()


def display():
    print("The derivative of the terms you inputted is:")
    i = 0
    while i < len(powers):
        print(str(final_coefficients[i]) + variable + "^" + str(final_powers[i]) + " +")
        i += 1


display()
