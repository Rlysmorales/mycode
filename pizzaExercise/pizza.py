#!/usr/bin/python3
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Spring', 'Summer', 'Fall', 'Winter'
sizes = [30, 40 ,20  , 10]
explode = (0, 0.3, 0, 0)  # only "explode" the 2nd slice (i.e. 'Summer')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.savefig("/home/student/static/perfectSummerWeather.png")
