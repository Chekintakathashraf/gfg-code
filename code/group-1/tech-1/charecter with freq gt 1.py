def find_duplicates(s):
    freq = {}
    
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    result = []
    added = set()  # to avoid adding same char again

    for char in s:
        if freq[char] > 1 and char not in added:
            result.append(char)
            added.add(char)

    return result


"""instead of set u can use dict , but it will get in the not order
Summary:
Question	Answer
Are dict keys unique?	✅ Yes
Can I loop through dict instead of string?	❌ Not if order matters
Why loop through string again?	✅ To preserve order + avoid re-adding"""