my_file = open("input.txt", "r", encoding="utf-8")
text = my_file.read()
my_file.close()

words = text.split()
words_count = {}

for word in words:
    if word not in words_count:
        print(0, end=" ")
        words_count[word] = 1
    else:
        print(words_count[word], end=" ")
        words_count[word] += 1