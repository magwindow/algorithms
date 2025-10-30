import math
import matplotlib.pyplot as plt


def revenue(tax):
    return 100 * (math.log(tax+1) - (tax - 0.2)**2 + 0.04)

# print(revenue(0.2))


xs = [x/1000 for x in range(1001)]
ys = [revenue(x) for x in xs]
plt.plot(xs,ys)
plt.title('Ставка налога и поступления в бюджет')
plt.xlabel('Ставка налога')
plt.ylabel('Поступления')
# plt.show()

# Связь между ставкой налога и поступлениями; 
# точка представляет текущее значение ставки
xs = [x/1000 for x in range(1001)]
ys = [revenue(x) for x in xs]
plt.plot(xs,ys)

current_rate = 0.7

plt.plot(current_rate,revenue(current_rate),'ro')
plt.title('Ставка налога и поступления в бюджет')
plt.xlabel('Ставка налога')
plt.ylabel('Поступления')
# plt.show()

def revenue_derivative(tax):
    """Вычисляет производную по ставке налога"""
    return 100 * (1/(tax + 1) - 2 * (tax - 0.2))

# print(revenue_derivative(0.7))

step_size = 0.001

current_rate = current_rate + step_size * revenue_derivative(current_rate)
# print(current_rate)
current_rate = current_rate + step_size * revenue_derivative(current_rate)
# print(current_rate)

# Реализация градиентного подъема
threshold = 0.0001
maximum_iterations = 100000

keep_going = True
iterations = 0

while keep_going:
    rate_change = step_size * revenue_derivative(current_rate)
    current_rate = current_rate + rate_change
    
    if abs(rate_change) < threshold:
        keep_going = False
    if iterations >= maximum_iterations:
        keep_going = False
    
    iterations = iterations + 1
    
print(current_rate)
print(revenue(current_rate))

