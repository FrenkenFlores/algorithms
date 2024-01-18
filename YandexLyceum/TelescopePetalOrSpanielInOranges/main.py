import sys
words = []
sub_words = [s.replace('\n', '') for s in sys.stdin.readlines()]
word = sub_words.pop(0)
for sub_word in sub_words:
    if set(sub_word).issubset(set(word)):
        for c in sub_word:
            if sub_word.count(c) > word.count(c):
                break
        else:
            words.append(sub_word)
print(len(words))
for w in words:
    print(w)