import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, color='red', marker='o', linestyle='--')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('My Plot')
plt.legend(['Line'])
plt.grid(True)
plt.show()

