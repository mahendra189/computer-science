def mostcommonword(paragraph,banned):
    paragraph = paragraph.lower().strip()
    separated = paragraph.split(' ')
    i = 0
    while i <len(separated):
        if not separated[i][-1].isalpha():
            separated[i]= separated[i][:-1]
        if ',' in separated[i]:
            splitted = separated[i].split(',')
            separated.pop(i)
            separated = separated + splitted
            continue
        i+=1
    # time for mapping
    word_mapping = {}
    for word in separated:
        if word in word_mapping:
            word_mapping[word] +=1
        else:
            word_mapping[word] = 1
    if len(word_mapping) ==1:
        for word in word_mapping:
            return word
    # print(separated)
    # print(word_mapping)
    # remove banned
    for ban in banned:
        word_mapping.pop(ban)
    # print(word_mapping)
    # time for max
    max = 1
    maxword = ''
    for item in word_mapping:
        if word_mapping[item] > max:
            max = word_mapping[item]
            maxword = item
    return maxword
            
# para = 'i am mahendra, i have a car, computer,modern home,house in sanfrancisco'
# banned = ['i','a']

# a = ' a b,b,b,b,c,c,c c a b'
a = "a, a, a, a, b,b,b,c, c"
b = ['a']
print(mostcommonword(a,b))
