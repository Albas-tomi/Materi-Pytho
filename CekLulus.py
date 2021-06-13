'''
Cek Kelulusan Nilai
'''
jwb="y"
while jwb=="y" or jwb=="Y":
    n=1
    while int(n)>0 and int(n)<=100:
        print("=====================")
        print("    Cek Kelulusan")
        print("=====================")
        n = input("Masukkan Nilai = ")
        if int(n)>0 and int(n)<=100:
            if int (n) >= 60:
                sts = "LULUS"
            else: 
                sts = "ULANG"
            print(sts)
            jwb=input("Masukkan Nilai Lagi ? y/t = ")
            if jwb == "t" or jwb == "T":
                break
        else:
            pesan="Masukkan Angka 1 - 100 !!"
            print(pesan)
            break