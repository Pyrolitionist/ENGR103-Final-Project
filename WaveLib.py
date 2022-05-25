import numpy as np


def sort_discharge(discharge):
    sort = sorted(discharge, key=float)
    return sort

def recurrence_interval(ranking):
    rec_int = np.zeros(len(ranking))
    for x in range(len(ranking)):
        rec_int[x] = (len(ranking) + 1)/(ranking[x])
    return rec_int
