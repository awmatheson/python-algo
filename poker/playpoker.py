#  File: playpoker.py
#  Description: A program simulating a five card draw poker game
#  Student's Name: Alexander Matheson
#  Student's UT EID: awm852
#  Course Name: CS 313E 
#  Unique Number: 50597
#
#  Date Created: 09/20/2015
#  Date Last Modified: 09/25/2015

#import the random number generator for card deck
import random
import operator

class Card (object):
	#define the sequence of ranks and suits
	RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

	SUITS = ('C', 'H', 'S', 'D')

	def __init__ (self, rank, suit):
		self.rank = rank
		self.suit = suit

	#return a string when requested
	def __str__ (self):
	# print J, Q, K, A instead of 11, 12, 13, 14
		if self.rank == 14:
			rank = 'A'
		elif self.rank == 13:
			rank = 'K'
		elif self.rank == 12:
			rank = 'Q'
		elif self.rank == 11:
			rank = 'J'
		else:
			rank = self.rank

		return str(rank) + self.suit

  #methods defined to use operators easily
	def __eq__ (self, other):
		return (self.rank == other.rank)

	def __ne__ (self, other):
		return (self.rank != other.rank)

	def __lt__ (self, other):
		return (self.rank < other.rank)

	def __le__ (self, other):
		return (self.rank <= other.rank)

	def __gt__ (self, other):
		return (self.rank > other.rank)

	def __ge__ (self, other):
		return (self.rank >= other.rank)

class Deck (object):
	
	def __init__ (self):
		#make a deck of cards
		self.deck = []
		for suit in Card.SUITS:
			for rank in Card.RANKS:
				card = Card (rank, suit)
				self.deck.append (card)

	#shuffle the deck with random package shuffle
	def shuffle (self):
		random.shuffle (self.deck)

	#deal the cards 1 at a time popping the top card off the list
	def deal (self):
		if len(self.deck) == 0:
			return None
		else:
			return self.deck.pop(0)

