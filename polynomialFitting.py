"""
Created on May 2 11:59:06 2023

@author: Bryan Yang
"""

# Optimization 

import pandas as pd

# Need x and y values to plot.
econ = pd.read_csv('ccar.csv')

# Add a column of numbers instead of dates for simplicity.
econ['x'] = pd.Series(range(1, 185))

# Using LBR (Unemployment) because it is fairly smooth. Polynomials don't work
    # as well on jagged series as they need to be extremely long.

    # Code comes from:
        # https://machinelearningmastery.com/curve-fitting-with-python/
        # Thank you Jason Brownlee

from numpy import arange
from scipy.optimize import curve_fit
from matplotlib import pyplot

# Need a function:
    # objective function
def objective(x, a, b):
    return (a * x) + b

# ---- Fit Curve ----
data = econ.values
# Values to be fit
y, x = data[:,6], data[:,18]
# Fit curve
popt, _ = curve_fit(objective, x, y)
# Summarize parameter values
a, b = popt
# Plot Values
pyplot.scatter(x, y)
# Define input range
x_line = arange(min(x), max(x), 1)
# Calculate Y-values for the x-range
y_line = objective(x_line, a, b)
# Create Plots
pyplot.plot(x_line, y_line, '--', color='red')
pyplot.show()

def objective(x, a, b, c):
    return (a * x) + (b * x**2) + c

# ---- Fit Curve ----
data = econ.values
# Values to be fit
y, x = data[:,6], data[:,18]
# Fit Curve
popt, _ = curve_fit(objective, x, y)
# Summarize parameter Values
a, b, c = popt
# Plot Values
pyplot.scatter(x, y)
# Define input range
x_line = arange(min(x), max(x), 1)
# Calculate Y-values for the x-range
y_line = objective(x_line, a, b, c)
# Create Plots
pyplot.plot(x_line, y_line, '--', color='red')
pyplot.show()

def objective(x, a, b, c, d, e):
    return (a * x) + (b * x**2) + (c * x**3) + (d * x**4) + e

# ---- Fit Curve ----
data = econ.values
# Values to be fit
y, x = data[:,6], data[:,18]
# Fit Curve
popt, _ = curve_fit(objective, x, y)
# Summarize parameter Values
a, b, c, d, e = popt
# Plot Values
pyplot.scatter(x, y)
# Define input range
x_line = arange(min(x), max(x), 1)
# Calculate Y-values for the x-range
y_line = objective(x_line, a, b, c, d, e)
# Create Plots
pyplot.plot(x_line, y_line, '--', color='red')
pyplot.show()


def objective(x, a, b, c, d, e, f):
    return (a * x) + (b * x**2) + (c * x**3) + (d * x**4) + (e * x**5) + f

# ---- Fit Curve ----
data = econ.values
# Values to be fit
y, x = data[:,6], data[:,18]
# Fit Curve
popt, _ = curve_fit(objective, x, y)
# Summarize parameter Values
a, b, c, d, e, f = popt
# Plot Values
pyplot.scatter(x, y)
# Define input range
x_line = arange(min(x), max(x), 1)
# Calculate Y-values for the x-range
y_line = objective(x_line, a, b, c, d, e, f)
# Create Plots
pyplot.plot(x_line, y_line, '--', color='red')
pyplot.show()

def objective(x, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u):
    return ((a * x) + (b * x**1.2) + (c * x**1.4) + (d * x**1.6) + (e * x**1.8) + (f * x**2) + (g * x**2.2) 
            + (h * x**2.4) + (i * x**2.6) + (j * x**2.8) + (k * x**3) + (l * x**3.2) + (m * x**3.4) + (n * x**3.6)
            + (o * x**3.8) + (p * x**3.8) + (q * x**4) + (r * x**4.2) + (s * x**4.4) + (t * x**4.6) + u)

# ---- Fit Curve ----
data = econ.values
# Values to be fit
y, x = data[:,6], data[:,18]
# Fit Curve
popt, _ = curve_fit(objective, x, y)
# Summarize parameter Values
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u = popt
# Plot Values
pyplot.scatter(x, y)
# Define input range
x_line = arange(min(x), max(x), 1)
# Calculate Y-values for the x-range
y_line = objective(x_line, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u)
# Create Plots
pyplot.plot(x_line, y_line, '--', color='red')
pyplot.show()

# The data is too dynamic for a simple polynomial.
    # We can cut the data into simplier pieces.
    # Reset the x axis though.
econ_sm = econ[econ.index > 123]
econ_sm ['x2'] = econ_sm['x'] - 124


def objective(x, a, b, c, d, e, f):
    return (a * x) + (b * x**2.5) + (c * x**3.5) + (d * x**4) + (e * x**4.5) + f

# ---- Fit Curve ----
data = econ_sm.values
# Values to be fit
y, x = data[:,6], data[:,18]
# Fit Curve
popt, _ = curve_fit(objective, x, y)
# Summarize parameter Values
a, b, c, d, e, f = popt
# Plot Values
pyplot.scatter(x, y)
# Define input range
x_line = arange(min(x), max(x), 1)
# Calculate Y-values for the x-range
y_line = objective(x_line, a, b, c, d, e, f)
# Create Plots
pyplot.plot(x_line, y_line, '--', color='red')
pyplot.show()


# Final optimized model

def objective(x, a, b, c, d, e, f, g, h, i):
    return ((a * x) + (b * x**1.2) + (c * x**1.4) + (d * x**1.6) + (e * x**1.8) + (f * x**3) + (g * x**4.7) 
            + (h * x**4.8) + i)

# ---- Fit Curve ----
data = econ_sm.values
# Values to be fit
y, x = data[:,6], data[:,18]
# Fit Curve
popt, _ = curve_fit(objective, x, y)
# Summarize parameter Values
a, b, c, d, e, f, g, h, i = popt
# Plot Values
pyplot.scatter(x, y)
# Define input range
x_line = arange(min(x), max(x), 1)
# Calculate Y-values for the x-range
y_line = objective(x_line, a, b, c, d, e, f, g, h, i)
# Create Plots
pyplot.plot(x_line, y_line, '--', color='red')
pyplot.show()

# Generating granular data 
T = 60
p = 120
r = T/p
pointStack = []
for z in range(1, p + 1):
    point = z * r
    pointStack.append(point)
pointStack2 = pd.DataFrame(pointStack)
pointStack2 = pointStack2.rename(columns={0: 'x'})
curveStack = objective(pointStack2['x'], a, b, c, d, e, f, g, h, i)
curveStack = pd.DataFrame(curveStack)
curveStack2 = curveStack.rename(columns = {'x':'LBR'})
curveStack2 = pd.concat([pointStack2, curveStack2], axis=1)

pyplot.scatter(curveStack2['x'], curveStack2['LBR'], color = 'red')
pyplot.scatter(x, y)
pyplot.show()