def count_duplicate_words(sentence):
    words = sentence.split()
    freq = {}
    
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    count = 0
    for word in freq:
        if freq[word] > 1:
            count += 1

    return count

print(count_duplicate_words("this is a test this is only a test"))  # 4
print(count_duplicate_words("apple banana mango orange apple mango"))  # 2
print(count_duplicate_words("one two three"))  # 0

