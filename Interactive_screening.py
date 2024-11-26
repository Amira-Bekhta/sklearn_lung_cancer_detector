import joblib 

model = joblib.load("lung_cancer_detector.joblib") # Load the model

print("Welcome to this interactive screening, please note that this only serves as a general screening and does not replace proffessional diagnosis")

gender = input("Choose your gender, please use 'M' for male and 'F' for female: ")
gender = 1 if gender == 'M' else 0 # Convert the gender to the corresponding number
age = int(input("Enter your age: "))
print("For the next questions please type '0' for NO and '1' for yes")
smoking = input("Do you smoke: ")
yellow_fings = input("Do you have yellow fingers: ")
anxiety = input("Are you experiencing anxiety: ")
peer_pressure = input("Any peer pressure: ")
chronic = input("Do you suffer from any chronic disease: ")
fatigue = input("Any fatigue: ")
allergy = input("Do you have any allergies: ")
wheezing = input("Any wheezing: ")
alcohol = input("Do you consume alcohol: ")
coughing = input("Are you experiencing a lot of coughing: ")
shortness = input("Do you have shortness of breath: ")
swallowing = input("Do you have swallowing diffuculty: ")
chest_pain = input("Do you feel chest pain: ")

symptoms = [gender, age, smoking, yellow_fings, anxiety, peer_pressure, chronic, fatigue, allergy, 
            wheezing, alcohol, coughing, shortness, swallowing, chest_pain]

prediction = model.predict([symptoms])

if(prediction == 1):
    print("You have a high chance of suffering from lung cancer, please consult a doctor to have an accurate diagnosis")
else:
    print("You have a low chance of suffering from lung cancer")