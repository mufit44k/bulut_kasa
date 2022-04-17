from kasa import Depo
from kasa_login import Login_Kasa
class Ui:
    def __init__(self):
        self.ui()
    def ui(self):
        print("""
            0 Çıkış
            1 Giriş
            2 Kayıt ol
            3 Şifremi unuttum
            """)
        while True:
            result = input("İşlem seçiniz:")
            if result == "0" or result == 0:
                print("çıkılıyor....")
                break
            elif result == "1" or result == 1:
                while True:
                    tel = input("telefon numarsı:")
                    passs = input("Şifre:")
                    if Depo().login(tel,passs) == True:
                        print("Hoşgeldin....")
                        Login_Kasa(tel)
                        break
                    else:
                        print("tekrar deneyin bilgiler eşleşmiyor..")
                        continue
            elif result == "2" or result == 2:
                while True:
                    tel = input("telefon numarası:")
                    while True:
                        pas1 = input("şifre:")
                        pas2 = input("şifre tekrar:")
                        if pas1 == pas2:
                            break
                        else:
                            print("şifreler uyuşmuyor")
                            continue
                    while True:
                        pasfon = input("Fon şifresi oluştur asla değiştirilemez görüntülenemez:")
                        pasfon2 = input("Fon şifresi oluştur asla değiştirilemez görüntülenemez(tekrar):")
                        if pasfon == pasfon2:
                            break
                        else:
                            print("şifreler uyuşmuyor")
                            continue
                    if Depo().register(tel, pas1, pasfon) == True:
                        print("kayıt işlemi başarılı giriş yapabilirsiniz:")
                        break
                    else:
                        ("Tekrar deneyin")
                        continue
            elif result == "3" or result == 3:
                while True:
                    kbilgi = input("telefon numrası:")
                    fon = input("Fon şifresi:")
                    gelen = Depo().forget(kbilgi, fon)
                    if gelen == False:
                        print("bilgiler hatalı tekrar dene")
                        continue
                    else:
                        print(f"telefon numaranız: {gelen[0]}\nşifreniz:{gelen[1]}")
                        break

            else:
                print("hatali seçim Tekrar dene")

if __name__=="__main__":
    Ui()