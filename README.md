# python-ecommerce
Harici Kütüphane Kullanmadım.

Aşağıdaki kod eğer program windows üzerinde açılıyorsa terminale cmd silme komutu eğer linux üzerinde açılıyorsa uçbirim silme komutu gönderiyor. Daha temiz bir görünüm için.
*********************************************
    if platform.system() == "Windows":
        os.system('cls')
             
    elif platform.system() == "Linux":
        os.system('clear')
*********************************************

app fonksiyonu açıklaması: kullanıcı adı ve şifre  doğrulaması yapıyor. dah asonra doğruysa eğer asıl programa yönlendiriyor

main fonksiyonu açıklaması: 4 ana kategoriyi kontrol ediyor. selimlere göre kategorilere yönlendiriyor.

urunekle fonksiyonu: seçilen kategori içindeki ürünleri listeye eklemee fonksiyonu.

urunsil fonksiyonu: seçilen ürün ismine göre listeden silme gerçekleştiriyor

sepet göster: sepeti gösterir

menu fonksiyonu: main den gelen sayıyı kontrol edip hataya düşmesini engelleyerek istenilen 4 sayıdan hangisi seçilmişse onun fonksiyonuna gönderiyor 

aşağıdaki kod bloğu hata alınmasını engelliyor bu sayede kodumuz try except ile hatasız çalışıyor. aynı samanda try içinde yazılan kodu kontrol edip doğrulunu onaylıyor.
********************************************
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
********************************************