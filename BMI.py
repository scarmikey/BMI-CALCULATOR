def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("Welcome to the BMI Calculator!")
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
    except ValueError:
        print("Error: Please enter valid numerical values for weight and height.")
        return

    if weight <= 0 or height <= 0:
        print("Error: Weight and height must be positive numbers.")
        return

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print("BMI: {:.2f}".format(bmi))
    print("Category:", category)


if __name__ == "__main__":
    main()
