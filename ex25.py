def break_words(stuff):
#this function breaks words for us"""
  words = stuff.split(' ')
  return words

def sort_words(words):
 # sort the words
  return sorted(words)

def print_first_word(words):
# print first word
  word = words.pop(0)
  print word

def print_last_word(words):
# print last word
  word = words.pop(-1)
  print word

def sort_sentence(sentence):
 """
 this is to sort
 sentence
 """
#take a full sentence and return the sorted words
 words = break_words(sentence)
 return sort_words(words)

def print_first_and_last_sentence(sentence):
#print 1st and last words of sentence
   words = break_words(sentence)
   print_first_word(words)
   print_last_word(words)


def print_first_and_last_sorted(sentence):
#print 1st and last words of sentence
   words = sort_sentence(sentence)
   print_first_word(words)
   print_last_word(words)
 
