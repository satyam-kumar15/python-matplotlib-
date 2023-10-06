import matplotlib.pyplot as plt
import numpy as np

# Creating Data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Line Plot
plt.figure(figsize=(8, 4))
plt.plot(x, y, label='sin(x)', color='blue', linewidth=2)
plt.title('Line Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Scatter Plot
plt.figure(figsize=(8, 4))
plt.scatter(x, y, label='sin(x)', color='red')
plt.title('Scatter Plot')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

# Bar Plot
categories = ['A', 'B', 'C', 'D']
values = [3, 7, 9, 5]

plt.figure(figsize=(8, 4))
plt.bar(categories, values, color='green')
plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid(axis='y')
plt.show()

# Histogram
data = np.random.normal(0, 1, 1000)

plt.figure(figsize=(8, 4))
plt.hist(data, bins=30, color='purple', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()

# Box Plot
data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(0, 2, 100)
data3 = np.random.normal(0, 1.5, 100)

plt.figure(figsize=(8, 4))
plt.boxplot([data1, data2, data3], labels=['Data 1', 'Data 2', 'Data 3'])
plt.title('Box Plot')
plt.ylabel('Value')
plt.grid(True)
plt.show()

# Pie Chart
sizes = [20, 30, 50]
labels = ['A', 'B', 'C']

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['blue', 'red', 'green'])
plt.title('Pie Chart')
plt.show()

# Subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plot 1
axes[0, 0].plot(x, y, color='blue')
axes[0, 0].set_title('Plot 1')

# Plot 2
axes[0, 1].scatter(x, y, color='red')
axes[0, 1].set_title('Plot 2')

# Plot 3
axes[1, 0].hist(data, bins=30, color='purple', alpha=0.7)
axes[1, 0].set_title('Plot 3')

# Plot 4
axes[1, 1].bar(categories, values, color='green')
axes[1, 1].set_title('Plot 4')

plt.tight_layout()
plt.show()
