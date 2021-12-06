# Sumber : https://www.youtube.com/watch?v=aBZru0Z-GyY&ab_channel=kyuu-chan

# Nama : Muchamad Fahmi
# NIM  : 0110221015
# Kelas: TI16

import cmath as cm

print('Bentuk persamaan kuadrat : ax2 + bx + c')

#input
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

#Memastikan nilai (tidak nol) a = 0
if a==0 :
    print('Nilai a tidak boleh nol')
else :
    D = b**2 -4*a*c
    #Cek Nilai Diskriminan
    if D>0:
        x1 = (-b+cm.sqrt(D))/(2*a)
        x2 = (-b-cm.sqrt(D))/(2*a)
        print('Jenis akarnya adalah 2 akar berbeda dan real')
    elif D==0 :
        x1 = (-b/(2*a))
        x2 = (-b/(2*a))
        print('Jenis akarnya adalah 2 akar kembar dan real')
    else :
        x1 = (-b+cm.sqrt(D))/(2*a)
        x2 = (-b-cm.sqrt(D))/(2*a)
        print('Jenis akarnya adalah 2 akar berbeda dan imajiner')

print('Akar dari persamaan kuadrat adalah '+str(x1)+' dan '+str(x2))

print('dengan Diskriminan : ',D)