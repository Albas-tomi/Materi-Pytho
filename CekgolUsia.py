"""
Cek Golongan Usia
"""
jwb="y"
while jwb=="y" or jwb=="Y":
    print("=====================")
    print("  Cek Golongan Usia")
    print("=====================")
    while int(u)>0 and int(u)<=100:
        u= input("Masukkan Usia Anda =  ")
        if int(u)>0 and int(u) <= 100:
            if int(u)>=60:
                sts="Lansia"
            elif int(u) >= 35:
                sts="Dewasa"
            elif int(u) >= 18:
                sts="Pemuda"
            elif int(u) >= 15:
                sts="Remaja"
            else:
                sts="Anak-anak"
            print(sts)

            jwb=input("Masukkan Nilai Lagi ? y/t = ")
            if jwb == "t" or jwb == "T":
                break
        else:
            pesan="Masukkan Angka 1 - 100 !!"
            print(pesan)
            break
