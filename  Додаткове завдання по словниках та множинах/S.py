n = int(input())
accents_dict = {}

for i in range(n):
    dict_word = input().strip()
    lowercase_word = dict_word.lower()

    if lowercase_word not in accents_dict:
        accents_dict[lowercase_word] = set()
    accents_dict[lowercase_word].add(dict_word)

peter_text = input().split()
errors_count = 0

for word in peter_text:
    uppercase_letters = 0
    for char in word:
        if char.isupper():
            uppercase_letters += 1

    if uppercase_letters != 1:
        errors_count += 1
        continue

    lowercase_word = word.lower()
    if lowercase_word in accents_dict:
        if word not in accents_dict[lowercase_word]:
            errors_count += 1

print(errors_count)