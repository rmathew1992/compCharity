from django.db import models

class User(models.Model):
	"""
	Each User has class variables, each which represents a database field in
	the model.

	Class Variables
	---------------
	username
	id
	bets = {bet1, bet2, ...}
	"""	
	def __str__(self):
		return self.username

	username = models.CharField(max_length=50)

class Challenge(models.Model):
	"""
	Challenges are created by challengers (a type of users) aimed at
	challengees (a type of user) who must fulfill the challenge.

	Each Challenge has class variables, each which represents a database field
	in the model.

	Class Variables
	---------------
	description: the description of the challenge
	bets: the Bets that have been pooled around this challenge.
	challengees: the users who have been challenged
	"""

	def __str__(self):
		return self.title

	title = models.CharField(default='', max_length=150)
	description = models.TextField()
	bets = models.ManyToManyField('Bet')
	challengees = models.ManyToManyField('User')

class Bet(models.Model):
	"""
	Bets are fundamentally controlled by the individual user making the bet.

	Each Bet has class variables, each which represents a database field in the
	model.

	Class Variables
	---------------
	user: foreign key connecting the user who has put money into this bet
	amount: dollar value of the bet
	challenge: the challenge this bet is associated with
	?charity: charity that this bet will be going to.
	"""

	def __str__(self):
		return str(self.user) + str(self.amount)

	user = models.ForeignKey('User')
	amount = models.FloatField(default=0.15)