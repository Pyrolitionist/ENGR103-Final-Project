import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import WaveLib as wL

# Reads and imports annual peak discharge data of the willamette river
willamette_peak_discharge = pd.read_csv("C:/Users/chris/OneDrive/Desktop/Willamette river peak discharges.csv")
Discharge = willamette_peak_discharge.loc[:, 'Discharge']

# Makes an array of 1 through n for the length of discharges
discharge_rank = np.zeros(len(Discharge))
for x in range(len(Discharge)):
    discharge_rank[x] = 1 + x
print(discharge_rank)

# Sorts discharge from the greatest to the least flow
sorted_discharge = wL.sort_discharge(Discharge)
inverted_discharge = sorted_discharge[::-1]

# Makes an array of recurrence intervals based on rank array
recurrence_interval = wL.recurrence_interval(discharge_rank)
print(recurrence_interval)

lin_reg = np.polyfit(recurrence_interval, inverted_discharge, 1)
best_fit_line = np.log(lin_reg[0] * recurrence_interval + lin_reg[1])

fig, ax = plt.subplots()
ax.scatter(recurrence_interval, inverted_discharge, marker='.', color='black')
ax.plot(recurrence_interval, best_fit_line, color='r')
plt.ylim(0, 12)
plt.semilogx()

plt.show()
