text = input()
words = text.split()

word_frequency = {}
for word in words:
    if word not in word_frequency:
        word_frequency[word] = 1
    else:
        word_frequency[word] += 1

sorting_list = []
for word in word_frequency:
    count = word_frequency[word]
    sorting_list.append((-count, word))

sorting_list.sort()

for element in sorting_list:
    print(element[1])