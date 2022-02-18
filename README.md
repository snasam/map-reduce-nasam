# map-reduce-nasam
## Data Details
The data set contains the information about different covid variants reported from different location at different dates.

## Analysis

I have processed the raw data using mapping technique and mapped two fields location, num_sequences_total. Now we total cases reported from each location everyday. By using reducing tecnique, I have reduced data and now we total cases reported from each location in total.

## Execution Commands
Mapping:
cat covid-variants.csv | Python 1mapper.py > nasamoutput1.txt

Reducing:
 cat covid-variants.csv | Python 1mapper.py | sort | Python 1reducer.py > nasamoutput2.txt

## Chart:


![Picture1](https://user-images.githubusercontent.com/77593263/154758013-892bbc63-41fc-4c82-916b-720f7ba10a8d.png)











