n = int(input())
synonyms_dict = {}

for i in range(n):
    pair = input().split()
    word1 = pair[0]
    word2 = pair[1]

    synonyms_dict[word1] = word2
    synonyms_dict[word2] = word1

search_word = input()
print(synonyms_dict[search_word])