import matplotlib.pyplot as plt

# Generate some data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a line plot
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Example Plot')
plt.grid(True)

# Save the plot to a file
plt.savefig('plot.png')
