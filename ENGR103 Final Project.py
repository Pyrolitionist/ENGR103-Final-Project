import pandas as pd
import numpy as np
import matplotlib as plt
import WaveLib as wL

# Reads and imports annual peak discharge data of the willamette river
willamette_peak_discharge = pd.read_csv("C:/Users/chris/OneDrive/Desktop/Willamette river peak discharges.csv")
Discharge = willamette_peak_discharge.loc[:, 'Discharge']

# Makes an array of 1 through n for the length of discharges
discharge_rank = np.zeros(len(Discharge))
for x in range(len(Discharge)):
    discharge_rank[x] = 1 + x
print(discharge_rank)

# Sorts discharge from greatest to least flow
sorted_discharge = wL.sort_discharge(Discharge)

# Makes an array of recurrence intervals based on rank array
recurrence_interval = wL.recurrence_interval(discharge_rank)
print(recurrence_interval)

fig, ax = plt.subplots()
ax.plot(recurrence_interval, Discharge, linewidth=2.0)
ax.set_yscale('log')
plt.show()
