
jwb="y"
while jwb=="y" or jwb=="Y":


    print("==============================")
    print("=   EKSPEDISI LORENA MALANG  =")
    print("==============================")
    print("=      KODE KOTA TUJUAN      =")
    print("==============================")
    print("=     1. SURABAYA =  A       =")
    print("=     2. BANDUNG  =  B       =")
    print("==============================")
    kota=['Surabaya','Bandung']
    jarak = [169,452,]
    ongkirperkm = [2500,4000]
    pilihan=input(">>>Masukkan Kode Tujuan = ")

    if pilihan=="a" or "A":
        idx = 0
    elif pilihan=="b" or "B":
        idx = 1
    else:
        pesan="Masukkan Kode yang Ada"

    print(">>> Pilihan Tujuan = " + kota[idx])
    print(">>> Jarak          = " + str(jarak[idx]) + " km")
    print(">>> Ongkir per km  = Rp. " + str(ongkirperkm[idx]))

    fixjarak = jarak[idx]
    fixongkirkm = ongkirperkm[idx]
    totongkir = fixjarak * fixongkirkm

    print(">>>-------------------------------------")
    print(">>> Total Biaya     = Rp." + str(totongkir))
    jwb=input("Masukkan Transaksi Lain ? y/t = ")
    if jwb=="t" or jwb=="T":
        break