import numpy as np


#######################################################################
# Function: sort_discharge
# Description: sorts the data points by discharge
# Parameters: data series
# Return values: sorted data series
# Pre-Conditions: N/A
# Post-Conditions: N/A
#######################################################################
def sort_discharge(discharge):
    sort = sorted(discharge, key=float)
    return sort


#######################################################################
# Function: recurrence_interval
# Description: calculates the recurrence interval for each data point
# Parameters: rank of discharge 1 to n
# Return values: recurrence interval
# Pre-Conditions: N/A
# Post-Conditions: N/A
#######################################################################
def recurrence_interval(ranking):
    rec_int = np.zeros(len(ranking))
    for x in range(len(ranking)):
        rec_int[x] = (len(ranking) + 1)/(ranking[x])
    return rec_int


#######################################################################
# Function: calculate_100yr_flood
# Description: calculates the discharge of the 100-year flood
# Parameters: line of best fit
# Return values: discharge of 100 year flood
# Pre-Conditions: N/A
# Post-Conditions: N/A
#######################################################################
def calculate_100yr_flood(regression):
    flood = regression[0] * np.log(100) + regression[1]
    return flood
