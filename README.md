<h1 align="center"> Tugas Kecil 2 IF2211 Strategi Algoritma </h1>
<h1 align="center">  Membangun Kurva Bézier dengan Algoritma Titik Tengah berbasis <em> Divide and Conquer </em> </h1>


## General Information
Program ini mengimplementasikan algoritma *Divide and Conquer* untuk pembentukan kurva Bézier, yang merupakan kurva parametrik ditentukan oleh serangkaian titik kontrol. Dalam proses pembentukannya, algoritma ini memulai dengan kurva Bézier linier antara dua titik kontrol, kemudian menambahkan titik kontrol tambahan untuk membentuk kurva Bézier kuadratik, kubik, kuartik, dan seterusnya. Dengan membagi masalah menjadi submasalah yang lebih kecil dan menggabungkan solusi, program memungkinkan pengguna untuk menentukan jumlah titik kontrol dan iterasi, serta menampilkan kurva Bézier yang dihasilkan, dengan penanganan pesan kesalahan yang sesuai jika terjadi kesalahan dalam input.


## Technology Used
- Python
- pip numpy library
- pip matplotlib.pyplot library
- pip matplotlib.animation library
- pip tkinter library
- pip PIL library


## Contributors
|   NIM    |                  Nama                  |
| :------: | :------------------------------------: |
| 13522053 |       Erdianti Wiga Putri Andini       |
| 13522108 |          M. Neo Cicero Koda            |



## Project Structure
```bash
.
│   README.md
│
├───bin                                   
│
├───doc  
│   └─── Laporan
│                      
├───src                             # Program
│   └─── assets                     # Folder untuk menyimpan gambar yang digunakan pada GUI 
│           ├─── background.png      
│           └─── background2.png      
│   ├─── bezier.py 
│   ├─── bruteforce.py 
│   ├─── dnc_n.py 
│   ├─── dnc.py 
│   ├─── GUI.py 
│   ├─── input.py 
│   ├─── main.py 
│   └─── util.py                       
│  
└───test                            # Testing cases
    ├─── case1_bf.txt             
    ├─── case1_gui.txt             
    ├─── case2_bf.txt
    ├─── case2_gui.txt
    ├─── case3_bf.txt
    ├─── case3_gui.txt
    ├─── case4_bf.txt
    ├─── case4_gui.txt
    ├─── case5_bf.txt
    ├─── case5_gui.txt
    ├─── case6_bf.txt
    ├─── case7_dnc.txt
    ├─── case7_gui.txt
    ├─── case8_dnc.txt
    ├─── case8_gui.txt
    ├─── case9_dnc.txt
    ├─── case10_dnc.txt
    ├─── case11_dnc.txt
    ├─── case12_dnc.txt
    └─── case13_invalidinput.txt
```


## How to Run (CLI)
1. Clone repository ini dengan mengetikkan `git clone https://github.com/wigaandini/Tucil2_13522053_13522108` pada terminal.
2. Pindah ke direktori src dengan `cd src`.
3. Run file dengan `python main.py"`.
4. Input algoritma yang ingin digunakan (1 untuk brute force, 2 untuk divide and conquer).
5. Input jumlah titik yang diinginkan (n).
6. Input titik-titik yang diinginkan sejumlah n dengan dipisahkan spasi (e.g. 1 3, -5 0, -2 -19).
7. Input jumlah iterasi yang diinginkan.
8. Bila memilih algoritma brute force, input nilai t.
9. Jika semua tipe input benar, maka program akan menampilkan titik-titik kurva, waktu eksekusi, dan animasi pembentukan kurva beserta waktu eksekusi tiap iterasi.


## How to Run (GUI)
1. Clone repository ini dengan mengetikkan `git clone https://github.com/wigaandini/Tucil2_13522053_13522108` pada terminal.
2. Pindah ke direktori src dengan `cd src`.
3. Run file dengan `python GUI.py`.
4. Tekan tombol 'Let's Make Bézier Curve!'.
5. Input jumlah titik yang diinginkan (n).
6. Input titik-titik yang diinginkan sejumlah n dengan dipisahkan spasi (e.g. 1 3, -5 0, -2 -19).
7. Input jumlah iterasi yang diinginkan.
8. Tekan tombol 'Show the Bézier Curve'.
9. Jika semua tipe input benar, maka program akan menampilkan animasi pembentukan kurva beserta waktu eksekusi tiap iterasi.


## Additional Notes
Program ini dibuat dan dites menggunakan Python versi 3.10.11.
Jika Anda belum menginstal library yang diperlukan, silakan instal terlebih dahulu menggunakan perintah berikut.
|    Library    |         How to Install          |
| :-----------: | :-----------------------------: |
|     numpy     |       `pip install numpy`       |
|   matplotlib  |     `pip install matplotlib`    |
|      PIL      |       `pip install Pillow`      |
|    tkinter    |         `pip install tk`        |
