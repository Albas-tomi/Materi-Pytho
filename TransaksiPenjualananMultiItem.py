# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 11:17:35 2021
@author: x220
"""
def FungsiBarang():
    global hrgsat
    global qty
    global nm_brg
    global total1
    print("  __>>>DAFTAR MENU <<<___ ")
    print(" ")
    print("MENU MAKANAN -->>")
    print(" ")
    print("a.Nasi Goreng        15.000")
    print("b.Lontong Goreng     14.900")
    print("c.Bakso Goreng       12.900")
    print("d.Rujak Goreng       13.000")
    print("e.Rujak Bakso        15.000")
    print("f.Rujak Bakco Pecel  17.000")
    
    #1. SIAPKAN VARIABEL
    kode =['a','b','c','d','e','f']
    namaBarang = [' Nasi Goreng',' Lontong Goreng',' Bakso Goreng','Rujak Goreng','Rujak Bakso','Rujak Bakso Pecel']
    harga = [15000,14900,12900,13000,15000,17000]
    
    #2. INPUT PILIHAN
    pilihan = input(">> Masukkan Kode Barang    = ")
    
    #3. INPUT QTY
    qty     = input(">> Masukkan Jumlah Barang  = ")
    
    #4. HITUNG BAYAR
    ##cek nama barang dan ambil harga satuan
    i = 0
    while i<len(namaBarang):
        #jika value pada list kode[i] == pilihan
        if kode[i] == pilihan:
            #ambil nama barang
            nm_brg = namaBarang[i]    
            #ambil harga satuan
            hrgsat = harga[i]
        #jika tidak cocok, lanjut ke i berikutnya
        i+=1
    total1 = hrgsat * int(qty)
    print("Pilihan Menu Makanan = " + nm_brg )
    print("Jumlah makanan       = " + str(qty))
    
FungsiBarang()
total2=0
def fungsiminuman():
    global jml
    global minum
    global total2
    global hrg
    print(" ")
    print("MENU MINUMAN -->>")
    print("a.Teh Dingin/Hangat/Panas  2.500")
    print("b.Kopi Dingin              5.000")
    print("c.Kopi Teh Panas           6.500")
    print("d.Coca Cola Dingin         3.500")
    print("e.Coca Cola Panas          5.000") 
    
    kode=['a','b','c','d','e']
    minuman =['Teh Dingin/Hangat/Panas','Kopi Dingin','Kopi Teh Panas','Coca Cola Dingin','Coca Cola Panas']
    harga =[2500,5000,6500,3500,5000]
        
    #memilih menu
    pilihan = input("-->> Masukkan Kode Menu = ")
    #Jumlah
    jml     = input("-->> Masukkan Jumlah    = ")
    
    #hitung bayar
    i=0
    while i<len(minuman):
        #jika value pada list kode[i] == pilihan
        if kode[i] == pilihan:
            #ambil nama barang
            minum = minuman[i]
            #ambil harga satuan
            hrg= harga[i]  
        #jika tidak cocok, lanjut ke i berikutnya
        i+=1
    total2=hrg*int(jml)
    print("Pilihan Menu Minuman = " + minum)
    print("Jumlah Minuman       = " + str(jml))
fungsiminuman()

totalsemua=0 
totalsemua=total1+total2
print(" ")
print("=================================")
print("======= S T R U K   B E L I =====")
print("=================================")
uang=int(input("Uang tunai Pembeli  =  Rp."))
kembalian=int(uang-totalsemua)
print("Beli Makanan     = " + nm_brg + " "+str(qty) + " x Rp." +str(hrgsat))
print("Beli Minuman     = " + minum + " "+str(jml) + " x Rp." + str(hrg))
print("Total Makanan    = " + " Rp."+str(total1))
print("Total Minuman    = " + " Rp."+str(total2))
print("====================================== +")
print("Total Pembelian  = " + " Rp."+str(totalsemua))
print("====================================== -")
print("Kembalian        = " + str(kembalian))