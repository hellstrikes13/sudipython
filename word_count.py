import sys
fn = sys.argv[1]
def word_count(filename):
  word_dict = {}
  filename = sys.argv[1]
  input_file = open(filename,'r')
  for lines in  input_file:
    words = lines.lower().split()
  #  print words
    for word in words:
        if word not in word_dict:
    	  word_dict[word] = 1
#	  print 'IF block ',word_dict
	else:
	  word_dict[word] = word_dict[word] + 1
#	  print 'Else block ',word_dict
#  print 'the final word count are:',word_dict
  return word_dict
  input_file.close()

def print_word(filename):
 words = word_count(filename)
 print 'keys:',words.keys() 
 print 'values',words.values()
 wc = sorted(words.keys())

 print '-----' * 10
 for i in wc:
  print i , words[i]
word_count(fn)
print_word(fn)

