from constants import PLAYERS
import sys


def main(team):
	print("""BASKETBALL TEAM STATS TOOL
	---- MENU----
	Here are your choices:
	1) Display Team Stats
	2) Quit
	""")

	response = int(input("Enter an option >  "))
	if response == 1:
		team = int(input("""
1) Panthers
2) Bandits
3) Warriors
					"""))
		if team == 1:
			print_players(my_panthers)

		elif team == 2:
			print_players(my_bandits)

		elif team == 3:
			print_players(my_warriors)

	elif response == 2:
		sys.exit()
	return team


names = []
experienced_dict = []
unexperienced_dict = []


for i in PLAYERS:
	if i['experience'] == "YES":
		experienced_dict.append(i)
	elif i['experience'] == "NO":
		unexperienced_dict.append(i)
	names.append(i['name'])


experienced_players = []
unexperienced_players = []


for i in experienced_dict:
	experienced_players.append(i['name'])


for i in unexperienced_dict:
	unexperienced_players.append(i['name'])


my_panthers = experienced_players[:3] + unexperienced_players[:3]
my_bandits = experienced_players[3:6] + unexperienced_players[3:6]
my_warriors = experienced_players[6:9] + unexperienced_players[6:9]


def print_players(team):
	print("""
	Team: {}
	--------------------
	Total players: 6""")

	print("Players on Team:\n")
	for player in team:
		print(player, end=", ")


if __name__ == '__main__':
	main(team=None)
