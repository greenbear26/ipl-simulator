import simfunctions

# Print final standings
for team in reversed(simfunctions.simulate_season()):
    print(f'{team["name"]} Points: {team["points"]} NRR: {team["nrr"]:.3f}')
