from kasa import Depo
class Login_Kasa:
    def __init__(self,kbilgi):
        self.kbilgi = kbilgi
        self.islemler()
    def islemler(self):
        print("""
        0 Çıkış
        1 Şifre Ekle
        2 Şifre Görüntüle
        3 Şifre silme
        4 Bilgi güncelleme
        """)
        while True:
            result = input("işlem seçiniz:")
            try:
                result = int(result)
            except:
                print("Tekrar deneyin")
                continue
            if result == 0:
                print("çıkılıyor...")
                break
            elif result == 1:
                sifread = input("şifre adı:")
                sifre = input("eklenecek şifre:")
                Depo().add(self.kbilgi, sifread, sifre)
            elif result == 2:
                gelen = Depo().all_pass(self.kbilgi)
                if gelen == []:
                    print("hiç kayıtlı şifreniz yok")
                else:
                    say = 1
                    for i in gelen:
                        print(f"{say}.şifrenin adı {i}")
                        say += 1
                    while True:
                        try:
                            ans = input("hangi şifreyi görüntülemek istiyorsunuz:")
                            ans = int(ans)
                        except:
                            print("yanlış seçim")
                        if ans > 0 and ans <= say:
                            ind = ans - 1
                            gönderilecek = gelen[ind]
                            while True:
                                fon = input("fon şifresi:")
                                gelenler = Depo().show(self.kbilgi, fon, gönderilecek)
                                if  gelenler == False:
                                    print("Fon şifresi Yanlış")
                                else:
                                    print(f"şifre adı:{gelenler[0]}\nşifre:{gelenler[1]}")
                                    break
                            break
                        else:
                            print("yanlış seçim")
            elif result == 3:
                gelen = Depo().all_pass(self.kbilgi)
                if gelen == []:
                    print("hiç kayıtlı şifreniz yok")
                else:
                    say = 1
                    for i in gelen:
                        print(f"{say}.şifrenin adı {i}")
                        say += 1
                    while True:
                        try:
                            ans = input("hangi şifreyi silmek istiyorsunuz:") 
                            ans = int(ans)
                        except:
                            print("yanlış seçim")
                        if ans > 0 and ans <= say:
                            ind = ans - 1
                            gönderilecek = gelen[ind]
                            while True:
                                fon = input("fon şifresi:")
                                gelenler = Depo().delete(self.kbilgi, fon, gönderilecek)
                                if  gelenler == False:
                                    print("Fon şifresi Yanlış")
                                else:
                                    print("silme işlemi bşarılı")
                                    break
                            break
                        else:
                            print("yanlış seçim")
            elif result == 4:
                print("1 şifre değişimi\n2 telefon numarası değişimi") 
                while True:
                    result = input("işlem seçiniz:")
                    try:
                        result = int(result)
                    except:
                        print("yanlış seçim")
                        continue
                    if result == 1:
                        while True:
                            newpass = input("yeni şifre:")
                            newpass2 = input("yeni şifre tekrar")
                            if newpass == newpass2:
                                while True:
                                    fon = input("Fon şifresi:")
                                    gelen = Depo().update_bilgi(self.kbilgi, "şifre", fon, newpass)
                                    if gelen == True:
                                        print("işlem başarılı")
                                        break
                                    else:
                                        print("bilgiler hatalı tekrar dene")
                                        continue
                                break
                            else:
                                print("yzdığınız şifreler uyuşmuyor")
                                continue
                        break
                    elif result == 2:
                        newpass = input("yeni telefon numarası:")
                        while True:
                            fon = input("Fon şifresi:")
                            gelen = Depo().update_bilgi(self.kbilgi, "telefon numarası", fon, newpass)
                            if gelen == True:
                                print("işlem başarılı")
                                break
                            else:
                                print("bilgiler hatalı tekrar dene")
                                continue
                        break
                    else:
                        print("seçim hatalı")
                        continue
                            

            else:
                print("Tekrar deneyin")
                continue


