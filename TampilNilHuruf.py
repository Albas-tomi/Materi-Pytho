'''
Menampilkan Nilai Huruf Dari Bilangan Bulat 0 - 100
'''
jwb="y"
while jwb=="y" or jwb=="Y":
    n=1
    while int(n) > 0 and  int(n) <= 100:
        print("========================")
        print("         Cek Nilai     ")
        print("========================")
        n=input("Masukkan Nilai = ")
        if int(n) > 0 and  int(n) <= 100:
            if int(n) > 80:
                sts="Baik Sekali"
            elif int(n) >=65:
                sts= "Baik"
            elif int(n) >=55:
                sts= "Cukup"
            elif int(n) >=40:
                sts= "Kurang"
            else:
                sts="Kurang Sekali"
            print(sts)
            jwb=input("Masukkan Nilai Lagi ? y/t = ")
            if jwb=="t" or jwb=="T":
                break
        else:
            pesan=print("Masukkan Angka 1 - 100 saja !!!")
            break
