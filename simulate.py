import numpy as np

STANDARD_DEVIATION = 1

def find_team_index(team_name, team_stats):
    return next(i for i, team in enumerate(team_stats) if team["name"] == team_name)

def simulate_match(team1_name, team2_name, team_stats):
    i1, i2 = find_team_index(team1_name, team_stats), find_team_index(team2_name, team_stats)
    t1, t2 = team_stats[i1], team_stats[i2]

    t1_nrr_sample = np.random.normal(loc=t1["nrr"], scale=STANDARD_DEVIATION)
    t2_nrr_sample = np.random.normal(loc=t2["nrr"], scale=STANDARD_DEVIATION)
    nrr_diff = t1_nrr_sample - t2_nrr_sample

    # Decide match outcome
    if nrr_diff >= 0:
        t1["wins"] += 1
        t2["losses"] += 1
        t1["points"] += 2
    else:
        t1["losses"] += 1
        t2["wins"] += 1
        t2["points"] += 2

    # Update match count first
    t1["matches"] += 1
    t2["matches"] += 1

    # Update average NRR using running average
    t1["nrr"] += nrr_diff / t1["matches"]
    t2["nrr"] -= nrr_diff / t2["matches"]

counter = 0

overall_team_score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while counter < 1000:
    # Initial team data
    team_stats = [
        dict(name="GT", matches=11, wins=8, losses=3, nrr=0.793, points=16),
        dict(name="RCB", matches=11, wins=8, losses=3, nrr=0.482, points=16),
        dict(name="PBKS", matches=11, wins=7, losses=3, nrr=0.376, points=15),
        dict(name="MI", matches=12, wins=7, losses=5, nrr=1.156, points=14),
        dict(name="DC", matches=11, wins=6, losses=4, nrr=0.362, points=13),
        dict(name="KKR", matches=12, wins=5, losses=6, nrr=0.193, points=11),
        dict(name="LSG", matches=11, wins=5, losses=6, nrr=-0.469, points=10),
        dict(name="SRH", matches=11, wins=3, losses=7, nrr=-1.192, points=7),
        dict(name="RR", matches=12, wins=3, losses=9, nrr=-0.718, points=6),
        dict(name="CSK", matches=12, wins=3, losses=9, nrr=-0.992, points=6)
    ]

    remaining_matches = [
        ("PBKS", "DC"),
        ("LSG", "RCB"),
        ("SRH", "KKR"),
        ("PBKS", "MI"),
        ("DC", "GT"),
        ("CSK", "RR"),
        ("RCB", "SRH"),
        ("GT", "LSG"),
        ("MI", "DC"),
        ("RR", "PBKS"),
        ("RCB", "KKR"),
        ("GT", "CSK"),
        ("LSG", "SRH")
    ]

    # Simulate all matches
    for team1, team2 in remaining_matches:
        simulate_match(team1, team2, team_stats)

    # Sort by points then NRR
    team_stats_sorted = sorted(team_stats, key=lambda x: (x["points"], x["wins"], x["nrr"]))

# Print final standings
# for team in reversed(team_stats_sorted):
#     print(f'{team["name"]} Points: {team["points"]} NRR: {team["nrr"]:.3f}')

    for i in range(0, len(team_stats_sorted)):
        team_index = find_team_index(team_stats_sorted[i]["name"], team_stats)
        overall_team_score[team_index] += i + 1
    counter+=1


# Print final results
print("Average Team Positioning")
for i in range(0, len(overall_team_score) - 1):
    value = overall_team_score[i]
    for j in range(i + 1, len(overall_team_score)):
        new_team_score = overall_team_score[j]
        if new_team_score < value:
            overall_team_score[j] = overall_team_score[i]
            overall_team_score[i] = new_team_score

            new_team = team_stats[j]
            team_stats[j] = team_stats[i]
            team_stats[i] = new_team

for i in range(len(overall_team_score) - 1, -1, -1):
    team = team_stats[i]
    print(f'{team["name"]} Average Standing: {overall_team_score[i]/1000}')

