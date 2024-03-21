#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Menentukan ganjil genap
nilai = int(input('Isikan nilai:'))
sisa_bagi = nilai % 2

if sisa_bagi==0:
    print(f'{nilai} adalah bilangan genap')
else :
    print(f'{nilai} adalah bilangan ganjil')
          
print('Program Selesai')          


# In[8]:


nilai_programan = int(input('Isikan Nilai Pemrograman:'))
if nilai_programan < 0 or nilai_programan > 100:
    print("Nilai Anda Salah")
else:
    if nilai_programan <50:
        print("E")
    elif nilai_programan <60:
        print("D")
    elif nilai_programan <70:
        print("C")
    elif nilai_programan <85:
        print("B")
    elif nilai_programan <=100:
        print("A")


# In[1]:


username = input('Isikan Username')
password = input('Isikan Password')

#Jika usename salah => username anda salah
#Jika password salah => password anda salah
#Jika keduanya salah => username dan password anda salah
#Jika keduanya benar => selamat datang {username}
#username: admin
#password: admin

if username == 'admin':
    if password == 'admin':
        print(f'selamat datang {username}')
    else:
        print(f'password anda salah')
        
else:
    if password == 'admin':
        print("username anda salah")
    else:
        print("username dan password anda salah")


# In[7]:


nama = input("masukan nama: ")
umur = int(input("masukan umur: "))
tempat_tinggal = input("masukan tempat_tinggal: ")
uang_tabungan = int(input("masukan uang_tabungan: "))

pangkat = ''
if umur > 40:
    if tempat_tinggal == 'nevada' or tempat_tinggal == 'new york' or tempat_tinggal == 'havana':
        if uang_tabungan > 10:
            pangkat = 'don'
elif umur >25 and umur <40:
    if tempat_tinggal == 'new jersey' or tempat_tinggal == 'manhattan' or tempat_tinggal == 'nevada':
        if uang_tabungan >= 1000000 and uang_tabungan <= 2000000:
            pangkat = 'underboss'
                
elif umur >18 and umur <24:
    if tempat_tinggal == 'california' or tempat_tinggal == 'detroit' or tempat_tinggal == 'boston':
        if uang_tabungan <1000000:
            pangkat = 'capo'

#lanjutkan kondisi percabangan...            
            
if pangkat !='':
    print(f'{nama} kemungkinan seseorang anggota mafia dengan pangkat {pangkat}')
else:
    print(f'{nama} tidak mencurigakan')


# In[ ]:




