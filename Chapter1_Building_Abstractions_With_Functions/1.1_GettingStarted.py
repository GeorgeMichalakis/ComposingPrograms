"""
Statements and expressions.
Instructions:
Compute some value
Carry out some action

Statements typicall describe actions
Expression typically describe computations
"""
#Import statement
from urllib.request import urlopen
# assignment statement
shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')
"""Associates shakespear with the value of the expression that follows = 
The expression applies the urlopen function to a URL that contains the complete text

"""

"""
Functions encapsulate logic that manipulates data. urlopen is as function. Web address is piece of data

"""

words = set(shakespeare.read().decode().split())

"""
Associates the name words to the set of all unique words that apear in shakespares play.

Chain of command: read, decode and split

Interpreters: Evalating compound expression reqirues a precise procedurue that interprets code in a predictable way. A program that evaluuates compound expression -> interpreter

"""