# Qns: Game Player Ranking System

# You are given a text file called players.txt.
# Each line contains a player's name and their score, separated by a space.

# Example:
# Alex 920
# Ben 430
# Clara 780

# Your task:

# 1. Read the data from players.txt.

# 2. Convert the data into a dictionary called player_scores.
#    The name should be the key.
#    The score should be the value.

# 3. Create TWO new dictionaries:
#    - high_score_players
#    - low_score_players

# 4. Loop through player_scores.
#    If the player scored 500 or above, store them in high_score_players.
#    Otherwise, store them in low_score_players.

# 5. From the high_score_players dictionary, calculate:

# Definitions:
# - Elite Players: 900 and above
# - 50 points away from Elite: 850 to 899
# - 100 points away from Elite: 800 to 849
# - 150 points away from Elite: 750 to 799

# 6. Write the summary into a file called leaderboard_summary.txt.

# The output file should contain:

# Total number of players:
# Total number of low score players:
# Total number of high score players:
# Total number of elite players:
# Total number of 50 points away from elite:
# Total number of 100 points away from elite:
# Total number of 150 points away from elite:
