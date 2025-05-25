s = "hello world"

word = s.strip().split()

reversed_word =[ x[::-1] for x in word ]

a = " ".join(reversed_word)

print(a)