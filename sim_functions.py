import schedule_parse
import numpy as np

STANDARD_DEVIATION = 1
REMAINING_SCHEDULE = schedule_parse.get_remaining_schedule()

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

def get_team_stats():
    TEAM_STATS = [
        dict(name="GT", matches=12, wins=9, losses=3, nrr=0.795, points=18),
        dict(name="RCB", matches=12, wins=8, losses=3, nrr=0.482, points=17),
        dict(name="PBKS", matches=12, wins=8, losses=3, nrr=0.389, points=17),
        dict(name="MI", matches=13, wins=8, losses=5, nrr=1.292, points=16),
        dict(name="DC", matches=13, wins=6, losses=6, nrr=-0.019, points=13),
        dict(name="KKR", matches=13, wins=5, losses=6, nrr=0.193, points=12),
        dict(name="LSG", matches=12, wins=5, losses=7, nrr=-0.506, points=10),
        dict(name="SRH", matches=12, wins=4, losses=7, nrr=-1.005, points=9),
        dict(name="RR", matches=14, wins=3, losses=10, nrr=-0.549, points=8),
        dict(name="CSK", matches=13, wins=3, losses=10, nrr=-1.030, points=6)
    ]
    return TEAM_STATS

def simulate_season():
    team_stats = get_team_stats()
    # Simulate all matches
    for team1, team2 in REMAINING_SCHEDULE:
        # print(f"Team 1: {team1} Team 2: {team2}")
        simulate_match(team1, team2, team_stats)

    # Sort by points then NRR
    team_stats_sorted = sorted(team_stats, key=lambda x: (x["points"], x["wins"], x["nrr"]))

    return team_stats_sorted

