def load_words(filename):
 f = open(filename,'r')
 content = f.read()
 f.close()
 wds = content.split()
 return wds
words = load_words("vocab.txt")
print "there are %d words in vocab file, starting with \n %s"%(len(words),words[:6])
