""" 
Input: "this is a test this is only a test"
Output: "this"  # or "is" or "a" or "test" — they all appear twice

Input: "hello world hello"
Output: "hello"

Input: "one word only"
Output: "one"  # all words appear once, return first one

"""



def most_frequent_word(sentence):
    words = sentence.split()
    
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1

    max_count = 0
    result_word = ""

    for word in words:  # loop original list to preserve order
        if freq[word] > max_count:
            max_count = freq[word]
            result_word = word

    return result_word

print(most_frequent_word("this is a test this is only a test"))  # this or is or a or test
print(most_frequent_word("hello world hello"))                   # hello
print(most_frequent_word("apple orange banana"))                 # apple

