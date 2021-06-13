'''
Pembelian Printer 
'''
harga=660000
jwb="y"
while jwb=="y" or jwb=="Y":
    qty=1
    while int(qty)>0:
        print("============================")
        print("  Jumlah Pembelian Printer")
        print("============================")
        qty=input("Masukkan Jumlah Pembelian = ")
        if int(qty)>0:
            totalbeli=int(qty)* 660000
            print("Rp."+str(totalbeli))
                #Cek Diskon
            if totalbeli>1500000:
                nilaidisk=totalbeli* 0.15
                print("Diskon = " + str(nilaidisk))
                #Hitung Total Pembelian
                total=totalbeli-nilaidisk
                print("Total Pembelian = Total Pesanan Rp."+ str(totalbeli) + " - Diskon Rp."+ str(nilaidisk) + " = Pembayaran Rp."+ str(total) ) 
            jwb=input("Masukkan Transaksi Lain ? y/t = ")
            if jwb=="t" or jwb=="T":
                break
        else:
            pesan="Masukkan Jumlah Yang Benar !!"
            break

