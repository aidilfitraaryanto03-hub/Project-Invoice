jumlah_jasa = int(input("Jumlah jasa : "))

jasa = []
subtotal = 0

for i in range(jumlah_jasa):
    print(f"\nJasa ke-{i+1}")
    nama_jasa = input("Nama jasa : ")
    harga = int(input("Harga jasa : "))
    jasa.append((nama_jasa, harga))
    subtotal += harga

ppn = int(subtotal * 0.10)
total = subtotal + ppn