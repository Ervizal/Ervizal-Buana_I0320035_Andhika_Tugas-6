#membuat judul program
print("=========================================")
print("==== Program Pengulangan Hello World ====")
print("=========================================")

#menyimpan text dalam variabel
text = "Hello World!"

#pengulangan teks menggunakan while
i = 1
while i <= 10:
    print(text, "ke-%d" % i)
    i += 1