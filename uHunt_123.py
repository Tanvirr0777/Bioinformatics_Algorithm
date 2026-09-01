
fr = open("input.txt","r")
fw = open("output.txt","w")


flag_sen = False

ignor_word = set()
sen = []
arr = []

for l in fr:
    line = l.strip()

    if line != "::" and flag_sen == False:
        ignor_word.add(line.lower())

    if line == "::":
        flag_sen = True
        continue

    if flag_sen:
        sentence = line.lower()
        sen.append(sentence)


for sentence in sen:
    words = sentence.split()

    for i, word in enumerate(words):
        if word not in ignor_word:
            temp = words.copy()
            temp[i] = word.upper()

            arr.append((word.upper(), " ".join(temp)))


arr.sort(key=lambda x: x[0])

for title in arr:
    print(title[1])
    fw.write(str(title[1])+"\n")

