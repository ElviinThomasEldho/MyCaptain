import operator

word = input("Enter a word : ")

freq = {}

for i in word:
    if i in freq:
        freq[i] +=1
    else:
        freq[i] = 1

sorted_d = dict(sorted(freq.items(), key=operator.itemgetter(1),reverse=True))


print("Frequency of each character in ", word)
for k in sorted_d:
    print(k, " : ", sorted_d[k])


