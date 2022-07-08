import matplotlib.pyplot as plt

x = []
y = []
z = []
for i in range(10):
	x.append(i)
	y.append(i*i)
	z.append(i**3)
plt.plot(x, y)
plt.plot(x, z)
plt.show()
print("cubic commit")
b = 0
a = 0
