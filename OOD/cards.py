import random

class Card:
	def __init__(self, suite, value):
		self.suite = suite
		self.value = value


class Deck:
	def __init__(self):
		self.cardDeck = []
		for val in range(1, 14):
			for sui in ['Spade', 'Club', 'Diamond', 'Heart']:
				cardDeck.append(Card(sui, val))

	def shuffle(self):
		for i in range(len(self.cardDeck)):
			ran = random.randint(len(self.cardDeck))
			self.cardDeck[i], self.cardDeck[ran] = self.cardDeck[ran], self.cardDeck[i]

	def getCardByIndex(self, index):
		return self.cardDeck.pop(index)

	def getRandomCard(self):
		ran = random.randint(len(self.cardDeck))
		return self.getCardByIndex(ran)
	
	def insertCardToIndex(self, card, index):
		self.cardDeck.insert(index, card)

	def getCardNumber(self):
		return len(self.cardDeck)

	def getCardDeck(self):
		return cardDeck


class Player:
	def __init__(self):
		self.score = 0
		self.cards = []

	def getRandomCardFromDeck(self, deck, num):
		for i in range(num):
			if deck.getCardNumber() > 0:
				self.cards.append(deck.getRandomCard())
			else:
				break

	def getCardFromTop(self, deck, num):
		for i in range(num):
			if deck.getCardNumber() > 0:
				self.cards.append(deck.getCardFromTop())
			else:
				break
	
	def putAllCardsBack(self, deck):
		for card in self.cards:
			deck.insertCardToIndex(card, 0)
		self.cards = []
		deck.shuffle()





