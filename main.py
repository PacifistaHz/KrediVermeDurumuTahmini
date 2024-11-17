import os

def arffDonusturCSV(dosyaAdi):
    yeniMetin = ""
    sutunAdlari = ""
    durum = False

    try:
        with open(dosyaAdi, "r") as f:
            satirlar = f.readlines()

        for satir in satirlar:
            if satir.strip().lower() == "@data":
                durum = True
                continue

            if "@attribute" in satir.lower():
                attribute_parts = satir.split()
                if len(attribute_parts) > 1:
                    sutunAdlari += attribute_parts[1] + ","

            if durum:
                if len(satir.strip()) > 0:  # Bu satırın veri içerdiğinden emin olun
                    yeniMetin += satir

        dosyaAdi = os.path.basename(dosyaAdi)
        dosyaAdi = os.path.splitext(dosyaAdi)[0]
        sutunAdlari = sutunAdlari.rstrip(",")

        dosya_yolu = os.path.abspath(dosyaAdi + ".csv")

        with open(dosya_yolu, "w") as f:
            f.write(sutunAdlari + "\n" + yeniMetin)

        print(f"ARFF'den CSV'ye dönüştürme işlemi tamamlandı. Dosya yolu: {dosya_yolu}")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

# Örneğin kullanım şekli:
arffDonusturCSV("ornek.arff")
