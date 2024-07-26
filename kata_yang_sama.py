import pandas as pd
import re

# Membaca file CSV
file_path = 'E:/KAMPUS/Pengolahan data besar/Tugas kelompok/friends_quotes.csv'
data = pd.read_csv(file_path)

def has_duplicate_words(sentence):
    # Membersihkan teks: menghapus tanda baca dan mengubah ke huruf kecil
    cleaned_sentence = re.sub(r'[^\w\s]', '', sentence).lower()
    
    # Memisahkan teks menjadi kata-kata individu
    words = cleaned_sentence.split()
    
    # Mendeteksi pengulangan kata
    word_set = set()
    for word in words:
        if word in word_set:
            return True
        word_set.add(word)
    return False

# Menerapkan fungsi ke setiap baris di kolom 'quote'
data['has_duplicates'] = data['quote'].apply(has_duplicate_words)

# Menampilkan baris yang memiliki kata yang sama dalam kutipan
duplicate_quotes = data[data['has_duplicates']]
print(duplicate_quotes[['quote']])
