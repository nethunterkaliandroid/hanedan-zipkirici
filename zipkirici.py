import sys
import zipfile
from tqdm import tqdm

wordlist = sys.argv[2]
zip_file = sys.argv[1]

zip_file = zipfile.ZipFile(zip_file)
n_words = len(list(open(wordlist, "rb")))

print("Denenecek toplam şifre miktarı:", n_words)

with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):

        try:

            zip_file.extractall(pwd=word.strip())

        except:

            continue

        else:

           print("[+] Şifre bulundu", word.decode().strip())

           exit(0)

print("[!] Şifre bulunamadı, başka bir kelime listesini denemelisiniz!")

#@nethunterROM
# Tüm hakları m12345'e aittir
