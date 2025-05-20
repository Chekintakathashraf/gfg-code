def unique_words(sentence):
    words = sentence.split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    result = []
    for word in words:
        if freq[word] == 1:
            result.append(word)

    return result

print(unique_words("this is a test this is only a test"))  # ['only']
print(unique_words("one two three four five"))             # ['one', 'two', 'three', 'four', 'five']
print(unique_words("hello hello world world hi"))          # ['hi']
