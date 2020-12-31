import re
sentence = input()
sentence = re.sub('lj|nj|dz=', 'j', sentence)
sentence = re.sub(r'[^\w]', '', sentence)
print(len(sentence))
