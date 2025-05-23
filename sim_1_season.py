import sim_functions

print(f"Remaining matches: {sim_functions.REMAINING_SCHEDULE}")

# Print final standings
for team in reversed(sim_functions.simulate_season()):
    print(f'{team["name"]} Points: {team["points"]} NRR: {team["nrr"]:.3f}')
