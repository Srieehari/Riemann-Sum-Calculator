import numpy as np
import math

# Write your function here
def f(x):
    return (1+ math.cos(x))**(1/3)

# Set the interval and number of subintervals
a = 0
b = math.pi/2
n = 4

# Calculate delta x
delta_x = (b - a) / n


x_values = [a + i * delta_x for i in range(n + 1)]
f_values = [f(x) for x in x_values]

# Trapezoidal Rule formula
Trapezoid_Rule = (delta_x / 2) * (f_values[0] + 2 * sum(f_values[1:-1]) + f_values[-1])


# Midpoint Rule
midpoints = [a + (i + 0.5) * delta_x for i in range(n)]
midpoint_sum = sum(f(x) for x in midpoints)
midpoint_estimate = delta_x * midpoint_sum

# Simpson's Rule
x_values = [a + i * delta_x for i in range(n + 1)]
simpson_sum = (f(x_values[0]) +
               4 * sum(f(x_values[i]) for i in range(1, n, 2)) +
               2 * sum(f(x_values[i]) for i in range(2, n, 2)) +
               f(x_values[n]))

simpson_estimate = (delta_x / 3) * simpson_sum




print("The trapezoid rule sum is :", Trapezoid_Rule)
print("The midpoint estimate is", midpoint_estimate)
print("The simpson estimate is", simpson_estimate)
