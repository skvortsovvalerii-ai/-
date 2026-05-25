my_file = open("input.txt", "r", encoding="utf-8")
text = my_file.read()
my_file.close()

words_list = text.split()

unique_words = set(words_list)

print(len(unique_words))