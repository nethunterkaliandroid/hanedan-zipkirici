
import zipfile
from tqdm import tqdm

wordlist = "wordlist.txt"
zip_file = "deneme.zip"

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
