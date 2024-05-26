import pandas as pd

english_to_sinhala = {
    'a': 'අ', 'b': 'බ', 'c': 'ස', 'd': 'ද', 'e': 'එ',
    'f': 'ෆ', 'g': 'ග', 'h': 'හ', 'i': 'ඉ', 'j': 'ජ',
    'k': 'ක', 'l': 'ල', 'm': 'ම', 'n': 'න', 'o': 'ඔ',
    'p': 'ප', 'q': 'ක්‍යු', 'r': 'ර', 's': 'ස', 't': 'ත',
    'u': 'උ', 'v': 'ව', 'w': 'ව', 'x': 'ක්ස්', 'y': 'ය',
    'z': 'ස'
}

data = []

for eng_letter, sin_letter in english_to_sinhala.items():
    data.append([eng_letter, sin_letter])


df = pd.DataFrame(data, columns=['English', 'Sinhala'])

df.to_csv('letter_mapping.csv', index=False)

print('Letter mapping saved to letter_mapping.csv')
