#Tugas1
#Soal : Buat fungsi untuk menampilkan nama2 siswa yang lulus saja

def lulus_saja(hasil_akhir):
    peserta_lulus = []
    for data in hasil_akhir:
        if data['nilai'] > 65:
            peserta_lulus.append(data['nama'])
    return print(peserta_lulus)

hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40}
]

lulus_saja(hasil_akhir)

