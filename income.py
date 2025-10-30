import math
import matplotlib.pyplot as plt

def income(edu_yrs):
    return math.sin((edu_yrs - 10.6) * (2 * math.pi/4)) + (edu_yrs - 11) / 2 


# Отношения между продолжительностью образования
# и пожизненным доходом
xs = [11 + x/100 for x in list(range(901))]
ys = [income(x) for x in xs]
plt.plot(xs,ys)

current_edu = 12.5

plt.plot(current_edu,income(current_edu),'ro')
plt.title('Образование и доход')
plt.xlabel('Продолжительность образования (в годах)')
plt.ylabel('Пожизненный доход')
# plt.show()

def income_derivative(edu_yrs):
    return math.cos((edu_yrs - 10.6) * (2 * math.pi/4)) + 1/2

threshold = 0.0001
maximum_iterations = 100000
current_education = 12.5
step_size = 0.001

keep_going = True
iterations = 0

while keep_going:
    education_change = step_size * income_derivative(current_education)
    current_education = current_education + education_change
    
    if abs(education_change) < threshold:
        keep_going = False
    
    if iterations >= maximum_iterations:
        keep_going = False
    
    iterations = iterations + 1

print(current_education)
print(income(current_education))