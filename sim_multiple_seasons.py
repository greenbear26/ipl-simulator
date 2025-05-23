import sim_functions
import sys

print(f"Remaining matches: {sim_functions.REMAINING_SCHEDULE}")

simulations = int(
    sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else int(
        input("How many simulations? "))
print(f"{simulations} simulations")

overall_team_score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

counter = 0

while counter < simulations:
    team_stats = sim_functions.get_team_stats()
    team_stats_sorted = sim_functions.simulate_season()

    for i in range(0, len(team_stats_sorted)):
        team_index = sim_functions.find_team_index(
            team_stats_sorted[i]["name"], team_stats)
        overall_team_score[team_index] += i + 1
    counter += 1

# Print final results
team_stats = sim_functions.get_team_stats()

team_stats_sorted = sorted([(i, j)
                            for i, j in zip(team_stats, overall_team_score)],
                           key=lambda x: x[1])

print("Average Team Positioning")
for i in range(len(overall_team_score) - 1, -1, -1):
    team, score = team_stats_sorted[i]
    # print(f'{team["name"]} Total Standing: {score}')
    print(
        f'{team["name"]} Average Standing: {score/simulations}'
    )
