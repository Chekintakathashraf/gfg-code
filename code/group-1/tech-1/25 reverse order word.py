def reverse_each_word(s):
    words = s.strip().split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

print(reverse_each_word("Let's learn Python"))  # "s'teL nrael nohtyP"
print(reverse_each_word("hello world"))         # "olleh dlrow"
print(reverse_each_word("  welcome  home "))    # "emoclew emoh"
