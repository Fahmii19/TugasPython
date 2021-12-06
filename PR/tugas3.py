#Tugas3
#Soal : . Buat fungsi untuk membuat list baru berisi isi list buah2an tetapi terduplikasi

def duplikasi(buah):
    index = len(buah)
    list_buah = []
    for i in range(len(buah)):
        list_buah.append(buah[i])
        list_buah.append(buah[i])
    print(list_buah)

duplikasi(['pepaya','mangga','pisang','durian','jambu'])