import sys
import os
from datetime import datetime,date
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit, QComboBox


class Giris(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cari Asistanım - Giriş")
        self.setGeometry(500, 250, 420, 260)

        self.baslik = QLabel("Cari Asistanım", self)
        self.baslik.setGeometry(30, 20, 300, 30)

        self.aciklama = QLabel("Şifreli giriş ekranı", self)
        self.aciklama.setGeometry(30, 55, 300, 25)

        self.kullanici = QLineEdit(self)
        self.kullanici.setPlaceholderText("Kullanıcı adı")
        self.kullanici.setGeometry(30, 90, 350, 35)

        self.sifre = QLineEdit(self)
        self.sifre.setPlaceholderText("Şifre")
        self.sifre.setGeometry(30, 135, 350, 35)

        self.buton = QPushButton("Giriş Yap", self)
        self.buton.setGeometry(30, 180, 350, 35)
        self.buton.clicked.connect(self.giris_kontrol)


    def giris_kontrol(self):
        if self.kullanici.text() == "admin" and self.sifre.text() == "1234":
            self.ana = AnaEkran()
            self.ana.show()
            self.close()
        else:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre hatalı!")
def dosyadan_kayitlari_oku():
    if not os.path.exists("cari_kayitlar.txt"):
        return []

    with open("cari_kayitlar.txt", "r", encoding="utf-8") as dosya:
        satirlar = dosya.readlines()

    kayitlar = []

    for satir in satirlar:
        satir = satir.strip()
        if satir != "":
            kayitlar.append(satir)

    return kayitlar


def dosyaya_kayit_yaz(kayit):
    with open("cari_kayitlar.txt", "a", encoding="utf-8") as dosya:
        dosya.write(kayit + "\n")

class AnaEkran(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cari Asistanım")
        self.setGeometry(300, 80, 900, 700)

        self.kayitlar = dosyadan_kayitlari_oku()

        self.baslik = QLabel("Cari Asistanım Ana Ekran", self)
        self.baslik.setGeometry(30, 20, 400, 30)

        self.aciklama = QLabel("Borç, alacak, ödeme ve tahsilat takip ekranı", self)
        self.aciklama.setGeometry(30, 55, 500, 30)

        self.cari_label = QLabel("Cari Adı:", self)
        self.cari_label.setGeometry(30, 100, 100, 30)

        self.cari_input = QLineEdit(self)
        self.cari_input.setGeometry(130, 100, 250, 30)
        self.cari_input.setPlaceholderText("Örn: ABC Sigorta")

        self.tutar_label = QLabel("Tutar:", self)
        self.tutar_label.setGeometry(30, 145, 100, 30)

        self.tutar_input = QLineEdit(self)
        self.tutar_input.setGeometry(130, 145, 250, 30)
        self.tutar_input.setPlaceholderText("Örn: 2500")

        self.tarih_label = QLabel("Tarih:", self)
        self.tarih_label.setGeometry(30, 190, 100, 30)

        self.tarih_input = QLineEdit(self)
        self.tarih_input.setGeometry(130, 190, 250, 30)
        self.tarih_input.setPlaceholderText("Örn: 25.04.2026")
        self.tur_label = QLabel("İşlem Türü:", self)
        self.tur_label.setGeometry(30, 235, 100, 30)

        self.tur_combo = QComboBox(self)
        self.tur_combo.setGeometry(130, 235, 250, 30)
        self.tur_combo.addItems(["Alacak", "Borç", "Ödeme"])
        self.vade_label = QLabel("Vade Tarihi:", self)
        self.vade_label.setGeometry(30, 275, 100, 30)

        self.vade_input = QLineEdit(self)
        self.vade_input.setGeometry(130, 275, 250, 30)
        self.vade_input.setPlaceholderText("Örn: 30.04.2026")
 

        self.ekle_buton = QPushButton("Cari İşlem Ekle", self)
        self.ekle_buton.setGeometry(30, 320, 350, 35)
        self.ekle_buton.clicked.connect(self.kayit_ekle)

        self.liste_buton = QPushButton("Kayıtları Listele", self)
        self.liste_buton.setGeometry(30, 365, 350, 35)
        self.liste_buton.clicked.connect(self.kayitlari_listele)
        self.arama_input = QLineEdit(self)
        self.arama_input.setGeometry(30, 415, 250, 30)
        self.arama_input.setPlaceholderText("Cari adına göre ara")

        self.arama_buton = QPushButton("Kayıt Ara", self)
        self.arama_buton.setGeometry(290, 415, 90, 30)
        self.arama_buton.clicked.connect(self.kayit_ara)
        self.sil_buton = QPushButton("Kayıt Sil", self)
        self.sil_buton.setGeometry(30, 455, 350, 35)
        self.sil_buton.clicked.connect(self.kayit_sil)
        self.toplam_buton = QPushButton("Toplam Hesapla", self)
        self.toplam_buton.setGeometry(30, 495, 350, 35)
        self.toplam_buton.clicked.connect(self.toplam_hesapla)
        self.geciken_buton = QPushButton("Geciken Ödemeleri Göster", self)
        self.geciken_buton.setGeometry(30, 535, 350, 35)
        self.geciken_buton.clicked.connect(self.geciken_odemeleri_goster)
        self.tahsilat_buton = QPushButton("Tahsilat Hatırlatma Metni", self)
        self.tahsilat_buton.setGeometry(30, 575, 350, 35)
        self.tahsilat_buton.clicked.connect(self.tahsilat_metni_olustur)

        self.sonuc = QTextEdit(self)
        self.sonuc.setGeometry(430, 100, 420, 330)
        self.sonuc.setPlaceholderText("Kayıtlar ve sonuçlar burada görünecek.")
    def kayit_ekle(self):
            cari_adi = self.cari_input.text()
            tutar = self.tutar_input.text()
            tarih = self.tarih_input.text()
            tur = self.tur_combo.currentText()
            vade =self.vade_input.text()

            if cari_adi == "" or tutar == "" or tarih == ""or vade =="":
                self.sonuc.setText("Lütfen tüm alanları doldurun.")
                return

            kayit = f"Cari Adı: {cari_adi} | İşlem Türü: {tur} | Tutar: {tutar} TL | Tarih: {tarih} | Vade Tarihi: {vade}"
            self.kayitlar.append(kayit)
            dosyaya_kayit_yaz(kayit)
            self.sonuc.setText("Kayıt eklendi:\n\n" + kayit)
    def kayitlari_listele(self):
        if len(self.kayitlar) == 0:
            self.sonuc.setText("Henüz kayıt yok.")
            return
        self.sonuc.setText("Kayıtlar:\n\n" + "\n".join(self.kayitlar))
    def kayit_ara(self):
        aranan = self.arama_input.text().lower()

        if aranan == "":
            self.sonuc.setText("Lütfen aramak istediğiniz cari adını yazın.")
            return

        bulunanlar = []

        for kayit in self.kayitlar:
            if aranan in kayit.lower():
                bulunanlar.append(kayit)

        if len(bulunanlar) == 0:
            self.sonuc.setText("Aranan cari kaydı bulunamadı.")
        else:
            self.sonuc.setText("Arama Sonuçları:\n\n" + "\n".join(bulunanlar))
    def kayit_sil(self):
        aranan = self.arama_input.text().lower()

        if aranan == "":
            self.sonuc.setText("Silmek için arama kutusuna cari adı yazın.")
            return

        yeni_liste = []
        silinenler = []

        for kayit in self.kayitlar:
            if aranan in kayit.lower():
                silinenler.append(kayit)
            else:
                yeni_liste.append(kayit)

        if len(silinenler) == 0:
            self.sonuc.setText("Silinecek kayıt bulunamadı.")
            return

        self.kayitlar = yeni_liste

        with open("cari_kayitlar.txt", "w", encoding="utf-8") as dosya:
            for kayit in self.kayitlar:
                dosya.write(kayit + "\n")

        self.sonuc.setText("Silinen kayıtlar:\n\n" + "\n".join(silinenler))
    def toplam_hesapla(self):
        toplam_alacak = 0
        toplam_borc = 0
        toplam_odeme = 0

        for kayit in self.kayitlar:
            parcalar = kayit.split("|")

            tur = ""
            tutar = "0"

            for parca in parcalar:
                parca = parca.strip()

                if parca.startswith("İşlem Türü:"):
                    tur = parca.replace("İşlem Türü:", "").strip()

                if parca.startswith("Tutar:"):
                    tutar = parca.replace("Tutar:", "").replace("TL", "").strip()

            try:
                tutar = float(tutar)
            except:
                tutar = 0

            if tur == "Alacak":
                toplam_alacak += tutar
            elif tur == "Borç":
                toplam_borc += tutar
            elif tur == "Ödeme":
                toplam_odeme += tutar

        net_durum = toplam_alacak - toplam_borc - toplam_odeme

        sonuc = (
            "TOPLAM DURUM\n\n"
            f"Toplam Alacak: {toplam_alacak:.2f} TL\n"
            f"Toplam Borç: {toplam_borc:.2f} TL\n"
            f"Toplam Ödeme: {toplam_odeme:.2f} TL\n\n"
            f"Net Durum: {net_durum:.2f} TL"
        )

        self.sonuc.setText(sonuc)
    def geciken_odemeleri_goster(self):
        bugun = date.today()
        gecikenler = []

        for kayit in self.kayitlar:
            parcalar = kayit.split("|")
            vade_tarihi = ""

            for parca in parcalar:
                parca = parca.strip()

                if parca.startswith("Vade Tarihi:"):
                    vade_tarihi = parca.replace("Vade Tarihi:", "").strip()

            try:
                vade = datetime.strptime(vade_tarihi, "%d.%m.%Y").date()
            except:
                continue

            if vade < bugun:
                gecikenler.append(kayit)

        if len(gecikenler) == 0:
            self.sonuc.setText("Geciken ödeme bulunmamaktadır.")
        else:
            self.sonuc.setText("GECİKEN ÖDEMELER:\n\n" + "\n".join(gecikenler))
    def tahsilat_metni_olustur(self):
        aranan = self.arama_input.text().lower()

        if aranan == "":
            self.sonuc.setText("Tahsilat metni için arama kutusuna cari adı yazın.")
            return

        secilen_kayit = ""

        for kayit in self.kayitlar:
            if aranan in kayit.lower():
                secilen_kayit = kayit
                break

        if secilen_kayit == "":
            self.sonuc.setText("Tahsilat metni için uygun kayıt bulunamadı.")
            return

        cari_adi = ""
        tutar = ""
        tarih = ""
        vade = ""

        parcalar = secilen_kayit.split("|")

        for parca in parcalar:
            parca = parca.strip()

            if parca.startswith("Cari Adı:"):
                cari_adi = parca.replace("Cari Adı:", "").strip()

            if parca.startswith("Tutar:"):
                tutar = parca.replace("Tutar:", "").strip()

            if parca.startswith("Tarih:"):
                tarih = parca.replace("Tarih:", "").strip()

            if parca.startswith("Vade Tarihi:"):
                vade = parca.replace("Vade Tarihi:", "").strip()

        metin = (
            f"Sayın {cari_adi},\n\n"
            f"{vade} vadeli {tutar} tutarındaki ödemeniz için hatırlatma amacıyla iletişime geçiyoruz.\n\n"
            f"Kayıt tarihi: {tarih}\n\n"
            f"Ödemenin uygun olduğunuz en kısa sürede gerçekleştirilmesini rica ederiz.\n\n"
            f"İyi çalışmalar."
        )

        self.sonuc.setText(metin)

app = QApplication(sys.argv)
pencere = Giris()
pencere.show()
sys.exit(app.exec())