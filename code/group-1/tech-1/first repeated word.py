def first_repeated_word(sentence):
    words = sentence.split()
    seen = set()
    
    for word in words:
        if word in seen:
            return word
        seen.add(word)
        
    return None

print(first_repeated_word("this is a test this is only a test"))  # this
print(first_repeated_word("one two three four"))                  # None
print(first_repeated_word("he said he will come"))                # he

