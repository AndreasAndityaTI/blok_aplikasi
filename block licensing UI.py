aplikasi=input("Masukkan nama aplikasi : ") #LicensingUI.exe
import os
while(True):
    os.system(f"taskkill /im {aplikasi}") # select process by its name
    os.system('cls')
