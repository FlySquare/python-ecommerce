import os #işlevler edinmek için
import platform #işletim sistemi bilgisi çekmek için
import getpass #şifreyi gizlemek için


sepet = []

def app():
    if platform.system() == "Windows":
        os.system('cls')
             
    elif platform.system() == "Linux":
        os.system('clear')
    kullaniciAdi = "flysquare"
    kullaniciSifre = "asd"

    print("*** 🛒 E-SEPET'E HOŞGELDİNİZ 🛒 ***")

    txt_kullaniciAdi = input("Kullanıcı Adınız: ")
    txt_sifre =  getpass.getpass("Şifreniz: ")

    if txt_kullaniciAdi==kullaniciAdi and txt_sifre==kullaniciSifre:
        if platform.system() == "Windows":
            os.system('cls')       
        elif platform.system() == "Linux":
            os.system('clear')
        main()
   
    else:
        if platform.system() == "Windows":
                os.system('cls')
                print("🚫 Kullanıcı Adı Veya Şifre Hatalı 🚫\n")
                app()
        elif platform.system() == "Linux":
                os.system('clear')
                print("🚫 Kullanıcı Adı Veya Şifre Hatalı 🚫\n")
                app()
        else:
                print("🚫 Kullanıcı Adı Veya Şifre Hatalı 🚫\n")
                app()

def main():
   
      
    print("İşlem yapmak istediğiniz numarayı giriniz:\n\n1- Sepete Ürün Ekle\n2- Sepetten Ürün Sil\n3- Sepeti Göster\n4- Çıkış\n")
    islemNo = input("Menü No: ")    
    if platform.system() == "Windows":
        os.system('cls')
             
    elif platform.system() == "Linux":
        os.system('clear')
    menu(islemNo)  

