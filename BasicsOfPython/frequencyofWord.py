sentence = "When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change"
wordcount = {}
for word in sentence.split():
    wordcount[word] = wordcount.get(word, 0) + 1
print (wordcount)