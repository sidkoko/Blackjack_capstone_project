
import random
from art import logo
from replit import clear

deck = {
   "A" : 1,
   "2" : 2,
   "3" : 3,
   "4" : 4,
   "5" : 5,
   "6" : 6,
   "7" : 7,
   "8" : 8,
   "9" : 9,
   "10" : 10,
   "J" : 10,
   "Q" : 10,
   "K" : 10
}

cards = list(deck.values())

play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
if play_game == "y":
   
   clear()
   global balance
   balance = 1000
   bet_amount = 0
  
   
   game_start = True

   while game_start:
  
      print(f"\t\t\t\tYour balance is: ${balance}")
      print("\t\t\tHow much do you want to bet?")
      bet_amount = int(input())
      if bet_amount >  balance:
         print("You can't bet more than you have!")
         bet_amount = int(input())
      balance -= bet_amount
      clear()

     
         
      print(logo)
      print(f"At stake : {bet_amount}\n\n")
      dealer_hand = []
      player_hand = []
      player_score = 0
      dealer_score = 0
      
      def score(cards):
         return sum(cards)
      
      def deal_card():
         for card in deck:
            if len(player_hand) < 2:
               player_hand.append(random.choice(cards))
            if len(dealer_hand) < 2:
               dealer_hand.append(random.choice(cards))
      
         player_score = score(player_hand)
         print(f"Your hand is : {player_hand}, current score: {player_score}")
         
         dealer_score = score(dealer_hand)
         print(f"Dealer's hand is : {dealer_hand[0]}")
         compare()
         
      
      def hit():
         player_hand.append(random.choice(cards))
         player_score = score(player_hand)
         dealer_hand.append(random.choice(cards))
         dealer_score = score(dealer_hand)
         if player_score > 21:
            stand()
         else:
            print(f"Your hand is : {player_hand}, current score: {player_score}")
            compare()


      def compare():
         if player_score < 21:
            print("Would you like to hit or stand?")
            choice = input().lower()
            if choice == "hit":
               hit()
            elif choice == "stand":
               stand()
            else:
               print("Invalid input")
               clear()
               compare()
      
   
      def stand():

         global balance
         player_score = score(player_hand)
         dealer_score = score(dealer_hand)
         print(f"Your final hand is : {player_hand}, current score: {player_score}")
         print(f"Dealer's final hand is : {dealer_hand}, current score: {dealer_score}")
               
         if player_score > 21:
            print("You busted! Dealer wins!")
         elif dealer_score > 21:
            balance += (2*bet_amount)
            print("Dealer busted! You win!")
         elif player_score > dealer_score:
            balance += (2*bet_amount)
            print("You win!")
         elif player_score < dealer_score:
            print("Dealer wins!")
         elif player_score == dealer_score:
            balance += bet_amount
            print("It's a draw!")
         
      
      deal_card()

      if balance <= 0:
         print("You are out of money. Game over.")
         game_start = False
         break
         
      choice_2 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
      if choice_2 == "y":
         clear()
      elif choice_2 == "n":
         game_start = False
      