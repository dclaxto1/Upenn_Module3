import os
import csv

budget_csv = os.path.join("Resources", "Budget_data.csv")

total_months = 0
total_amount = 0
diff_count = 0
prev_value = 0
diff_total = 0 
diff_avg = 0
max_increase = 0
max_decrease = 0
max_increase_month = ""
max_decrease_month = ""
#dif_val is the change amount


#open csv file and count total number of months
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header = next(csv_reader)
    for row in csv_reader:
        # Q1 - total number of months
        total_months +=1 

        # Q2 - net total amt of prof/loss
        total_amount = total_amount + int(row[1])

        #Q3 - changes in prof/loss and get avg 
        if total_months >= 2:
            diff_count +=1 
            diff_val = int(row[1]) - prev_value
            diff_total += diff_val
            prev_value = int(row[1])

            if diff_val > max_increase:
                max_increase = diff_val
                max_increase_month = row[0]
            if diff_val < max_decrease:
                max_decrease = diff_val
                max_decrease_month = row[0]        
        else: # month 1:
            prev_value = int(row[1])
            max_increase_month = row[0]
            max_decrease_month = row[0]
        
diff_avg = round(diff_total/diff_count, 2)

#print the total number of months
print(f"Total months: {total_months}")
#print the total of profit and loss
print(f"Total amount is: {total_amount}")
#print the average change
print(f"The average change is: {diff_avg}")
print(f"Greatest increase in profits {max_increase}, {max_increase_month}")
print(f"Greatest decrease in profits: {max_decrease},{max_decrease_month}")

#write to output file
output_file = open("analysis/bankanalysis.txt","w")
output_file.write(f"Total months: {total_months}\n")
output_file.write(f"\n")
output_file.write(f"Total amount is: {total_amount}\n")
output_file.write(f"\n")
output_file.write(f"The average change is: {diff_avg}\n")
output_file.write(f"\n")
output_file.write(f"Greatest increase in profits {max_increase}, {max_increase_month}\n")
output_file.write(f"\n")
output_file.write(f"Greatest decrease in profits: {max_decrease},{max_decrease_month}\n")
output_file.close