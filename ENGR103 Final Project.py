#######################################################################
# Program Filename: ENGR103 Final Project
# Author: Chris Milford
# Date: 6/6/2022
# Description:
# Input: Peak annual discharge .csv file
# Output: Discharge of 100 Year Flood
#######################################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import WaveLib as wL

# Reads and imports annual peak discharge data of the willamette river
willamette_peak_discharge = pd.read_csv("C:/Users/chris/Downloads/Willamette river peak discharges - Sheet1.csv")
Discharge = willamette_peak_discharge.loc[:, 'Discharge']

# Makes an array of 1 through n for the length of discharges
discharge_rank = np.zeros(len(Discharge))
for x in range(len(Discharge)):
    discharge_rank[x] = 1 + x

# Sorts discharge from the greatest to the least flow
sorted_discharge = wL.sort_discharge(Discharge)
inverted_discharge = sorted_discharge[::-1]

# Makes an array of recurrence intervals based on rank array
recurrence_interval = wL.recurrence_interval(discharge_rank)

# Calculates Regression for Logarithmic Dataset, Makes Line Of Best Fit
lin_reg = np.polyfit(np.log(recurrence_interval), inverted_discharge, 1)
best_fit_line = lin_reg[0] * np.log(recurrence_interval) + lin_reg[1]

# Calculates 100 Year Flood and adds it to data set
hundred_year_flood = wL.calculate_100yr_flood(lin_reg)
best_fit_line = np.append(best_fit_line, hundred_year_flood)
recurrence_interval = np.append(recurrence_interval, 100)
inverted_discharge = np.append(inverted_discharge, hundred_year_flood)

# Output & Data Interpretation
print('#############################################################################################################')
print('The estimated discharge for the 100 year flood for this area of this stream is', hundred_year_flood, 'cfs')
print('-----------------------------------------------------------------------------------------------------------')
print('Interpretation of Data for User:')
print('This indicates that every year there is a 1% chance for a flood this large to occur, and that any areas that')
print('will be affected by this flood are labeled as within the 100 year flood plane which impacts insurance, risk')
print('of purchasing property, personal safety, as well as tighter regulations on government safety standards.')
print('#############################################################################################################')

# Plotting Data
fig, ax = plt.subplots()
ax.plot(recurrence_interval, best_fit_line, color='red', linestyle='--')
ax.plot(100, hundred_year_flood, marker='o', color='blue', label='100 Year Flood')
ax.scatter(recurrence_interval, inverted_discharge, marker='.', color='black', label='Annual Peak Discharges')
ax.legend()
plt.title('Annual Peak Discharges 2010 - 2021')
ax.set_xlabel('Recurrence Interval (years)')
ax.set_ylabel('Peak Discharge (cfs)')
plt.semilogx()
plt.show()
