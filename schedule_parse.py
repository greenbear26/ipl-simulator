import csv
from datetime import datetime, timedelta

def get_remaining_schedule():
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
            date = datetime.strptime(row[2], "%d/%m/%Y %H:%M") + timedelta(hours
                                                                           = 4)
            present = datetime.now()
            # print(f"Match: {date} Now: {present} Match Later than now: {date>present}")
            if (date >= present):
                if row[4] in team_names and row[5] in team_names:
                    remaining_schedule.append((team_names[row[4]],
                                               team_names[row[5]]))
    print(remaining_schedule)
    return remaining_schedule
