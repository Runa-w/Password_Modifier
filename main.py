word = input()
password = ''

for char in word:
  password = word.replace('i', '!').replace('a', '@').replace('m', 'M').replace('B', '8').replace('o', '.')
  password += 'q*s'
print(password)
  