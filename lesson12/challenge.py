def calculate_bmi(weight, height):

    bmi = weight / (height ** 2)
    return bmi


def categorize_bmi(bmi):

    if bmi < 18.5:
        return "Nder peshe"
    elif 18.5 <= bmi < 24.9:
        return "Peshe normale"
    elif 24.9 <= bmi < 29.9:
        return "Mbi peshe"
    else:
        return "Obese"


def bmi_challenge():
    print("Mire se erdhet ne BMI challenge:")

    try:

        weight = float(input("Shkruaj sa kilogram ke tani per momentin: "))
        height = float(input("Shkruaj gjatesine tuaj ne meter: "))


        bmi = calculate_bmi(weight, height)


        category = categorize_bmi(bmi)


        print(f"Your BMI is {bmi:.2f}, which is considered '{category}'.")

    except ValueError:
        print("Please enter valid numerical values for weight and height.")

    except Exception as e:
        print(f"An error occurred: {e}")



bmi_challenge()
