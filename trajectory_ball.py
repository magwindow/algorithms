import matplotlib.pyplot as plt

def ball_trajectory(x):
    """Функция вычисления траектории мяча"""
    location = 10*x - 5*(x**2)
    return location

# Построение траектории гипотетического мяча между моментом броска (x = 0)
# и его соприкосновением с землей (x = 2)
xs = [x/100 for x in list(range(201))]
ys = [ball_trajectory(x) for x in xs]
plt.plot(xs, ys)
plt.title('Траектория брошенного мяча')
plt.xlabel('Горизонтальная позиция мяча')
plt.ylabel('Вертикальная позиция мяча')
plt.axhline(y = 0)
plt.show()

# Траектория гипотетического брошенного мяча с отрезками,
# представляющими линии видимости мяча
xs2 = [0.1,2]
ys2 = [ball_trajectory(0.1),0]
xs3 = [0.2,2]
ys3 = [ball_trajectory(0.2),0]
xs4 = [0.3,2]
ys4 = [ball_trajectory(0.3),0]
plt.title('Траектория брошенного мяча - с линиями видимости')
plt.xlabel('Горизонтальная позиция мяча')
plt.ylabel('Вертикальная позиция мяча')
plt.plot(xs,ys,xs2,ys2,xs3,ys3,xs4,ys4)
plt.show()

# Траектория гипотетического брошенного мяча с отрезками,
# представляющими линии видимости мяча, и отрезками A и B,
# отношение длин которых дает интересующий нас тангенс
xs5 = [0.3,0.3]
ys5 = [0,ball_trajectory(0.3)]
xs6 = [0.3,2]
ys6 = [0,0]
plt.title('Траектория брошенного мяча - вычисление тангенса')
plt.xlabel('Горизонтальная позиция мяча')
plt.ylabel('Вертикальная позиция мяча')
plt.plot(xs,ys,xs4,ys4,xs5,ys5,xs6,ys6)
plt.text(0.31,ball_trajectory(0.3)/2,'A',fontsize = 16)
plt.text((0.3 + 2)/2,0.05,'B',fontsize = 16)
plt.show()