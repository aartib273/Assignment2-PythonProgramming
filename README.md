# Assignment2-PythonProgramming
Game Mechanics: The game is a card game between two entities. The game can be played between two humans or a human and a machine. Choose a set of characters(fictional or real) and their characteristics. Characteristics are represented by a specific numeric value indicating the strength of the characteristic (strenghts may be indicated by negative or positive numeric value). Each card contains only one character and its characteristics.
Characteristics must be same across all characters but can vary in strength. No characteristic across characters can share the same value.
The two entities will be called Player 1 and Player 2 hence.
Distribute the cards equally among player 1 and player 2 face down such that the players cannot see the characters they have been given. Simulate a dice throw by both player 1 and player 2 where the highest number starts first
Constraints : Each player gets two special spells (God and Resurrect) . These spells are not associated to the characters but is assoicated to the player itself

Each round is played as below:
Player 1 : chooses the first card from the deck and can: play a charactertistic he wishes to challenge player 2 with . Player 2 chooses the first card in his deck and compares the charactertistic. The round is won by the Player whose characteristic weighs more and gets 1 point. The 2 cards are then kept faced down on a different deck called ‘outdated'(the cards go in the outdated deck in a random order). In round 2 , The player who won the previous round begins by choosing the next card in his deck and the round proceeds as above.

Spells:
In each round a player can decide to play the God spell or the Resurrect spell along with challenging with a characteristic. 

God Spell: After choosing the next card and characteristic on his deck, player 1 can play the God spell allowing the player to force a card number to be played by the Player 2. Player 1 can choose any card number he wants and player 2 should then compare the charactestic on the choosen card.

Resurrect Spell: Before choosing the next card and characteristic, player 1 can choose Resurrect spell. Choosing Resurrect will create a random number and the card at the that random number position from the ‘outdated’ deck will be choosen. The card present at the random number at the ‘outdated’ deck will be added back to the top of the player deck. The player must then play this card.
When Player 1 plays the God spell , Player 2 cannot play the God spell as he is forced to choose the card , however player 2 can play the Resurrect spell and add a new card to the top of his deck. Player 1 can then force the resurrected card to be choosen or can go with his earlier choice.

God and Resurrect spell can only be played once by each Player. The Game ends when all cards of one / both players have been played.
The game is won by the player with maximum points. 