class Poker (object):
	#create a deck and shuffle it
	def __init__ (self, numHands):
		self.deck = Deck()
		self.deck.shuffle()
		self.hands = []
		numCards_in_Hand = 5

		for i in range (numHands):
			hand = []
			for j in range (numCards_in_Hand):
				hand.append (self.deck.deal())
			self.hands.append (hand)

	def play (self):
		#make a list to print at the end that will contain hand values
		print_hands = []

		#make a dictionary that will contain hand and hand value as key pair
		totalHandValues = {}

		#print poker hands individually as strings
		print("")
		for pokerHand in range (len(self.hands)):
			# sort the hands for comparison
			sortedHand = sorted (self.hands[pokerHand], reverse = True)
			hand = ''
			for card in sortedHand:
				hand = hand + str(card) + ' '
			print ('Hand ' + str(pokerHand + 1) + ': ' + hand)

			# Assign the sortedHand to a variable that we will use
			# to check what the hand is and its value
			handToCheck = sortedHand

			#call functions to check what the hand is (royal flush, straight, pair etc.)
			if(self.is_royal_flush(handToCheck) == True):
				handValue = 10
				print_hands.append('Hand ' + str(pokerHand + 1) + ': Royal Flush')

			elif(self.is_straight_flush(handToCheck) == True):
				handValue = 9
				print_hands.append('Hand ' + str(pokerHand + 1) + ': Straight Flush')

			elif(self.is_four(handToCheck) == True):
				handValue = 8
				print_hands.append('Hand ' + str(pokerHand + 1) + ': Four of a Kind')

			elif(self.is_full(handToCheck) == True):
				handValue = 7
				print_hands.append('Hand ' + str(pokerHand + 1) + ': Fullhouse')

			elif(self.is_flush(handToCheck) == True):
				handValue = 6
				print_hands.append('Hand ' + str(pokerHand + 1) + ': Flush')

			elif(self.is_straight(handToCheck) == True):
				handValue = 5
				print_hands.append('Hand ' + str(pokerHand + 1) + ': Straight')

			elif(self.is_three(handToCheck) == True):
				handValue = 4
				print_hands.append('Hand ' + str(pokerHand + 1) + ': Three Pair')

			elif(self.is_two(handToCheck) == True):
				handValue = 3
				print_hands.append('Hand ' + str(pokerHand + 1) + ': Two Pair')

			elif(self.is_one(handToCheck) == True):
				handValue = 2
				print_hands.append('Hand ' + str(pokerHand + 1) + ': One Pair')

			elif(self.is_high(handToCheck) == True):
				handValue = 1
				print_hands.append('Hand ' + str(pokerHand + 1) + ': High Card')

			total_points = (handValue * 13**5 + handToCheck[0].rank * 13**4 + handToCheck[1].rank * 13**3 
				+ handToCheck[2].rank * 13**2 + handToCheck[3].rank * 13 + handToCheck[4].rank)

			totalHandValues["Hand "+ str(pokerHand + 1)] = total_points

		# Print out the poker hands as flush, straight etc.
		print("")
		for pokerHand in range (len(self.hands)):
			print(print_hands[pokerHand])

		print("")

		#check for a tie and print out hands that tie. If no tie, print winner
		sortedHandValues = sorted(totalHandValues.values(), reverse = True)
		if (sortedHandValues[0] == sortedHandValues[1]):
			if (sortedHandValues[0] == sortedHandValues[1] == sortedHandValues[2]):
				if (sortedHandValues[0] == sortedHandValues[1] == sortedHandValues[2] == sortedHandValues[3]):
					for hand, totalValue in totalHandValues.items():
						if totalValue == sortedHandValues[0]:
							print(hand + " ties.")
				else:
					for hand, totalValue in totalHandValues.items():
						if totalValue == sortedHandValues[0]:
							print(hand + " ties.")
			for hand, totalValue in totalHandValues.items():
				if totalValue == sortedHandValues[0]:
					print(hand + " ties.")
		else:
			for hand, totalValue in totalHandValues.items():
				if totalValue == sortedHandValues[0]:
					print(hand + " wins.")

	#royal flush
	def is_royal_flush(self,handToCheck):
		sumHand = 0
		suitCheck = handToCheck[0].suit
		countSuit = 0
		for card in range(5):
			sumHand = sumHand + handToCheck[card].rank
			if (handToCheck[card].suit == suitCheck):
				countSuit += 1
		if (sumHand == 60 and countSuit > 4): 
			return True
		else:
			return False

	#straight flush
	def is_straight_flush (self, handToCheck):
		suitCheck = handToCheck[0].suit
		cardRank = handToCheck[0].rank
		countRank = 0
		countSuit = 0
		for card in range(5):
			if (handToCheck[card].suit == suitCheck and handToCheck[card].rank == cardRank):
				countSuit += 1
				countRank += 1
				cardRank -= 1
		if (countRank > 4 and countSuit > 4): 
			return True
		else:
			return False

	#four of a kind
	def is_four (self, handToCheck):
		if(handToCheck[0].rank == handToCheck[1].rank == 
			handToCheck[2].rank == handToCheck[3].rank):
			return True
		elif(handToCheck[1].rank == handToCheck[2].rank == 
			handToCheck[3].rank == handToCheck[4].rank):
			return True
		else:
			return False

	#fullhouse
	def is_full (self, handToCheck):
		if(handToCheck[0].rank == handToCheck[1].rank and  
			handToCheck[2].rank == handToCheck[3].rank == handToCheck[4].rank):
			return True
		elif(handToCheck[3].rank == handToCheck[4].rank and  
			handToCheck[0].rank == handToCheck[1].rank == handToCheck[2].rank):
			return True
		else:
			return False

	#flush
	def is_flush (self, handToCheck):
		if(handToCheck[0].suit == handToCheck[1].suit == handToCheck[2].suit == 
			handToCheck[3].suit == handToCheck[4].suit):
			return True
		else:
			return False

	#straight
	def is_straight (self, handToCheck):
		cardRank = handToCheck[0].rank
		countRank = 0
		for card in range(5):
			if (handToCheck[card].rank == cardRank):
				countRank += 1
				cardRank -= 1
		if (countRank > 4): 
			return True
		else:
			return False

	#three of a kind
	def is_three (self, handToCheck):
		if(handToCheck[0].rank == handToCheck[1].rank == handToCheck[2].rank):
			return True
		elif(handToCheck[1].rank == handToCheck[2].rank == handToCheck[3].rank):
			return True
		elif(handToCheck[2].rank == handToCheck[3].rank == handToCheck[4].rank):
			return True
		else:
			return False

	#two pair
	def is_two (self, handToCheck):
		if(handToCheck[0].rank == handToCheck[1].rank and handToCheck[2].rank == handToCheck[3].rank):
			return True
		if(handToCheck[0].rank == handToCheck[1].rank and handToCheck[3].rank == handToCheck[4].rank):
			return True
		elif(handToCheck[1].rank == handToCheck[2].rank and handToCheck[3].rank == handToCheck[4].rank):
			return True
		else:
			return False

	#one pair
	def is_one (self, handToCheck):
		if(handToCheck[0].rank == handToCheck[1].rank):
			return True
		elif(handToCheck[1].rank == handToCheck[2].rank):
			return True
		elif(handToCheck[2].rank == handToCheck[3].rank):
			return True
		elif(handToCheck[3].rank == handToCheck[4].rank):
			return True
		else:
			return False

	#high card
	def is_high (self, handToCheck):
		return True


def main():
	#request user input for hands to play
	numHands = int (input ('Enter number of hands to play: '))

	# need at least 2 players but no more than 6
	while (numHands < 2 or numHands > 6):
		numHands = int (input ('Enter number of hands to play: '))

	# create a Poker object:  create a deck, shuffle it, and
	# deal out the cards
	game = Poker(numHands)

	# play the game
	game.play()

main()

