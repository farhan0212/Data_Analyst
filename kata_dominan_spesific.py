import pandas as pd
import re

# Membaca file CSV
data = pd.read_csv('friends_quotes.csv')

# Fungsi untuk menghitung jumlah kemunculan kata khusus
def count_specific_word(sentence, word):
    # Membersihkan teks: menghapus tanda baca dan mengubah ke huruf kecil
    cleaned_sentence = re.sub(r'[^\w\s]', '', sentence).lower()
    # Memisahkan teks menjadi kata-kata individu
    words = cleaned_sentence.split()
    # Menghitung jumlah kemunculan kata khusus
    return words.count(word)

# Kata khusus yang ingin dicari
specific_word = "good"

# Menghitung jumlah kemunculan kata khusus dalam setiap kutipan
data['count_' + specific_word] = data['quote'].apply(lambda x: count_specific_word(x, specific_word))

# Menampilkan jumlah kemunculan kata khusus
total_count = data['count_' + specific_word].sum()
print(f"Total kemunculan kata '{specific_word}': {total_count}")
