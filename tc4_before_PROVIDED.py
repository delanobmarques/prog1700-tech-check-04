############################################
# Tech Check 4 - Provided Starter File
############################################

#FUNCTION
def main():

    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.\n")

    numericGrade = 0.0

    #Gather user inputs
    letterGrade = input("Please enter a letter grade : ").upper()
    modifier = input("Please enter a modifier (+, - or nothing) : ")
    isValidLetterGrade = True
    isValidModifier = True

    # Determine base numeric value of the grade
    if letterGrade == "A":
        numericGrade = 4.0
    elif letterGrade == "B":
        numericGrade = 3.0
    elif letterGrade == "C":
        numericGrade = 2.0
    elif letterGrade == "D":
        numericGrade = 1.0
    elif letterGrade == "F":
        numericGrade = 0.0
    else:
        #If an invalid letter is entered
        print("You entered an invalid letter grade.")
        isValidLetterGrade = False
    
    # Determine whether to apply a modifier
    if modifier == "+":
        if letterGrade != "A" and letterGrade != "F": # Plus is not valid on A or F
            numericGrade += 0.3
    elif modifier == "-":
        if letterGrade != "F":     # Minus is not valid on F
            numericGrade -= 0.3
    elif modifier != "":
        #If an invalid modifier is entered
        print("You entered an invalid modifier.")
        isValidModifier = False

    # Output final message and result, with formatting
    if isValidModifier and isValidLetterGrade:
        print("The numeric value is: {0:.1f}".format(numericGrade))

#PROGRAM STARTS HERE
if __name__ == "__main__":
    main()