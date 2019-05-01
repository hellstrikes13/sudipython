word_list = ['cat','dog','rabbit']
letterlist = { }
for a_word in word_list:
    for a_letter in a_word:
        letterlist[a_letter] = 1
        
lst = letterlist.keys()
print sorted(lst)
