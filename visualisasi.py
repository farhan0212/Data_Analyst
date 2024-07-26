# import pandas as pd
# from collections import Counter
# import re
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud

# # Membaca file CSV
# file_path = 'E:/KAMPUS/Pengolahan data besar/Tugas kelompok/friends_quotes.csv'
# data = pd.read_csv(file_path)

# # Menggabungkan semua teks dalam kolom 'quotes'
# all_quotes = ' '.join(data['quote'].dropna())

# # Membersihkan teks: menghapus tanda baca dan mengubah ke huruf kecil
# cleaned_quotes = re.sub(r'[^\w\s]', '', all_quotes).lower()

# # Memisahkan teks menjadi kata-kata individu
# words = cleaned_quotes.split()

# # Menghitung frekuensi kemunculan setiap kata
# word_counts = Counter(words)

# # Membuat Word Cloud
# wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)

# # Menampilkan Word Cloud
# plt.figure(figsize=(10, 5))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.show()

import pandas as pd
from collections import Counter
import re
import matplotlib.pyplot as plt

# Membaca file CSV
file_path = 'E:/KAMPUS/Pengolahan data besar/Tugas kelompok/friends_quotes.csv'
data = pd.read_csv(file_path)

# Menggabungkan semua teks dalam kolom 'quotes'
all_quotes = ' '.join(data['quote'].dropna())

# Membersihkan teks: menghapus tanda baca dan mengubah ke huruf kecil
cleaned_quotes = re.sub(r'[^\w\s]', '', all_quotes).lower()

# Memisahkan teks menjadi kata-kata individu
words = cleaned_quotes.split()

# Menghitung frekuensi kemunculan setiap kata
word_counts = Counter(words)

# Memilih sejumlah kata yang paling sering muncul (misalnya, 10 kata teratas)
top_words = word_counts.most_common(10)

# Membuat DataFrame baru dari hasil perhitungan frekuensi kata
df_top_words = pd.DataFrame(top_words, columns=['Word', 'Frequency'])

# Menampilkan tabel
print("Top 10 Most Common Words:")
print(df_top_words)

# Membuat diagram batang
plt.figure(figsize=(10, 6))
plt.bar(df_top_words['Word'], df_top_words['Frequency'], color='skyblue')
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.title('Top 10 Most Common Words in Quotes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
