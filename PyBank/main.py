import os

import csv

print(os.getcwd())

# Having problems with default directory, I used full directory to get around it
csvpath = os.path.join("..", "c:/Users/eceka/Google Drive/BootCampWork/python---challenge/PyBank/Resources","budget_data.csv")
#csvpath = os.path.join("..", "Resources","budget_data.csv")

months_list = []
months_count = []
profit_loss_list = []
net_profit = []
avg_change = []
max_increase = []
max_decrease = []
date_inc = []
date_dec = []

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile)

 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")


    for row in csvreader:
        
        months_list.append(row[0])
        profit_loss_list.append(int(row[1]))

  
    months_count = len(months_list)
    net_profit = sum(profit_loss_list)
    avg_change = (net_profit / months_count)
    max_increase = max(profit_loss_list)
    max_decrease = min(profit_loss_list)

    date_inc_i = profit_loss_list.index(max_increase)
    date_dec_i = profit_loss_list.index(max_decrease)
    date_inc = months_list[date_inc_i]
    date_dec = months_list[date_dec_i]

    print(f'Total Months: {months_count}' )
    print(f'Total Net Profit: ${net_profit}')
    print(f'Average Change: ${avg_change}')
    print(f'Greatest Increase in Profits: {date_inc} (${max_increase})')
    print(f'Greatest Decrease in Profits: {date_dec} (${max_decrease})')
    

