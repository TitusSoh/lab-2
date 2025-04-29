def calbmi(height, weight):
    bmi = weight / (height * height)
    print(f"bmi = {bmi:.2f}")
    return bmi
def classbmi(bmi):
    if(bmi <18.5):
        print("underweight")
    elif(bmi>= 18.5 and bmi <= 25):
        print("normal")
    else: print("overweight")
    return
weighti = float(input("weight pls "))
heighti = float(input("height pls "))
outp = calbmi(heighti, weighti)
classbmi(outp)