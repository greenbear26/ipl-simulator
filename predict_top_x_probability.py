import sim_functions
import sys

simulations = 100000

team = sys.argv[1] if len(sys.argv) > 1 else input("Which team? ")
if (any(team == teams["name"] for teams in sim_functions.get_team_stats())):
    print(f"Predicting playoff probability for {team}")
else:
    print(f"Invalid team, please select from {[teams["name"] for teams in
                                               sim_functions.get_team_stats()]}")
    exit()

x = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 4

counter = 0
playoffs_made = 0

while counter < simulations:
    team_stats = sim_functions.get_team_stats()
    team_stats_sorted = sim_functions.simulate_season()

    # Printing playoff teams
    # print([teams["name"] for teams in team_stats_sorted[10-x:10]])

    if any(team == teams["name"] for teams in team_stats_sorted[10-x:10]):
        playoffs_made += 1
    counter += 1

# Print final results
print(f"{team} made the top {x} {playoffs_made} out of {simulations} times, for a probability of {playoffs_made / simulations * 100:.3f} %")
print("If you would like a different amount of top teams, input a different number as the second argument")
