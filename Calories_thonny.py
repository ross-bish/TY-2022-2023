#The following programme calculates the total calories from your total macros

protein = input("Enter your daily Protein intake in grams: ")
carbs = input("Enter your daily Carbs intake in grams: ")
fats = input("Enter your daily Fat intake in grams: ")

total_cals = int(protein) * 4 + int(carbs) * 4 + int(fats) * 9

print("\nYour total daily calories are ", total_cals, "kcals")