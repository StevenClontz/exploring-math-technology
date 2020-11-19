data_one = [] # fill in values from first dataset
data_two = [] # fill in this too

# if means are different, data was entered incorrectly
from statistics import mean
assert mean(data_one) == mean(data_two), "Means should be the same"
print("The mean for each dataset is FIXME") # print out the mean of the datasets

deviations_one = [
    abs( value - mean(data_one) ) # measure distance of value from the mean
    for value in data_one # do this for each value of data
]
print(deviations_one)
deviations_two = [] # TODO
print(deviations_two) # prints [5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 1, 1, 3, 4, 6]