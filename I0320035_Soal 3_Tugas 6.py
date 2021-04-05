#membuat judul program
print("===========================================")
print("==== Program Pengecekan Bilangan Prima ====")
print("===========================================")
    
#menyimpan input bilangan dalam suatu variabel
num = int(input("Masukkan bilangan : "))
p = 0
#membagi jenis bilangan
if(num >= 1):
    for i in range(1, num+1):
        angka = i
        for j in range(1, i+1):
            if (i % j) == 0:
                p += 1
            else:
                continue
        if(p == 2):
            print("%d adalah bilangan prima" % angka)
        else:
            print("%d bukan prima" % angka)
        p = 0
else:
    print("Input anda tidak tepat")