import os #işlevler edinmek için

import getpass #şifreyi gizlemek için

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


kullaniciAdi = "flysquare"
kullaniciSifre = "asd"
print("*** 🛒 E-SEPET'E HOŞGELDİNİZ 🛒 ***")

txt_kullaniciAdi = input("👨 Kullanıcı Adınız: ")
txt_sifre =  getpass.getpass("🔐 Şifreniz: ")

