import simfunctions

team_stats = simfunctions.get_team_stats()


overall_team_score = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

counter = 0

while counter < 1000:
    team_stats_sorted = simfunctions.simulate_season()

    for i in range(0, len(team_stats_sorted)):
        team_index = simfunctions.find_team_index(team_stats_sorted[i]["name"], team_stats)
        overall_team_score[team_index] += i + 1
    counter+=1
    print(f"counter: {counter}")

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

