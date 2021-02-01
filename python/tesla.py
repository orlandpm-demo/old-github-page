# Using readlines() 
file = open('TSLA.csv', 'r') 
lines = file.readlines() 
  
count = 0

greatest_so_far = 0
greatest_date = None

# Strips the newline character 
for line in lines: 
    count += 1
    if count > 1:
        columns = line.strip().split(',')
        change = float(columns[4]) - float(columns[1])
        if change > greatest_so_far:
            greatest_so_far = change
            greatest_date = columns[0]

print(greatest_date, greatest_so_far)