import sim_functions

# Print final standings
for team in reversed(sim_functions.simulate_season()):
    print(f'{team["name"]} Points: {team["points"]} NRR: {team["nrr"]:.3f}')
