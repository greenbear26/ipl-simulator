import sim_functions
import sys

simulations = 100000
team_1 = sys.argv[1] if len(sys.argv) > 1 else input("Team 1? ")
team_2 = sys.argv[2] if len(sys.argv) > 2 else input("Team 2? ")

for team in team_1, team_2:
    if (any(team == teams["name"] for teams in sim_functions.get_team_stats())):
        continue
    else:
        print(f"Invalid team(s), please select from {[teams["name"] for teams in
                                                   sim_functions.get_team_stats()]}")
        exit()

print(f"Predicting match for {team_1} and {team_2}")

counter = 0
team_1_wins = 0
team_1_index = sim_functions.find_team_index(team_1, sim_functions.get_team_stats())

while counter < simulations:
    team_stats = sim_functions.get_team_stats()
    sim_functions.simulate_match(team_1, team_2, team_stats)

    if (team_stats[team_1_index]["wins"] >
            sim_functions.get_team_stats()[team_1_index]["wins"]):
        team_1_wins += 1
    counter += 1

print(f"{team_1} beat {team_2} {team_1_wins} out of {simulations} times, for a win probability of {team_1_wins / simulations * 100:.3f} %")
