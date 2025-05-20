def words_appearing_twice(sentence):
    words = sentence.split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    result = []
    for word in words:
        if freq[word] == 2 and word not in result:
            result.append(word)

    return result

print(words_appearing_twice("this is a test this is only a test"))  # ['this', 'is', 'a', 'test']
print(words_appearing_twice("apple banana orange apple banana mango"))  # ['apple', 'banana']
print(words_appearing_twice("one two three one two three one"))  # ['two', 'three']

"""Summary:

    Approach 1 is simpler and good when you just want the first word with the second highest frequency in original order.

    Approach 2 is more flexible if you want to sort and process words more carefully, e.g., for tie-breaks."""