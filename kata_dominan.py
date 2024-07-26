import pandas as pd
from collections import Counter
import re

# Membaca file CSV
data = pd.read_csv('friends_quotes.csv')

# Menggabungkan semua teks dalam kolom 'quotes'
all_quotes = ' '.join(data['quote'].dropna())

# Membersihkan teks: menghapus tanda baca dan mengubah ke huruf kecil
cleaned_quotes = re.sub(r'[^\w\s]', '', all_quotes).lower()

# Memisahkan teks menjadi kata-kata individu
kata = cleaned_quotes.split()

# Menghitung frekuensi kemunculan setiap kata
jumlah_kata = Counter(kata)

# Menemukan kata yang paling sering muncul
most_common_words = jumlah_kata.most_common(20)  #5 kata yang sering muncul

print("Kata yang paling sering muncul:")
for word, count in most_common_words:
    print(f"{word}: {count}")
