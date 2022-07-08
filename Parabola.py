import matplotlib.pyplot as plt

x = []
y = []
for i in range(10):
	x.append(i)
	y.append(i*i)
plt.plot(x, y)
plt.show()
