from pywebio.input import input,FLOAT
from pywebio.output import put_text

def bmi():
	height=input("Input your height(cm):",type=FLOAT)
	weight=input("Input your weight(cm):",type=FLOAT)

	BMI = weight / (height/100)** 2

	top_status =[(16,'Severly underweight'),(18.5,'underweight'),(25,'normal'),(30,'Overweight'),(35,'moderately obese'),(float('inf') ,'Severly obese'),]

	for top, status in top_status:
		if BMI <= top:
			put_text('Your BMI : %.1f. Category:%s' % (BMI,status))
			break

if __name__ == '__main__':
	bmi()