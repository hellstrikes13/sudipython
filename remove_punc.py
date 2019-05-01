import string
def remove_punc(st):
 print 'original string:',st
 st_free_punc = ""
 for letter in st:
   if letter not in string.punctuation:
     st_free_punc = st_free_punc + letter
 return st_free_punc
s = remove_punc("sudee{\?}--p")
print 'clean string:',s
  
