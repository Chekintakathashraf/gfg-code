def count_vowels_consonants(s):
    vowels = set('aeiouAEIOU')
    vowel_count = 0
    consonant_count = 0
    
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
                
    return vowel_count, consonant_count

v, c = count_vowels_consonants("hello")
print(f"Vowels = {v}, Consonants = {c}")  # Vowels = 2, Consonants = 3

v, c = count_vowels_consonants("Python")
print(f"Vowels = {v}, Consonants = {c}")  # Vowels = 1, Consonants = 5
