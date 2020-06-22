{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import the different modules that I need \n",
    "\n",
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#create a list for each column so I can get a total later on\n",
    "\n",
    "date = []\n",
    "profit_loss = []\n",
    "monthly_revenue_change = []\n",
    "\n",
    "#set the variables\n",
    "\n",
    "months_count = 0\n",
    "profit_loss_total = 0\n",
    "monthly_change_amount = 0\n",
    "starting_profit = 867884\n",
    "monthly_change_amount_total=0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#open up the file that I need to loop through\n",
    "\n",
    "bank_data = os.path.join(\"Resources\", \"PyBank_Resources_budget_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#read through the csv file that contains my data\n",
    "\n",
    "with open(bank_data) as csvfile:\n",
    "    csvreader=csv.reader(csvfile, delimiter=\",\")\n",
    "    \n",
    "    #skip header row\n",
    "    \n",
    "    next(csvreader)\n",
    "    \n",
    "    #loop through the data and count the number of months\n",
    "\n",
    "    for row in csvreader:\n",
    "        \n",
    "        #separate out the months and the profit/loss in to 2 different lists\n",
    "        \n",
    "        date.append(row[0])\n",
    "        profit_loss.append(row[1])\n",
    "        \n",
    "        #count the total number of months\n",
    "        \n",
    "        months_count += 1\n",
    "        \n",
    "        #total up the amount of profits and losses over the entire dataset \n",
    "        \n",
    "        profit_loss_total = profit_loss_total + int(row[1])\n",
    "        \n",
    "        #figure out the average monthly change by first setting the profit variable\n",
    "        \n",
    "        monthly_profit = int(row[1])\n",
    "        \n",
    "        #figure out the revenue change between the last iteration and the current iteration by setting the variable\n",
    "        \n",
    "        monthly_change_amount = (monthly_profit)-(starting_profit)\n",
    "        \n",
    "        #add that change amount to the list that we created above\n",
    "        \n",
    "        monthly_revenue_change.append(monthly_change_amount)\n",
    "        \n",
    "        #we have to reset the new starting profit amount to the monthly profit from the current iteration\n",
    "        \n",
    "        starting_profit = monthly_profit\n",
    "        \n",
    "        #we have to add the monthly change amount from this iteration to the total monthly change counter\n",
    "        \n",
    "        monthly_change_amount_total = monthly_change_amount_total + monthly_change_amount\n",
    "        \n",
    "        #__________________________________________________________________________________\n",
    "        \n",
    "        \n",
    "        greatest_increase_profits = monthly_revenue_change[0]\n",
    "        greatest_decrease_profits = monthly_revenue_change[0]\n",
    "        \n",
    "        for i in range(len(monthly_revenue_change)):\n",
    "            if monthly_revenue_change[i] >= greatest_increase_profits:\n",
    "                greatest_increase_profits = monthly_revenue_change[i]\n",
    "                greatest_increase_date = date[i]\n",
    "                \n",
    "            elif monthly_revenue_change[i] <= greatest_decrease_profits:\n",
    "                greatest_decrease_profits = monthly_revenue_change[i]\n",
    "                greatest_decrease_date = date[i]\n",
    "                \n",
    "        \n",
    "    #find the average...but remember not to use the first month...and make sure it is outside of the for loop\n",
    "        \n",
    "    monthly_change_amount_average = round((monthly_change_amount_total)/(months_count - 1),2)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "_____________________\n",
      "                     \n",
      "Total Months:  86\n",
      "Total:  $38382578\n",
      "Average Monthly Change:  $-2315.12\n",
      "Greatest Increase In Profits:  Feb-2012  ($1926159)\n",
      "Greatest Increase In Profits:  Sep-2013  ($-2196167)\n"
     ]
    }
   ],
   "source": [
    "\n",
    "print(\"Financial Analysis\")\n",
    "print(\"_____________________\")\n",
    "print(\"                     \")\n",
    "\n",
    "print(f'Total Months:  {months_count}')\n",
    "print(f'Total:  ${profit_loss_total}')\n",
    "print(f'Average Monthly Change:  ${monthly_change_amount_average}')\n",
    "print(f'Greatest Increase In Profits:  {greatest_increase_date}  (${greatest_increase_profits})')\n",
    "print(f'Greatest Increase In Profits:  {greatest_decrease_date}  (${greatest_decrease_profits})')\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
