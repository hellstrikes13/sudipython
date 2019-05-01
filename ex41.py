import random
from urllib import urlopen
import sys
word_url = "http://learncodethehardway.org/words.txt"
words = []
phrases = {
"class %%%(%%%):":
 "make a class named %%% that is-a %%%",
 "class %%%(object):\n\tdef __init__(self, ***)" :
 "class %%% has-a __init__ that takes self and *** parameters.",
 "class %%%(object):\n\tdef ***(self, @@@)":
 "class %%% has-a function named *** that takes self and @@@ parameters.",
 "*** = %%%()":
 "Set *** to an instance of class %%%.",
 "***.***(@@@)":
 "From *** get the *** function, and call it with parameters self, @@@.",
 "***.*** = '***'":
 "From *** get the *** attribute and set it to '***'."
}
#do they wannna extract phrases 1st
phrase_first = False
if len(sys.argv) == 2 and sys.argv[1] == 'english':
 phrase_first = True

#load words from website
for word in urlopen(word_url).readline():
 words.append(word.strip())

def convert(snippet,phrase):
 class_names = [w.capitalize() for w in 
                random.sample(words,snippet.count("%%%"))]
 other_names = random.sample(words,snippet.count("***"))
 results = []
 param_names = []

 for i in range(0,snippet.count("@@@")):
  param_count = random.randint(1,3)
  param_names.append(', '.join(random.sample(words,param_count)))

 for sent in snippet , phrase:
  result = sentence[:]

 for word in class_names:
  result = result.replace("%%%",word,1)

 for word in other_names:
  result = result.replace("***",word , 1)

 for word in param_names:
  result = result.replace("@@@",word , 1)

 results.append(result)
 return results

try:
 while True:
  snippets = phrases.keys()
  random.shuffle(snippets)
 for s in snippets:
  phr = phrases[s]
  que , ans = convert(s,phr)
  if phrase_first:
   que , ans = ans , que
  print que
  raw_input("> ")
  print "answer %s\n\n" %ans
except EOFError:
 print 'looks like we have encounter end_of_file error.. good bye..'
