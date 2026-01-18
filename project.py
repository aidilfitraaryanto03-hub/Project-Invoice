def rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")

def terbilang(n):
    angka = ["nol","satu","dua","tiga","empat","lima","enam","tujuh","delapan","sembilan",
             "sepuluh","sebelas"]
    if n < 12:
        return angka[n]
    elif n < 20:
        return terbilang(n-10) + " belas"
    elif n < 100:
        return terbilang(n//10) + " puluh " + terbilang(n%10)
    elif n < 200:
        return "seratus " + terbilang(n-100)
    elif n < 1000:
        return terbilang(n//100) + " ratus " + terbilang(n%100)
    elif n < 2000:
        return "seribu " + terbilang(n-1000)
    elif n < 1000000:
        return terbilang(n//1000) + " ribu " + terbilang(n%1000)
    else:
        return "jumlah terlalu besar"

<<<<<<< HEAD
print("=" * 70)
print("FAKTUR TAGIHAN".center(70))
print("=" * 70)
=======
print("="*70)
print("FAKTUR TAGIHAN".center(70))
print("="*70)
>>>>>>> 36cb63f62639cbfcf1f8728d7049e4281406862a

perusahaan = input("Nama Perusahaan : ")
alamat = input("Alamat Perusahaan : ")
telepon = input("Telepon : ")

<<<<<<< HEAD
print("-" * 70)
=======
print("-"*70)
>>>>>>> 36cb63f62639cbfcf1f8728d7049e4281406862a

no_faktur = input("No Faktur : ")
tanggal = input("Tanggal : ")
nama = input("Nama Pembeli : ")
alamat_pembeli = input("Alamat Pembeli : ")

<<<<<<< HEAD
print("=" * 70)
=======
print("="*70)
>>>>>>> 36cb63f62639cbfcf1f8728d7049e4281406862a

jumlah_jasa = int(input("Jumlah jasa : "))

total = 0

for i in range(jumlah_jasa):
    print(f"\nJasa ke-{i+1}")
    nama_jasa = input("Nama jasa  : ")
    harga = int(input("Harga jasa : "))
    total += harga

# === PERHITUNGAN TAMBAHAN SESUAI FAKTUR ===
margin = total * 30 // 100
net = total - margin
dpp = total
ppn = dpp * 10 // 100
grand_total = net + ppn

print("=" * 70)
print(f"No Faktur  : {no_faktur}")
print(f"Tanggal    : {tanggal}")
print(f"Pembeli    : {nama}")
print(f"Alamat     : {alamat_pembeli}")
print("-" * 70)

<<<<<<< HEAD
print(f"Subtotal     : {rupiah(total)}")
print(f"Margin 30%   : {rupiah(margin)}")
print(f"Net          : {rupiah(net)}")
print(f"DPP          : {rupiah(dpp)}")
print(f"PPN 10%      : {rupiah(ppn)}")
print(f"Grand Total  : {rupiah(grand_total)}")
print(f"Terbilang    : {terbilang(grand_total)} rupiah")
print("=" * 70)
=======
print("DAFTAR JASA")
for i, j in enumerate(jasa, start=1):
    print(f"{i}. {j[0]} - {rupiah(j[1])}")

print("-"*70)
print(f"Subtotal : {rupiah(subtotal)}")
print(f"PPN 10%  : {rupiah(ppn)}")
print(f"Total    : {rupiah(total)}")
print(f"Terbilang: {terbilang(total)} rupiah")
print("="*70)

#END
>>>>>>> 36cb63f62639cbfcf1f8728d7049e4281406862a
