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

print("="*70)
print("FAKTUR TAGIHAN".center(70))
print("="*70)

print(f"Perusahaan : {perusahaan}")
print(f"Alamat     : {alamat}")
print(f"Telepon    : {telepon}")

print("-"*70)
print(f"No Faktur  : {no_faktur}")
print(f"Tanggal    : {tanggal}")
print(f"Pembeli    : {nama_pembeli}")
print(f"Alamat     : {alamat_pembeli}")
print("-"*70)

print("DAFTAR JASA")
for i, j in enumerate(jasa, start=1):
    print(f"{i}. {j[0]} - {rupiah(j[1])}")

print("-"*70)
print(f"Subtotal : {rupiah(subtotal)}")
print(f"PPN 10%  : {rupiah(ppn)}")
print(f"Total    : {rupiah(total)}")
print(f"Terbilang: {terbilang(total)} rupiah")
print("="*70)