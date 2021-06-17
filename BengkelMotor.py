jwb="y"
while jwb=="y" or jwb=="Y":
    print("==============================")
    print("=     BENGKEL MOTOR UD       =")
    print("==============================")
    print("        IBU SUNH HIN         ")
    print("==============================")
    print("= LIST HARGA :        ")
    print("=  A.Duration SW20 1L      = Rp.53000 ")
    print("=  B.Castrol Magnatec 1L   = Rp.50000 ")
    print("=  C.Federal Supreme XX 1L = Rp.54000 ")
    print("=  D.Yamalube 1L           = Rp.45000 ")
    print("=  E.Shell 1L              = Rp.46000 ")
    print("==============================")
    merk=['Duration SW20 1L','Castrol Magnatec 1L','Federal Supreme XX 1L','Yamalube 1L','Shell 1L','x']
    harga = [53000,50000,54000,45000,46000,0]

    pilihan=input(">>>Masukkan Kode Barang Pembelian = ")
    jumlah=int(input(">>> Jumlah Oli = "))
    if pilihan=="a" or "A":
        idx = 0
    elif pilihan=="b" or "B":
        idx = 1
    elif pilihan=="c" or "C":
        idx = 2
    elif pilihan=="d" or "D":
        idx = 3
    elif pilihan=="e" or "E":
        idx = 4 
    else:
        idx=5
        
    print(">>> Merk   = " + merk[idx])
    print(">>> Harga  = " + str(harga[idx]))
    print(">>> Jumlah = " + str(jumlah))

    total=jumlah*harga[idx]
    ppn=total*0.01
    bayar=total+ppn

    print("PPN  = " + str(ppn))
    print("Total Pembayaran + PPN = " + str(bayar))

    if bayar>=200000:
        diskon=bayar*0.05
        hargadiskon=bayar-diskon
        print(">> Diskon 5%")
        print(">> Total bayar = Rp"+str(hargadiskon))
        print("--------------------------------------")
    jwb=input("Masukkan Transaksi Lain ? y/t = ")
    if jwb=="t" or jwb=="T":
        break