from constants import *
import sys
from copy import deepcopy


def main():
	while True:
		print("""BASKETBALL TEAM STATS TOOL
		---- MENU----
		Here are your choices:
		1) Display Team Stats
		2) Quit
		""")
		response = input("Enter an option >  ")
		if response == "1":
			team = input("""
		1) Panthers
		2) Bandits
		3) Warriors
							""")
			if team == "1":
				print_players(my_panthers, TEAMS[0])

			elif team == "2":
				print_players(my_bandits, TEAMS[1])

			elif team == "3":
				print_players(my_warriors, TEAMS[2])

			else:
				print("Please enter a valid response ")
				continue

		elif response == "2":
			sys.exit()

		else:
			print("enter a valid response ")
			continue

		return team


data_to_work_with = deepcopy(PLAYERS)


def sort_players():
	names = []
	experienced_dict = []
	inexperienced_dict = []
	for i in data_to_work_with:
		if i['experience'] == "YES":
			i['experience'] = True
			experienced_dict.append(i['name'])
		elif i['experience'] == "NO":
			i['experience'] = False
			inexperienced_dict.append(i['name'])
		i['height'] = i['height'].split()
		i['height'] = int(i['height'][0])
		names.append(i['name'])

	return experienced_dict, inexperienced_dict


experienced_dict, inexperienced_dict = sort_players()


def create_team():
    my_panthers = experienced_dict[:3] + inexperienced_dict[:3]
    my_bandits = experienced_dict[3:6] + inexperienced_dict[3:6]
    my_warriors = experienced_dict[6:9] + inexperienced_dict[6:9]
    return my_panthers, my_bandits, my_warriors


my_panthers, my_bandits, my_warriors = create_team()


def print_players(team, string):
	print("""   Team {}
	--------------------
	Total players: {}""".format(string, len(team)))

	print("Players on Team:\n")
	print(", ".join(team))


if __name__ == '__main__':
	main()