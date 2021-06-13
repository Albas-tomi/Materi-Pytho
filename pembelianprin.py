'''
Pembelian Printer 
'''
jwb="y"
harga=660000
while jwb=="y" or jwb=="Y":
     qty=1
     while int(qty) > 0:
        print("============================")
        print("  Jumlah Pembelian Printer")
        print("============================")
        qty=input("Masukkan Jumlah Pembelian = ")
        if int(qty)>0:
            totalbeli=int(qty)*int(harga)
            print(totalbeli)
            jwb=input("Masukkan Transaksi Baru ? y/t = ")
            if jwb=="t" or jwb=="T":
                break
        else:
            pesan=("Masukkan Jumlah Yang Benar !!")
            print(pesan)
            break