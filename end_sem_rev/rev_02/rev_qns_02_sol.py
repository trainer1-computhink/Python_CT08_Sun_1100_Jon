# =========================
# Game Player Ranking System Solution
# =========================

import os

folder = os.getcwd()

player_scores = {}
high_score_players = {}
low_score_players = {}

elite_count = 0
fifty_away_count = 0
hundred_away_count = 0
hundred_fifty_away_count = 0

# =========================
# Step 1 & 2: Read file and build dictionary
# =========================
file_name = "players.txt"

full_path = os.path.join(folder, file_name)
with open(full_path, "r") as file:
    for line in file:
        parts = line.strip().split()

        name = parts[0]
        score = int(parts[1])

        player_scores[name] = score

# =========================
# Step 3 & 4: Split into high and low score players
# =========================

for name in player_scores:
    score = player_scores[name]

    if score >= 500:
        high_score_players[name] = score
    else:
        low_score_players[name] = score

# =========================
# Step 5: Count categories
# =========================

for name in high_score_players:
    score = high_score_players[name]

    if score >= 900:
        elite_count += 1
    elif score >= 850:
        fifty_away_count += 1
    elif score >= 800:
        hundred_away_count += 1
    elif score >= 750:
        hundred_fifty_away_count += 1

# =========================
# Step 6: Write to output file
# =========================

output_file_name = "ldr_board_summary.txt"
output_full_path = os.path.join(folder, output_file_name)
with open(output_file_name, "w") as file:
    file.write("Total number of players: " + str(len(player_scores)) + "\n")
    file.write("Total number of low score players: " + str(len(low_score_players)) + "\n")
    file.write("Total number of high score players: " + str(len(high_score_players)) + "\n")
    file.write("Total number of elite players: " + str(elite_count) + "\n")
    file.write("Total number of 50 points away from elite: " + str(fifty_away_count) + "\n")
    file.write("Total number of 100 points away from elite: " + str(hundred_away_count) + "\n")
    file.write("Total number of 150 points away from elite: " + str(hundred_fifty_away_count) + "\n")

print("leaderboard_summary.txt has been created.")
