{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import the modules necessary to run code\n",
    "\n",
    "import os\n",
    "import csv\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#set variables and dictionaries that will get filled with data\n",
    "\n",
    "total_votes=0\n",
    "\n",
    "candidate_votes={}\n",
    "\n",
    "candidate_percentages={}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "#declare the path to the file I will use\n",
    "\n",
    "poll_data = os.path.join(\"Resources\", \"PyPoll_Resources_election_data.csv\")\n",
    "\n",
    "#open the file that I need to loop through\n",
    "\n",
    "with open(poll_data) as csvfile:\n",
    "    csvreader=csv.reader(csvfile, delimiter=\",\")\n",
    "    \n",
    "    #skip header row\n",
    "    \n",
    "    next(csvreader)\n",
    "    \n",
    "    #using each row in the datafile as its own iteration\n",
    "    #count the total rows (which are votes) and set a variable to be the value in the 3rd column\n",
    "    \n",
    "    for row in csvreader:\n",
    "        total_votes+=1\n",
    "        \n",
    "        candidate=row[2]\n",
    "        \n",
    "        #start filling the data into the empty dictionary\n",
    "        #add a new key for each unique candidate plus the vote that it represents\n",
    "        \n",
    "        if candidate not in candidate_votes.keys():\n",
    "            candidate_votes[candidate] = 1\n",
    "        \n",
    "        #if we already have a key with that candidate...just increase the value by one vote\n",
    "        \n",
    "        else:\n",
    "            candidate_votes[candidate] +=1\n",
    "   \n",
    "    #this allows us to iterate through our dictionary for each key value and calculate the percentage of the votes \n",
    "\n",
    "for key, value in candidate_votes.items():\n",
    "    candidate_percentages[key]=format(((value/total_votes)*100),'.3f')\n",
    "        \n",
    "    #this will search through our dictionary for the greatest \"value\" and return its \"key\"\n",
    "\n",
    "winning_candidate = max(candidate_votes, key=candidate_votes.get)         \n"
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
      "ELECTION RESULTS\n",
      "___________________________\n",
      "                  \n",
      "TOTAL VOTES:  3521001\n",
      "___________________________\n",
      "                  \n",
      "Khan:  63.000%  (2218231)\n",
      "Correy:  20.000%  (704200)\n",
      "Li:  14.000%  (492940)\n",
      "O'Tooley:  3.000%  (105630)\n",
      "___________________________\n",
      "                  \n",
      "WINNER:  Khan\n",
      "___________________________\n"
     ]
    }
   ],
   "source": [
    "#printing the election results in the correct format\n",
    "\n",
    "print(f'ELECTION RESULTS')\n",
    "print(f'___________________________')\n",
    "print(f'                  ')\n",
    "print(f'TOTAL VOTES:  {total_votes}')\n",
    "print(f'___________________________')\n",
    "print(f'                  ')\n",
    "for key, value in candidate_votes.items():\n",
    "    print(f'{key}:  {format(((value/total_votes)*100),\".3f\")}%  ({value})')\n",
    "print(f'___________________________')\n",
    "print(f'                  ')\n",
    "print(f'WINNER:  {winning_candidate}')\n",
    "print(f'___________________________')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "    #writing the new text file with the results\n",
    "    #note: it is one tab over so that our orignial csv is still open and we can calculate the values below\n",
    "    \n",
    "    results=os.path.join(\"Analysis\", \"Election_Results.txt\")\n",
    "\n",
    "    with open(results, \"w\") as textfile:\n",
    "        writer=csv.writer(textfile)\n",
    "    \n",
    "        writer.writerow([f'ELECTION RESULTS'])\n",
    "        writer.writerow([f'___________________________'])\n",
    "        writer.writerow([f'TOTAL VOTES:  {total_votes}'])\n",
    "        writer.writerow([f'___________________________'])\n",
    "        for key, value in candidate_votes.items():\n",
    "            writer.writerow([f'{key}:  {format(((value/total_votes)*100),\".3f\")}%  ({value})'])\n",
    "        writer.writerow([f'___________________________'])\n",
    "        writer.writerow([f'WINNER:  {winning_candidate}'])\n",
    "        writer.writerow([f'___________________________'])\n",
    "    "
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
