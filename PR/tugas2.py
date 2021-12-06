# Tugas2
# Soal : Buat fungsi untuk membuat list baru berisi urutan terbalik dari buah2an

def balikan(buah):
    index = len(buah)
    for i in buah:
        index -= 1
        print(buah[index])

balikan(['pepaya','mangga','pisang','durian','jambu'])