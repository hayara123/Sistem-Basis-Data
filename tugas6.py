nama = []
nim = []
jurusan = []
print("-----------------------DATA DIRI-------------------")
pilihan=1
while(pilihan!=0):
    print("""
1. Tampilkan biodata
2. Tambah biodata
3. Hapus biodata
0. Keluar
""")
    pilihan=int(input("masukkan pilihan = "))
    if pilihan==1 :
        print ("Nama  NIM  Jurusan ")
        for i in range (len (nim)):
            print(nama[i]["nama"],"|",nim[i]["nim"],"|",jurusan[i]["jurusan"],"|")
    elif pilihan==2 :
        namasaya=input("masukkan nama = ")
        nama.append({"nama" : namasaya})
        nimsaya=input("masukkan NIM = ")
        nim.append({"nim" : nimsaya})
        jurusansaya=input("masukkan jurusan = ")
        jurusan.append({"jurusan" : jurusansaya})
    else :
        jurusansaya=input("masukkan jurusan = ")
        for i in range (len(jurusan)):
            if jurusansaya == jurusan[i]['jurusan']:
                print(i)
                del nama [i]
                del nim [i]
                del jurusan [i]
                break
