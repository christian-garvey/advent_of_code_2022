##############################################
# AoC Day 04
## P01 answer - 
## P02 answer - 
##############################################

## Libraries
import pandas as pd

## Request data
# from request_input_data import get_input
# data = get_input(4)

day = "04"
file = f"day{day}_input.txt"

## Read data and strip "/n"
lines = open(file).readlines()
lines_strip = [l.strip() for l in lines]
# print(lines_strip)

data = pd.DataFrame(lines_strip)
# print(data.head())


## Split data at ","
for i, r in data.iterrows():
    str(r)
    r.str.split(",")
    print(r)

print(data.head())

## Split on "-" 

## Do check on Pair 1
### If pair1_int[0] <= pair2_int[0] 
###     AND pair1_int[1] >= pair2_int[1] 
###    Then fully contained and add to list
### If not, then...
## Do check on Pair 2
### If pair2_int[0] <= pair1_int[0] 
###     AND pair2_int[1] >= pair1_int[1] 
###    Then fully contained and add to list




## Assumes that pairs are always ascending --> 
# To negate this, If int[0] > int[1], then swap around

#__________________________________
## Cycle through chars in string
### If get to char which is not intIf char is integer