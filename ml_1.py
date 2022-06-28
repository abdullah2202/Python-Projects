import numpy
import matplotlib.pyplot as plt

num = 2000

x = numpy.random.normal(5.0, 3.0, num)
y = numpy.random.normal(5.0, 0.5, num)
s = numpy.random.uniform(10.0, 50.0, num)

plt.scatter(x, y, s=s, alpha = 0.5)
plt.show()
