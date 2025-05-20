def group_anagrams(words):
    groups = {}

    for word in words:
        key = ''.join(sorted(word))  # sort the word to get its "signature"
        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

