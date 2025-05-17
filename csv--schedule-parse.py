import csv
from datetime import datetime, timedelta

remaining_schedule = []

team_names = {
    "Gujarat Titans": "GT",
    "Royal Challengers Bengaluru": "RCB",
    "Punjab Kings": "PBKS",
    "Mumbai Indians": "MI",
    "Delhi Capitals": "DC",
    "Lucknow Super Giants": "LSG",
    "Kolkata Knight Riders": "KKR",
    "Sunrisers Hyderabad": "SRH",
    "Rajasthan Royals": "RR",
    "Chennai Super Kings": "CSK"
}

with open("ipl-2025-EasternStandardTime.csv", "r") as file:
    csv_reader = csv.reader(file)
    counter = 0
    for row in csv_reader:
        if counter == 0:
            counter += 1
            continue
        date = datetime.strptime(row[2], "%d/%m/%Y %H:%M")
        print(date)
        present = datetime.now()
        if (date.date() >= present.date()):
            if row[4] in team_names and row[5] in team_names:
                remaining_schedule.append((team_names[row[4]],
                                           team_names[row[5]]))

print(remaining_schedule)

