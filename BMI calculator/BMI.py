def calculate_bmi(weight, height):
    # Calculate BMI using the formula: weight(kg) / (height(m)^2)
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_status(bmi):
    # Determine the health status based on the BMI value
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    # Get user input for weight and height
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        # Validate input
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Display the result
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Health status: {get_bmi_status(bmi)}")

    except ValueError:
        print("Invalid input! Please enter numeric values for weight and height.")

if __name__ == "__main__":
    main()
