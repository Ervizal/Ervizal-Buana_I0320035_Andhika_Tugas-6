#membuat judul program
print("======================================================")
print("====== Program Menampilkan Deret Bilangan Prima ======")
print("======================================================")
    
#menyimpan input bilangan dalam suatu variabel
num1 = int(input("Masukkan bilangan awal : "))
num = int(input("Masukkan bilangan akhir : "))
p = 0
#membagi jenis bilangan
if((num1 and num) >= 1 ):
    for i in range(num1, num+1):                        #Membuat perulangan untuk menampilkan angka dari 1 - num
        angka = i                                       #Membuat cloning isi variabel i ke variabel angka
        for j in range(1, i+1):                         #Menggunakan perulangan untuk mengecek status bilangan (prima atau tidak)
            if (i % j) == 0:                            #Bilangan i akan di modulus bergantian dari 1 hingga j
                p += 1                                  #Jika bilangan i dapat di modulus j dan menghasilkan 0, nilai variabel p akan ter-increment
            else:
                continue                                #Jika bilangan i tidak dapat di modulus j atau hasilnya selain 0, akan dilanjutkan perulangan lagi
        if(p == 2):                                     #Ide utama dari pengecekan bilangan prima adalah bilangan prima hanya dapat dibagi habis oleh 2 bilangan
            print("%d adalah bilangan prima" % angka)   #Sehingga jika suatu bilangan jika dan hanya jika dapat dibagi 2 bilangan, bilangan tersebut adalah prima
        else:
            print("%d bukan prima" % angka)             #Selain aturan tersebut, bilangan tersebut bukanlah prima
        p = 0                                           #Nilai variabel p dikembalikan 0, sehingga saat perulangan berikutnya, nilai p adalah 0 kembali
else:
    print("Input anda tidak tepat")