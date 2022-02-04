import sys

for line in sys.stdin:  
    dataList = line.strip().split(",") 
    
    if (len(dataList) == 4) :
        location,date,variant,num_sequences_total = dataList 
        print (location,"\t", num_sequences_total)

