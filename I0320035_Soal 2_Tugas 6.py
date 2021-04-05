#membuat judul program
print("======================================")
print("==== Program Menghitung Rata-Rata ====")
print("======================================")

#membuat list yang akan diisi angka
angka = []

#memasukkan input angka dengan append
n = int(input("Masukkan jumlah angka yang akan di rata-rata : "))
for i in range(n):
	angka.append(float(input("masukkan angka ke-%d : " % (i+1))))

#menghitung rata-rata
jumlah = 0
for i in range(n):
	jumlah += angka[i]
jumlah /= n

#menampilkan hasil rata-rata bilangan
print("Hasil rata-rata dari bilangan yang anda masukkan adalah", format(jumlah, ".2f"))