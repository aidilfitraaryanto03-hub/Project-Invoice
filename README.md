coding ada di branch hendri
def rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")

def terbilang(n):
    if n == 0:
        return ""

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

print("=" * 70)
print("FAKTUR TAGIHAN".center(70))
print("=" * 70)

perusahaan = input("Nama Perusahaan : ")
alamat = input("Alamat Perusahaan : ")
telepon = input("Telepon : ")

print("-" * 70)

no_faktur = input("No Faktur : ")
tanggal = input("Tanggal : ")
nama = input("Nama Pembeli : ")
alamat_pembeli = input("Alamat Pembeli : ")

print("=" * 70)

jumlah_jasa = int(input("Jumlah jasa : "))

total = 0

for i in range(jumlah_jasa):
    print(f"\nJasa ke-{i+1}")
    nama_jasa = input("Nama jasa  : ")
    harga = int(input("Harga jasa : "))
    total += harga

# === PERHITUNGAN ===
margin = total * 30 // 100
net = total - margin
dpp = net              # FIX: DPP = Net
ppn = dpp * 10 // 100
grand_total = dpp + ppn

print("=" * 70)
print(f"No Faktur  : {no_faktur}")
print(f"Tanggal    : {tanggal}")
print(f"Pembeli    : {nama}")
print(f"Alamat     : {alamat_pembeli}")
print("-" * 70)

print(f"Subtotal     : {rupiah(total)}")
print(f"Margin 30%   : {rupiah(margin)}")
print(f"Net          : {rupiah(net)}")
print(f"DPP          : {rupiah(dpp)}")
print(f"PPN 10%      : {rupiah(ppn)}")
print(f"Grand Total  : {rupiah(grand_total)}")
print(f"Terbilang    : {terbilang(grand_total)} rupiah")
print("=" * 70)
