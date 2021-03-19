
import json

with open('bmi.json') as f:
  data = json.load(f)

def bmiCalc(data):
    for i in range(len(data)):
        if data[i]['Gender']=='Male' or data[i]['Gender']=='Female' :
            height=float(data[i]['HeightCm'])
            heightMeter=height/100
            weight=data[i]['WeightKg']
            bmi=weight/(heightMeter*heightMeter)
            bmi=round(bmi,2)
            
            if bmi <= 18.4:
                
                bmiCategory='Underweight'
                healthRisk='Malnutrition risk'
                data[i]['bmiCategory']=bmiCategory
                data[i]['healthRisk']=healthRisk

            elif 18.5 < bmi < 24.9:
                
                bmiCategory='Normal weight'
                healthRisk='Low risk'
                data[i]['bmiCategory']=bmiCategory
                data[i]['healthRisk']=healthRisk


            elif 25 < bmi < 29.9:
                
                bmiCategory='Over weight'
                healthRisk='Enhanced risk'
                data[i]['bmiCategory']=bmiCategory
                data[i]['healthRisk']=healthRisk

            elif 30 < bmi < 34.9:
                
                bmiCategory='Moderately obese'
                healthRisk='Medium risk'
                data[i]['bmiCategory']=bmiCategory
                data[i]['healthRisk']=healthRisk

            elif 35 < bmi < 39.9:
                
                bmiCategory='Severely obese' 
                healthRisk='High risk'
                data[i]['bmiCategory']=bmiCategory
                data[i]['healthRisk']=healthRisk

            elif 35 < bmi < 39.9:
                
                bmiCategory='Very severely obese'   
                healthRisk='Very high risk'  
                data[i]['bmiCategory']=bmiCategory
                data[i]['healthRisk']=healthRisk





bmiCalc(data)
print (data)
with open('appendedBMI.json', 'w') as outfile:
    json.dump(data, outfile)

#print(data)