#Tugas4
#Buat fungsi untuk membuat string baru berisi hanya konsonan dari string fungsi

def konsonan(kata):
    value_kata = kata
    vokal = ['a','e','i','o','u','']
    for x in kata.lower():
        if x in vokal:
            value_kata = value_kata.replace(x, "")
    print(value_kata)

konsonan("Nurul Fikri")
