import pymongo
from pymongo import MongoClient
import certifi
ca = certifi.where()
from bson.objectid import ObjectId

class Depo:
    def __init__(self):
        self.cluster = MongoClient("mongodb+srv://MFT2015:Mufit2015@cluster0.yovhi.mongodb.net/kasaui?retryWrites=true&w=majority",tlsCAFile=ca)
        self.db = self.cluster["kasaui"]
        self.collectionuser = self.db["kasauser"]
        self.collectionuserpass = self.db["kasapass"]
    def login(self,tel,paswd):
        result = self.collectionuser.find({"telefon numarası":tel,"şifre":paswd})
        result = list(result)
        if result == []:
            return False
        else:
            return True
    def register(self,tel,paswd,passwd2):
        result = self.collectionuser.find({"telefon numarası":tel})
        result = list(result)
        if result == []:
            self.collectionuser.insert_one({"telefon numarası":tel,"şifre":paswd,"Fon şifresi":passwd2})
            return True
        else:
            return False
    def show(self,kbilgi,passwd2,pssname):
        result = self.collectionuser.find({"telefon numarası":kbilgi,"Fon şifresi":passwd2})
        result = list(result)
        result2 = self.collectionuserpass.find({"kbilgi":kbilgi})
        result2 = list(result2)
        if self.kontrol(result2) == True:
            eklenen = result2[0]["eklenen"]
            if result == []:
                return False
            else:
                for i in eklenen:
                    if i["şifre adı"] == pssname:
                        listereturn = [pssname,i["şifre"]]
                        return listereturn
        else:
            return False
    def add(self,kbilgi,pssname,pss):
        gelen_dict = {"şifre adı":pssname,"şifre":pss}
        result = self.collectionuserpass.find({"kbilgi":kbilgi})
        result = list(result)
        if result == []:
            self.collectionuserpass.insert_one({"kbilgi":kbilgi,"eklenen":[gelen_dict]})
            print("eklendi")
        else:
            eklenen_list = result[0]["eklenen"]
            eklenen_list.append(gelen_dict)
            self.collectionuserpass.update_one({"kbilgi":kbilgi},{"$set":{"kbilgi":kbilgi,"eklenen":eklenen_list}})
            print("eklendi")
    def delete(self,kbilgi,passwd2,pssname):
        result = self.collectionuser.find({"telefon numarası":kbilgi,"Fon şifresi":passwd2})
        result = list(result)
        result2 = self.collectionuserpass.find({"kbilgi":kbilgi})
        result2 = list(result2)
        if self.kontrol(result2) == True:
            eklenen = result2[0]["eklenen"]
            eklenecek = eklenen
            if result == []:
                return False
            else:
                for i in eklenen:
                    if i["şifre adı"] == pssname:
                        eklenecek.remove(i)
                        self.collectionuserpass.update_one({"kbilgi":kbilgi},{"$set":{"kbilgi":kbilgi,"eklenen":eklenecek}})
                        return True
        else:
            return False
    def forget(self,kbilgi,passwd2):
        result = self.collectionuser.find({"telefon numarası":kbilgi,"Fon şifresi":passwd2})
        result = list(result)
        if self.kontrol(result) == True:
            lis = [result[0]["telefon numarası"],result[0]["şifre"]]
            return lis
        else:
            return False
    def all_pass(self,kbilgi):
        result = self.collectionuserpass.find({"kbilgi":kbilgi})
        result = list(result)
        if self.kontrol(result) == True:
            eklenen = result[0]["eklenen"]
            listee = []
            for i in eklenen:
                listee.append(i["şifre adı"])
            return listee
        else:
            return []
    def kontrol(self,result):
        if result == []:
            return False
        else:
            return True
    def update_bilgi(self,kbilgi,change,passwd2,newchange):
        result = self.collectionuser.find({"telefon numarası":kbilgi,"Fon şifresi":passwd2})
        result = list(result)
        if self.kontrol(result) == True:
            result[0][change] = newchange

            self.collectionuser.update_one({"telefon numarası":kbilgi},{"$set":{"telefon numarası":result[0]["telefon numarası"],"şifre":result[0]["şifre"],"Fon şifresi":passwd2}})

            return True
        else:
            return False