def text_to_words(txt):
 '''
 return a list of words with all punctuations removed
 and all in lowercase
 '''
 my_subs = txt.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_‘{|}~’"abcdefghijklmnopqrstuvwxyz)
 clean_text = txt.translate(my_subs)
 print clean_text
 wds = clean_text.split()
 return wds

def get_words_in_book(filename):
""" Read a book from filename, and return a list of its words. """
 f = open(filename, "r")
 content = f.read()
 f.close()
 wds = text_to_words(content)
 return wds
 book_words = get_words_in_book('alice_in_wonderland.txt')
 print "there are %d words in vocab file, starting with \n %s"%(len(words),words[:100])
