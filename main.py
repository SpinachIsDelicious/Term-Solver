common_difference = int(input("Common Difference: "))
first_term = int(input("First Term: "))
wanted_term = int(input("Wanted Term: "))

wanted = first_term + (wanted_term - 1) * common_difference

print("Your answer: " + str(wanted))