def urunekle():

      
    print("Kategoriler: \n\n1-Teknoloji\n2-Spor\n3-Kitap\n4-Hobi\n5-Giyim\n6-Geri Dön \n")
    secilenKategori = input("Kategori Seçiniz: ")
    
    try:
        b = int(secilenKategori)
    except ValueError:
        try:
            b = float(secilenKategori)
        except ValueError:
            urunekle()
        else:
            urunekle()
    else:
        secilenKategori_int = int(secilenKategori)
        if secilenKategori_int <1 or secilenKategori_int>6:
            urunekle()
        elif secilenKategori_int == 6:
            if platform.system() == "Windows":
                os.system('cls')
                     
            elif platform.system() == "Linux":
                os.system('clear')
            main()
        elif secilenKategori_int == 5:
            if platform.system() == "Windows":
                os.system('cls')
                     
            elif platform.system() == "Linux":
                os.system('clear')
            kat_1 = "Mavi / Yüksek Bel Mom Jeans"
            kat_2 = "Nike / Air Force 1 High '07"
            kat_3 = "Adidas / Superstar Ayakkabı"
            kat_4 = "Zara / Çıkarılabilir Pilot Şapka"
            kat_5 = "Puma / Arsenal Pijama Takımı"
           
            print("Giyim Kategorisi Ürünleri: \n\n1- "+kat_1+"\n"+"2- "+kat_2+"\n"+"3- "+kat_3+"\n"+"4- "+kat_4+"\n"+"5- "+kat_5+"\n"+"6- Geri Git\n")
            sepetekle = input("Sepete eklemek istediğin ürün: ")
 
            try:
                b = int(sepetekle)
            except ValueError:
                try:
                    b = float(sepetekle)
                except ValueError:
                    if platform.system() == "Windows":
                        os.system('cls')
                        urunekle()
                    elif platform.system() == "Linux":
                        os.system('clear')
                        urunekle()
                    
                else:
                    if platform.system() == "Windows":
                        os.system('cls')
                        urunekle()
                    elif platform.system() == "Linux":
                        os.system('clear')
                        urunekle()
                    
            else:
                sepetekle_int = int(sepetekle)
                if(sepetekle_int<1 or sepetekle_int >6):
                   urunekle()
                elif sepetekle_int==6:
                    if platform.system() == "Windows":
                        os.system('cls')
                        urunekle()
                    elif platform.system() == "Linux":
                        os.system('clear')
                        urunekle()
                elif sepetekle_int==1:
                    sepet.append(kat_1)
                    if platform.system() == "Windows":
                        os.system('cls')

                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
                elif sepetekle_int==2:
                    sepet.append(kat_2)
                    if platform.system() == "Windows":
                        os.system('cls')
                             
                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
                elif sepetekle_int==3:
                    sepet.append(kat_3)
                    if platform.system() == "Windows":
                        os.system('cls')
                             
                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
                elif sepetekle_int==4:
                    sepet.append(kat_4)
                    if platform.system() == "Windows":
                        os.system('cls')
                             
                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
                elif sepetekle_int==5:
                    sepet.append(kat_5)
                    if platform.system() == "Windows":
                        os.system('cls')
                             
                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
        elif secilenKategori_int == 4:
            if platform.system() == "Windows":
                os.system('cls')
                     
            elif platform.system() == "Linux":
                os.system('clear')
            kath_1 = "Uzaktan kumandalı araba"
            kath_2 = "Playstation 5"
            kath_3 = "Monopoly"
            kath_4 = "F16 Savaş Uçağı Maketi"
            kath_5 = "Oyun Hamuru"
           
            print("Teknoloji Kategorisi Ürünleri: \n\n1- "+kath_1+"\n"+"2- "+kath_2+"\n"+"3- "+kath_3+"\n"+"4- "+kath_4+"\n"+"5- "+kath_5+"\n"+"6- Geri Git\n")
            sepetekle = input("Sepete eklemek istediğin ürün: ")
 
            try:
                b = int(sepetekle)
            except ValueError:
                try:
                    b = float(sepetekle)
                except ValueError:
                    if platform.system() == "Windows":
                        os.system('cls')
                        urunekle()
                    elif platform.system() == "Linux":
                        os.system('clear')
                        urunekle()
                    
                else:
                    if platform.system() == "Windows":
                        os.system('cls')
                        urunekle()
                    elif platform.system() == "Linux":
                        os.system('clear')
                        urunekle()
                    
            else:
                sepetekle_int = int(sepetekle)
                if(sepetekle_int<1 or sepetekle_int >6):
                   urunekle()
                elif sepetekle_int==1:
                    sepet.append(kath_1)
                    if platform.system() == "Windows":
                        os.system('cls')

                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
                elif sepetekle_int==6:
                    if platform.system() == "Windows":
                        os.system('cls')
                        urunekle();
                    elif platform.system() == "Linux":
                        os.system('clear')
                        urunekle();
                elif sepetekle_int==2:
                    sepet.append(kath_2)
                    if platform.system() == "Windows":
                        os.system('cls')
                             
                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
                elif sepetekle_int==3:
                    sepet.append(kath_3)
                    if platform.system() == "Windows":
                        os.system('cls')
                             
                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
                elif sepetekle_int==4:
                    sepet.append(kath_4)
                    if platform.system() == "Windows":
                        os.system('cls')
                             
                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
                elif sepetekle_int==5:
                    sepet.append(kath_5)
                    if platform.system() == "Windows":
                        os.system('cls')
                             
                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
        elif secilenKategori_int == 3:
            if platform.system() == "Windows":
                os.system('cls')
                     
            elif platform.system() == "Linux":
                os.system('clear')
            katk_1 = "Cengiz Aytmatov / Beyaz  Gemi"
            katk_2 = "Oğuz Atay / Tutanamayanlar"
            katk_3 = "Hemingway / Çanlar Kimin İçin Çalıyor"
            katk_4 = "Charles Disckens / İki Şehrin Hikayesi"
            katk_5 = "Cengiz Erşahin / Sır"
           
            print("Kitap Kategorisi Ürünleri: \n\n1- "+katk_1+"\n"+"2- "+katk_2+"\n"+"3- "+katk_3+"\n"+"4- "+katk_4+"\n"+"5- "+katk_5+"\n 6- Geri Git\n")
            sepetekle = input("Sepete eklemek istediğin ürün: ")
 
            try:
                b = int(sepetekle)
            except ValueError:
                try:
                    b = float(sepetekle)
                except ValueError:
                    if platform.system() == "Windows":
                        os.system('cls')
                        urunekle()
                    elif platform.system() == "Linux":
                        os.system('clear')
                        urunekle()
                    
                else:
                    if platform.system() == "Windows":
                        os.system('cls')
                        urunekle()
                    elif platform.system() == "Linux":
                        os.system('clear')
                        urunekle()
                    
            else:
                sepetekle_int = int(sepetekle)
                if(sepetekle_int<1 or sepetekle_int >6):
                   urunekle()
                elif sepetekle_int==1:
                    sepet.append(katk_1)
                    if platform.system() == "Windows":
                        os.system('cls')

                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
                elif sepetekle_int==6:
                    if platform.system() == "Windows":
                        os.system('cls')
                        urunekle();
                    elif platform.system() == "Linux":
                        os.system('clear')
                        urunekle();
                elif sepetekle_int==2:
                    sepet.append(katk_2)
                    if platform.system() == "Windows":
                        os.system('cls')
                             
                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
                elif sepetekle_int==3:
                    sepet.append(katk_3)
                    if platform.system() == "Windows":
                        os.system('cls')
                             
                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
                elif sepetekle_int==4:
                    sepet.append(katk_4)
                    if platform.system() == "Windows":
                        os.system('cls')
                             
                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
                elif sepetekle_int==5:
                    sepet.append(katk_5)
                    if platform.system() == "Windows":
                        os.system('cls')
                             
                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
        elif secilenKategori_int == 2:
            if platform.system() == "Windows":
                os.system('cls')
                     
            elif platform.system() == "Linux":
                os.system('clear')
            kats_1 = "Türkiye Kupası Futbol Topu"
            kats_2 = "5 Numara Kaleci Eldiveni"
            kats_3 = "Fenerbahçe İç Saha Forması XL"
            kats_4 = "Minyatür Golf Çantası"
            kats_5 = "Tenis Raket Takımı"
           
            print("Spor Kategorisi Ürünleri: \n\n1- "+kats_1+"\n"+"2- "+kats_2+"\n"+"3- "+kats_3+"\n"+"4- "+kats_4+"\n"+"5- "+kats_5+"\n6- Geri Dön\n")
            sepetekle = input("Sepete eklemek istediğin ürün: ")
 
            try:
                b = int(sepetekle)
            except ValueError:
                try:
                    b = float(sepetekle)
                except ValueError:
                    if platform.system() == "Windows":
                        os.system('cls')
                        urunekle()
                    elif platform.system() == "Linux":
                        os.system('clear')
                        urunekle()
                    
                else:
                    if platform.system() == "Windows":
                        os.system('cls')
                        urunekle()
                    elif platform.system() == "Linux":
                        os.system('clear')
                        urunekle()
                    
            else:
                sepetekle_int = int(sepetekle)
                if(sepetekle_int<1 or sepetekle_int >6):
                   urunekle()
                elif sepetekle_int==1:
                    sepet.append(kats_1)
                    if platform.system() == "Windows":
                        os.system('cls')

                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
                elif sepetekle_int==2:
                    sepet.append(kats_2)
                    if platform.system() == "Windows":
                        os.system('cls')
                             
                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
                elif sepetekle_int==6:
                    if platform.system() == "Windows":
                        os.system('cls')
                        urunekle();
                    elif platform.system() == "Linux":
                        os.system('clear')
                        urunekle();
                elif sepetekle_int==3:
                    sepet.append(kats_3)
                    if platform.system() == "Windows":
                        os.system('cls')
                             
                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
                elif sepetekle_int==4:
                    sepet.append(kats_4)
                    if platform.system() == "Windows":
                        os.system('cls')
                             
                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
                elif sepetekle_int==5:
                    sepet.append(kats_5)
                    if platform.system() == "Windows":
                        os.system('cls')
                             
                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
        elif secilenKategori_int == 1:
            if platform.system() == "Windows":
                os.system('cls')
                     
            elif platform.system() == "Linux":
                os.system('clear')
            katt_1 = "LG Smart Televizyon"
            katt_2 = "MacBook Pro 16GB"
            katt_3 = "512GB M2 SSD"
            katt_4 = "Samsung Home Sound Bar"
            katt_5 = "JBL GO 2 Bluetooth Hoparlor"
           
            print("Teknoloji Kategorisi Ürünleri: \n\n1- "+katt_1+"\n"+"2- "+katt_2+"\n"+"3- "+katt_3+"\n"+"4- "+katt_4+"\n"+"5- "+katt_5+"\n6- Geri Dön\n")
            sepetekle = input("Sepete eklemek istediğin ürün: ")
 
            try:
                b = int(sepetekle)
            except ValueError:
                try:
                    b = float(sepetekle)
                except ValueError:
                    if platform.system() == "Windows":
                        os.system('cls')
                        urunekle()
                    elif platform.system() == "Linux":
                        os.system('clear')
                        urunekle()
                    
                else:
                    if platform.system() == "Windows":
                        os.system('cls')
                        urunekle()
                    elif platform.system() == "Linux":
                        os.system('clear')
                        urunekle()
                    
            else:
                sepetekle_int = int(sepetekle)
                if(sepetekle_int<1 or sepetekle_int >6):
                   urunekle()
                elif sepetekle_int==1:
                    sepet.append(katt_1)
                    if platform.system() == "Windows":
                        os.system('cls')

                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
                elif sepetekle_int==6:
                    if platform.system() == "Windows":
                        os.system('cls')
                        urunekle();
                    elif platform.system() == "Linux":
                        os.system('clear')
                        urunekle();
                elif sepetekle_int==2:
                    sepet.append(katt_2)
                    if platform.system() == "Windows":
                        os.system('cls')
                             
                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
                elif sepetekle_int==3:
                    sepet.append(katt_3)
                    if platform.system() == "Windows":
                        os.system('cls')
                             
                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
                elif sepetekle_int==4:
                    sepet.append(katt_4)
                    if platform.system() == "Windows":
                        os.system('cls')
                             
                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()
                elif sepetekle_int==5:
                    sepet.append(katt_5)
                    if platform.system() == "Windows":
                        os.system('cls')
                             
                    elif platform.system() == "Linux":
                        os.system('clear')
                    print("\nSepete eklendi. Son sepetiniz aşağıda!\n")
                    print(sepet)
                    print("\n")
                    urunekle()





