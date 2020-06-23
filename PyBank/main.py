{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import the modules that I will need\n",
    "import os\n",
    "import csv\n",
    "\n",
    "#indicate the path to the file that we will be looping through\n",
    "bank_data = os.path.join(\"Resources\", \"PyBank_Resources_budget_data.csv\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#create new lists that we will be storing data in when we run our loop\n",
    "date=[]\n",
    "revenue=[]\n",
    "revenue_change_list=[]\n",
    "\n",
    "#Set up all of the variables that we will need to use with their starting values\n",
    "month_count=0\n",
    "total_revenue=0\n",
    "current_month_revenue=0\n",
    "revenue_change=0\n",
    "average_revenue_change=0\n",
    "greatest_increase=0\n",
    "greatest_decrease=0\n",
    "\n",
    "#note: the starting revenue value was pulled from the first line of the dataset\n",
    "starting_month_revenue=867884\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#we need to open the file that we are going to loop through\n",
    "with open(bank_data) as csvfile:\n",
    "    csvreader=csv.reader(csvfile, delimiter=\",\")\n",
    "    \n",
    "    #we need to skip the header row\n",
    "    next(csvreader)\n",
    "    \n",
    "    #each row from the csvreader will be an iteration in the loop\n",
    "    for row in csvreader:\n",
    "        #we add each row value to the new separate lists that we created above\n",
    "        date.append(row[0])\n",
    "        revenue.append(row[1])\n",
    "        \n",
    "        #since each row is a new month...the month count is a simple count of the rows\n",
    "        month_count+=1\n",
    "        \n",
    "        #we set a new variable to be the value in the second column of our original dataset\n",
    "        current_month_revenue=int(row[1])\n",
    "        \n",
    "        #this is the total revenue counter and it adds the current month value with each iteration\n",
    "        total_revenue=total_revenue + current_month_revenue\n",
    "        \n",
    "        #this tracks the revenue change between each iteration\n",
    "        revenue_change=(current_month_revenue)-(starting_month_revenue)\n",
    "        \n",
    "        #we reset the starting month value for the next iteration...it is now the current month value\n",
    "        starting_month_revenue=current_month_revenue\n",
    "        \n",
    "        #we add the revenue change amount for this iteration to a new list that was created above\n",
    "        revenue_change_list.append(revenue_change)\n",
    "        \n",
    "        #this tracks the total value of the revenue change between each iteration\n",
    "        #it will be used outside of the loop to calculate the average after the final iteration is run\n",
    "        average_revenue_change = (average_revenue_change + revenue_change)\n",
    "        \n",
    "        #we set the greatest inc/dec variables to the only value in the new list that we created above\n",
    "        greatest_increase=revenue_change_list[0]\n",
    "        greatest_decrease=revenue_change_list[0]\n",
    "        \n",
    "        #we create a new loop inside our other loop to find the greatest inc/dec\n",
    "        #it will run as many iterations as there are rows in our new revenue change list\n",
    "        for i in range(len(revenue_change_list)):\n",
    "            if revenue_change_list[i]>=greatest_increase:\n",
    "                greatest_increase=revenue_change_list[i]\n",
    "                greatest_increase_date=date[i]\n",
    "                \n",
    "            elif revenue_change_list[i]<=greatest_decrease:\n",
    "                greatest_decrease=revenue_change_list[i]\n",
    "                greatest_decrease_date=date[i]\n",
    "                \n",
    "    #we calculate the average revenue change...note: it is outside the loop as it is done at the end\n",
    "    #we have to minus one from the month count since the first month doesn't count towards revenue change\n",
    "    average_revenue_change = round((average_revenue_change)/((month_count)-1),2)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "FINANCIAL ANALYSIS\n",
      "___________________\n",
      "                   \n",
      "Total Months: 86\n",
      "Total:  $38382578\n",
      "Average Change: $-2315.12\n",
      "Greatest Increase In Profits: Feb-2012 ($1926159)\n",
      "Greatest Decrease In Profits: Sep-2013 ($-2196167)\n"
     ]
    }
   ],
   "source": [
    "#now we have to print the values that we calculated above\n",
    "\n",
    "print(f'FINANCIAL ANALYSIS')\n",
    "print(f'___________________')\n",
    "print(f'                   ')\n",
    "print(f'Total Months: {month_count}')\n",
    "print(f'Total:  ${total_revenue}')\n",
    "print(f'Average Change: ${average_revenue_change}')\n",
    "print(f'Greatest Increase In Profits: {greatest_increase_date} (${greatest_increase})')\n",
    "print(f'Greatest Decrease In Profits: {greatest_decrease_date} (${greatest_decrease})')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#now we need to export the results to a new text file\n",
    "\n",
    "results=os.path.join(\"Analysis\", \"Financial_Analysis.txt\")\n",
    "\n",
    "with open(results, \"w\") as textfile:\n",
    "    writer=csv.writer(textfile)\n",
    "    \n",
    "    writer.writerow([f'FINANCIAL ANALYSIS'])\n",
    "    writer.writerow([f'___________________'])\n",
    "    writer.writerow([f'Total Months: {month_count}'])\n",
    "    writer.writerow([f'Total:  ${total_revenue}'])\n",
    "    writer.writerow([f'Average Change: ${average_revenue_change}'])\n",
    "    writer.writerow([f'Greatest Increase In Profits: {greatest_increase_date} (${greatest_increase})'])\n",
    "    writer.writerow([f'Greatest Decrease In Profits: {greatest_decrease_date} (${greatest_decrease})'])"
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
