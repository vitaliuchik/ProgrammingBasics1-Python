birthday = [i for i in range(28, 38)]
gray_bin = []
decoded_bin = []
len_birth = len(birthday)

# кодування Грея у двійкову форму
for i in range(len_birth):
    gray_bin.append(bin(birthday[i] ^ (birthday[i] >> 1))[2:])

print('birthday + 10 list: ', birthday)
print('coded list in binary: ', gray_bin)

# декодування Грея в двійкову форму
for i in range(len_birth):
    decoded_bin.append(gray_bin[i][0])
    for j in range(1, len(gray_bin[i])):
        decoded_bin[i] += str(int(gray_bin[i][j]) ^ int(decoded_bin[i][j-1]))

print('decoded list in binary: ', decoded_bin)

# переведення декодованих даних в десяткову форму
decoded_int = [int('0b'+decoded_bin[i], 2) for i in range(len_birth)]

print('decoded list: ', decoded_int)