def urunsil():
    
    print("Şuanki Sepetiniz Aşağıda --- (Geri Gitmek İçin esc yazınız): \n")
    print(sepet)
    urunsil2 = input("\n Silmek istediğiniz ürünün adını giriniz: ")
    if urunsil2 == "esc":
        if platform.system() == "Windows":
            os.system('cls')
            main()
        
        elif platform.system() == "Linux":
            os.system('clear')
            main()
       
    else:
        try:
            sepet.remove(urunsil2)
        except ValueError:
            if platform.system() == "Windows":
                os.system('cls')
                urunsil()
          
            elif platform.system() == "Linux":
                os.system('clear')
                urunsil()
            
        else:
            if platform.system() == "Windows":
                os.system('cls')
          
            elif platform.system() == "Linux":
                os.system('clear')
        
            print("Ürün sepetten silindi!\n")
            urunsil()    


def sepetgoster():
    print("Şuanki Sepetiniz: \n")
    print(sepet)
    print("\n")
    main()


def menu(var):


    
 
    try:
        b = int(var)
    except ValueError:
        try:
            b = float(var)
        except ValueError:
            main()
        else:
            main()
    else:
        intvar=int(var)
        if(intvar<1 or intvar >4):
            main()
        else:
            if intvar == 1:
                if platform.system() == "Windows":
                    os.system('cls')
                    urunekle()

                elif platform.system() == "Linux":
                    os.system('clear')
                    urunekle()
                
            elif intvar == 2:
                urunsil()
            elif intvar == 3:
                sepetgoster()
            elif intvar == 4:
                if platform.system() == "Windows":
                    os.system('cls')
                    app()
                elif platform.system() == "Linux":
                    os.system('clear')
                    app()
                else:
                    app()


        
  


            



app()

