text = input()
words = text.split()

word_frequency = {}
for word in words:
    if word not in word_frequency:
        word_frequency[word] = 1
    else:
        word_frequency[word] += 1

most_frequent_word = ""
max_count = -1

for word in word_frequency:
    current_count = word_frequency[word]

    if current_count > max_count:
        max_count = current_count
        most_frequent_word = word
    elif current_count == max_count:
        if word < most_frequent_word:
            most_frequent_word = word

print(most_frequent_word)