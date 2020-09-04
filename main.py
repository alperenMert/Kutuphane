import sqlite3

#Bağlantılar kuruldu
connect=sqlite3.connect("KutuphaneDB.sqlite")
crs=connect.cursor()
crs.execute("CREATE TABLE IF NOT EXISTS Kitap(KitapAdi TEXT, Yazar Text, YayinEvi TEXT, BasimYili INTEGER)")
connect.commit()

while True:
    def list():
        crs.execute("SELECT * FROM Kitap")
        list=crs.fetchall() #Listedeki kitapların hepsi çağırıldı
        print("Kitaplar:")
        for i in list: #Kitaplar sıra ile ekrana yazdırıldı
            print(i)

    def add(KitapAdi,Yazar,YayinEvi,BasimYili):
        crs.execute("INSERT INTO Kitap VALUES(@ka,@y,@ye,@by)",(KitapAdi,Yazar,YayinEvi,BasimYili)) # Kitap eklendi
        connect.commit()

    def delete(KitapAdi):
        crs.execute("DELETE FROM Kitap WHERE KitapAdi=@ka",(KitapAdi,)) # (KitapAdi,) virgül konulmasının sebebi bütün satırı silmesini sağlamak
        connect.commit()

    #Kütüphane ana menüsü
    print("""Kütüphane:
    1- Kitapları Listele
    2- Kitap Ekle
    3- Kitap Sil
    q- Çıkış""")
    choose=input("Lütfen işlem seçiniz:")
    if choose == "q":
        break
    elif choose == "1":
        list()
    elif choose == "2":
        KitapAdi=input("Kitap Adı:")
        Yazar=input("Yazar:")
        YayinEvi=input("Yayın Evi:")
        BasimYili=int(input("Basım Yılı:"))
        add(KitapAdi,Yazar,YayinEvi,BasimYili)
    elif choose == "3":
        KitapAdi=input("Silmek istediğiniz kitabın adı:")
        delete(KitapAdi)

#Bağlantı sonlandı
connect.close()

