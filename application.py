from constants import PLAYERS, TEAMS
import sys



def menu():
	print("""BASKETBALL TEAM STATS TOOL

---- MENU----

 Here are your choices:
  1) Display Team Stats
  2) Quit

""")


response = int(input("Enter an option >  "))


def main():
	if response == 1:
		team = input("""
		1) Panthers
		2) Bandits
		3) Warriors
					""")
		if team == 1:
			print_panthers()
		elif team == 2:
			print_bandits()
		elif team == 3:
			print_warriors()
	print("Press ENTER to continue")
	if response == 2:
		sys.exit()



names = []

for i in PLAYERS:
	names.append(i['name'])

panthers = names[:6]
bandits = names[6:12]
warriors = names[12:18]


def print_panthers():
	for panther in panthers:
		print(panther, ',', end="")


def print_bandits():
	for bandit in bandits:
		print(bandit, ",", end="")


def print_warriors():
	for warrior in warriors:
		print(warrior, ",", end="")


if __name__ == "__main__":
	menu()

#
# names = []
# experienced = []
# unexperienced = []
#
#
# for i in PLAYERS:
#     names.append(i['name'])
#
# for i in PLAYERS:
#     if i['experience'] == "YES":
#         experienced.append(i)
#
# for i in PLAYERS:
#     if i['experience'] == "NO":
#         unexperienced.append(i)
#
# panthers = names[:6]
# bandits = names[6:12]
# warriors = names[12:18]
#
#
# def print_panthers():
#     for panther in panthers:
#         print(panther, ',', end="")
#
#
# def print_bandits():
#     for bandit in bandits:
#         print(bandit, ",", end="")
#
#
# def print_warriors():
#     for warrior in warriors:
#         print(warrior, ",", end="")
#
#
#
# newex = []
# unex = []
#
#
# for i in experienced:
#     newex.append(i['name'])
#
#
# for i in unexperienced:
#     unex.append(i['name'])
#
# print(newex)
# print(unex)
# my_panthers = newex[:3] + unex[:3]
# print(my_panthers)
# my_bandits = newex[3:6] + unex[3:6]
# print(my_bandits)
# my_warriors = newex[6:9] + unex[6:9]
# print(my_warriors)
