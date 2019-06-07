from enum import Enum
from enum import IntEnum
import random

def diceRoll():
    player = random.randint(1, 6)
    return player

def main():
    ressurect_spell_player1 = False
    ressurect_spell_player2 = False
    god_spell_player1 = False
    god_spell_player2 = False
    player1_wins = 0
    player2_wins = 0

    characters = list()

    Raechal_Green = {
        "Name": "Raechal_Green",
        "Humor": 5,
        "Intelligence": 7,
        "Spontanity": 8,
        "Financial_status": 9,
        "Spiritual": 4,
        "Geek": 4
    }
    characters.append(Raechal_Green)

    Joey_Tribianni = {
        "Name": "Joey_Tribianni",
        "Humor": 8,
        "Intelligence": 6,
        "Spontanity": 9,
        "Financial_status": 9,
        "Spiritual": 2,
        "Geek": 1
    }
    characters.append(Joey_Tribianni)

    Chandler_Bing = {
        "Name": "Chandler_Bing",
        "Humor": 9,
        "Intelligence": 9,
        "Spontanity": 10,
        "Financial_status": 10,
        "Spiritual": 1,
        "Geek": 7
    }
    characters.append(Chandler_Bing)

    Monika_Geller = {
        "Name": "Monika_Geller",
        "Humor": 7,
        "Intelligence": 8,
        "Spontanity": 7,
        "Financial_status": 8,
        "Spiritual": 5,
        "Geek": 6
    }
    characters.append(Monika_Geller)

    Ross_Geller = {
        "Name": "Ross_Geller",
        "Humor": 7,
        "Intelligence": 8,
        "Spontanity": 9,
        "Financial_status": 9,
        "Spiritual": 6,
        "Geek": 10
    }
    characters.append(Ross_Geller)

    Pheobe_Buffay = {
        "Name": "Pheobe_Buffay",
        "Humor": 6,
        "Intelligence": 7,
        "Spontanity": 8,
        "Financial_status": 7,
        "Spiritual": 10,
        "Geek": 1
    }
    characters.append(Pheobe_Buffay)

    player1_cards = list()
    player2_cards = list()
    old_cards = list()

    random.shuffle(characters)
    player1_cards = characters[0:int(len(characters)/2)]
    player2_cards = characters[int((len(characters)/2)):len(characters)]



    while len(player1_cards) > 0 and len(player2_cards) > 0:
        choice_made = False
        player1 = diceRoll()
        player2 = diceRoll()
        # player1 = 4
        # player2 = 2
        if player1 > player2:

            print("Player 1 card")
            card1 = player1_cards[len(player1_cards)-1]

            print(card1)
            if not ressurect_spell_player1  and not god_spell_player1 and not choice_made:
                print("Do you want to play Gods spell/Reserruct spell? \n1.God Spell\n2.Resurrect Spell\n3.Use nothing")
                choice = input()
                choice_made = True
                if choice == '1':
                    god_spell_player1 = True

                    print("Enter a number between 0-" + str(len(player2_cards)-1))
                    selected_no = input()
                    if int(selected_no) < len(player2_cards):
                        card2 = player2_cards[int(selected_no)]

                elif choice == '2':
                    ressurect_spell_player1 = True
                    if len(old_cards) > 1:
                        print("Card chosen from old deck")
                        select = random.randint(0, len(old_cards)-1)
                        card2 = old_cards[select]
                        old_cards.remove(card2)
                    elif len(old_cards) == 1:
                        print("Card chosen from old deck")
                        select = 0
                        card2 = old_cards[select]
                    else:
                        print("Card chosen from current deck as old deck is empty")
                        ressurect_spell_player1 = False

                        card2 = player2_cards[len(player2_cards) - 1]

                else:
                    card2 = player2_cards[len(player2_cards) - 1]

            if not ressurect_spell_player1 and not choice_made:

                print("Do you want to play Reserruct spell? \n1.yes\n2.No")
                choice = input()
                choice_made = True
                if choice == '1':
                    ressurect_spell_player1 = True
                    if len(old_cards) > 1:
                        print("Card chosen from old deck")
                        select = random.randint(0, len(old_cards)-1)
                        card2 = old_cards[select]
                        old_cards.remove(card2)
                    elif len(old_cards) == 1:
                        print("Card chosen from old deck")
                        select = 0
                        card2 = old_cards[select]
                        old_cards.remove(card2)
                    else:
                        print("Card chosen from current deck as old deck is empty")
                        card2 = player2_cards[len(player2_cards) - 1]
                        ressurect_spell_player1 = False
                else:
                    ressurect_spell_player1 = False
                    card2 = player2_cards[len(player2_cards) - 1]
            if not god_spell_player1 and not choice_made:
                print("Do you want to play God's  spell? \n1.yes\n2.No")
                choice = input()
                choice_made = True
                if choice == '1':
                    god_spell_player1 = True
                    print("Enter a number between 0-" + str(len(player2_cards) - 1))
                    selected_no = input()
                    if int(selected_no) < len(player2_cards):
                        card2 = player2_cards[int(selected_no)]
                else:
                    god_spell_player1 = False
                    card2 = player2_cards[len(player2_cards) - 1]


            print("Pick a characteristic from [Humor,Intelligence,Financial_status,Spiritual,Geek] : ")
            property = input()
            if property in card1 and property in card2:

                value1 = card1[property]
                value2 = card2[property]
                if(value1 > value2):
                    print("Player 1 wins")
                    player1_wins = player1_wins + 1
                elif(value2 > value1):
                    print("Player 2 wins")
                    player2_wins = player2_wins + 1
                else:
                    print("Draw!! Play Again")
                print("Card of player 2")
                print(card2)
                old_cards.append(card1)
                old_cards.append(card2)
                if card1 in player1_cards:
                    player1_cards.remove(card1)
                if card2 in player2_cards:
                    player2_cards.remove(card2)
            else:
                print("Invalid Characteristic")

        elif player2 > player1:

            print("Player 2 card")
            card2 = player2_cards[len(player2_cards) - 1]

            print(card2)
            if not ressurect_spell_player2 and not god_spell_player2 and not choice_made:
                print("Do you want to play Gods spell/Reserruct spell? \n1.God Spell\n2.Resurrect Spell\n3.Use nothing")
                choice = input()
                choice_made = True
                if choice == '1':
                    god_spell_player2 = True

                    print("Enter a number between 0-" + str(len(player1_cards) - 1))
                    selected_no = input()
                    if int(selected_no) < len(player1_cards):
                        card1 = player1_cards[int(selected_no)]

                elif choice == '2':
                    ressurect_spell_player2 = True
                    if len(old_cards) > 1:
                        print("Card chosen from old deck")
                        select = random.randint(0, len(old_cards) - 1)
                        card1 = old_cards[select]
                        old_cards.remove(card1)
                    elif len(old_cards) == 1:
                        print("Card chosen from old deck")
                        select = 0
                        card1 = old_cards[select]
                    else:
                        print("Card chosen from current deck as old deck is empty")
                        ressurect_spell_player1 = False

                        card1 = player1_cards[len(player1_cards) - 1]

                else:
                    card1 = player1_cards[len(player1_cards) - 1]

            if not ressurect_spell_player2 and not choice_made:

                print("Do you want to play Reserruct spell? \n1.yes\n2.No")
                choice = input()
                choice_made = True
                if choice == '1':
                    ressurect_spell_player2 = True
                    if len(old_cards) > 1:
                        print("Card chosen from old deck")
                        select = random.randint(0, len(old_cards) - 1)
                        card1 = old_cards[select]
                        old_cards.remove(card1)
                    elif len(old_cards) == 1:
                        print("Card chosen from old deck")
                        select = 0
                        card1 = old_cards[select]
                        old_cards.remove(card1)
                    else:
                        print("Card chosen from current deck as old deck is empty")
                        card1 = player1_cards[len(player1_cards) - 1]
                        ressurect_spell_player2 = False
                else:
                    ressurect_spell_player2 = False
                    card1 = player1_cards[len(player1_cards) - 1]
            if not god_spell_player2 and not choice_made:
                print("Do you want to play God's  spell? \n1.yes\n2.No")
                choice = input()
                choice_made = True
                if choice == '1':
                    god_spell_player2 = True
                    print("Enter a number between 0-" + str(len(player1_cards) - 1))
                    selected_no = input()
                    if int(selected_no) < len(player1_cards):
                        card1 = player1_cards[int(selected_no)]
                else:
                    god_spell_player2 = False
                    card1 = player1_cards[len(player1_cards) - 1]

            print("Pick a characteristic from [Humor,Intelligence,Financial_status,Spiritual,Geek] : ")
            property = input()
            if property in card1 and property in card2:

                value1 = card1[property]
                value2 = card2[property]
                if (value1 > value2):
                    print("Player 1 wins")
                    player1_wins = player1_wins + 1
                elif (value2 > value1):
                    print("Player 2 wins")
                    player2_wins = player2_wins + 1
                else:
                    print("Draw!! Play Again")
                print("Card of player 1")
                print(card1)
                old_cards.append(card1)
                old_cards.append(card2)
                if card1 in player1_cards:
                    player1_cards.remove(card1)
                if card2 in player2_cards:
                    player2_cards.remove(card2)
            else:
                print("Invalid Characteristic")
        print("\n-----------------------------------------\n")

    print("Total Wins Player 1 : " + str(player1_wins))
    print("Total Wins Player 2 : " + str(player2_wins))
    if player1_wins > player2_wins:
        print("Ultimate winner is player 1 ")
    elif player1_wins < player2_wins:
        print("Ultimate winner is player 2 ")
    else:
        print("It's a tie")
main()




