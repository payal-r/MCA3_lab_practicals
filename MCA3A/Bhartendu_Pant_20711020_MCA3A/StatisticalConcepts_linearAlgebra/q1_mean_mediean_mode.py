import numpy as np
from scipy import stats

dataset = [4,4,2,2,8,9,4]
mean = np.mean(dataset)
print(mean)

sorted_dataset=sorted(dataset)

median = np.median(sorted_dataset)
print(median)

mode = stats.mode(dataset)
print(mode)
