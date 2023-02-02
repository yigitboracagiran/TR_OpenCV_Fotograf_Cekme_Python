#! /usr/bin/python3
import cv2
import os

kisiIsmi=input("Resmi Cekilen Kisinin Ismini Turkce Karakter Kullanmadan Giriniz: ") #Fotoğrafı çekilen kişinin ismi...
if os.path.isdir("dataset/" + kisiIsmi)==False:
    os.mkdir("dataset/" + kisiIsmi)
kamera=cv2.VideoCapture(0)
aciklama="Fotografi Cekmek Icin Bosluga, Cikmak Icin ESC'ye Basiniz."
cv2.namedWindow(aciklama, cv2.WINDOW_NORMAL)
cv2.resizeWindow(aciklama, 500, 500)
resimSayisi=0 #Klasorde onceden bulunan resim sayisi
while True:
    (kameraBasariylaAcildiMi, cerceve)=kamera.read()
    if not kameraBasariylaAcildiMi:
        print("Kamera Acilamadi!")
        break
    cv2.imshow(aciklama, cerceve)
    key=(cv2.waitKey(1))&(0xFF)
    if key==ord('q'): #Q tusuna basıldığında kapanır.
        print("Q Tuşuna Basildi. Kapatiliyor...")
        break
    elif key==ord(' '): #Boşluk Tuşuna Basıldığında Fotoğraf Çeker.
        resimAdi="dataset/" + kisiIsmi + "/image_{}.jpg".format(resimSayisi)
        cv2.imwrite(resimAdi, cerceve)
        print("{} Resim Cekildi!".format(resimAdi))
        resimSayisi+=1
kamera.release()
cv2.destroyAllWindows()
