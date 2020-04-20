# import urllib.request
# url = 'https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt'
# f = urllib.request.urlopen(url)
# text = f.read()
# text = text.decode('utf-8')
# print(text)


import urllib.request
url = 'https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt'
f = urllib.request.urlopen(url)
text = f.readlines()
result_list = []
for i in range(len(text)):
    text[i] = text[i].strip().decode('utf-8')
    text[i] = text[i].replace('\t', ' ')
    text[i] = text[i].split()
for i in range(len(text) - 7):
    if text[i][0].isdigit():
        el = text[i]
        document = ''
        if text[i + 6][0] == '—':
            document = text[i + 6][-1]
        elif text[i + 7][0] == '—':
            document = text[i + 7][-1]
        name = ' '.join([el[1], el[2], el[3]])
        s = [el[0], name, document, el[6], text[i + 3][-1] ]
        result_list.append(s)

print(result_list)
# print(text)
