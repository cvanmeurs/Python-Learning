"""
# make the baby ask a question repeatedly until you say "just because"

answer = input("Why is the sky blue?: ").strip().lower()

while answer != "just because":
	answer = input("Why?: ").strip().lower()
"""

# same as above, but baby has a list of 3 questions to ask

from random import choice  # allows for choice() instead of random.choice() - loads specific function

questions = ["Why is the sky blue?",
	"Where do babies come from?",
	"Why is the US dollar no longer on the gold standard?"
]

question = choice(questions) # current question is one of the questions chosen at random

answer = input(question + ": ").strip().lower()

while answer != "just because":
	answer = input("Why?: ").strip().lower()

print("Oh. Okay.")