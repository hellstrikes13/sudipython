punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
def remove_punc(st):
 print st
 st_free_punc = ""
 for letter in st:
   if letter not in punctuation:
     st_free_punc = st_free_punc + letter
 return st_free_punc
s = remove_punc("sudee{\?}--p")
print s
  
