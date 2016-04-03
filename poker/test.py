def main():

	def is_two (self, pokerHand):
		hand = self.hands[pokerHand]
		find_pair(hand)
		def find_pair (hand):
			if hand[0].rank == hand[1].rank:
				if hand[1].rank == hand[2].rank:
					return False
				else:
					return True
			else: 
				return find_pair(hand[1:])

main()