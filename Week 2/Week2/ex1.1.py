def match_words(words):
    count = 0
    for word in words:
        if(len(word) > 1 and word[0] == word[-1]):
            count += 1
    return count

print(match_words(["abc", "xyz", "aba", "1221"]))
