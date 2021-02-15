import matplotlib.pyplot as plt


def my_func(x, a, b, c, d):
    return (a*x**2 + b*x + c) / (x + d)


styles = plt.style.available
plt.style.use(styles[2])

a = 5; b = 2; c = 5; d = -1
legend = 'y = {}*x**2 + {}*x + {}'.format(a, b, c)

left = -20; right = 20; step = 1
data_x = []; data_y = []
pos_x = left
while pos_x <= right:
    try:
        pos_y = my_func(pos_x, a, b, c, d)
        data_x.append(pos_x)
        data_y.append(pos_y)
    except:
        pass
    pos_x += step
plt.plot(data_x, data_y, linewidth = 2, color='#ba55d3')

plt.title("График функции")
plt.xlabel("Ось Y")
plt.ylabel("Ось X")
plt.legend([legend])
plt.grid(True)
plt.axhline(linewidth = 2, color ='#6e7f80')
plt.axvline(linewidth = 2, color ='#6e7f80')

plt.show()
