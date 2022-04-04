# PUZZLE-15 SOLVER
Penyelesaian Puzzle-15 Game Board menggunakan algorima Branch & Bound

## Deskripsi Singkat
<img src="img/image2.png" alt="Alt text" title="Optional title">
Pada Tucil kali ini akan dibuat sebuah program problem solving dari Game Board Puzzle-15. Puzzle-15 Game  pustaka (library) myConvexHull dalam bahasa Python yang dapat mengembalikan convex hull dari kumpulan data 2 dimensi (dapat dianggap kumpulan titik 2 dimensi). Himpunan titik pada bidang planar disebut convex jika untuk sembarang dua titik pada bidang tersebut (misal p dan q), seluruh segmen garis yang berakhir di p dan q berada pada himpunan tersebut. Contoh gambar 1 adalah poligon yang convex, sedangkan gambar 2 menunjukkan contoh yang non-convex.

<img src="img/image1.png" alt="Alt text" title="Optional title">

## Requirement Program
Interpreter:
- python

Library:
- copy
- random
- time
- msvcrt

## Instalasi
Clone repositori ini dengan menggunakan command pada terminal:  
```
git clone https://github.com/Amike31/Tucil_Stima_3
```

## Menjalankan Program
### Menggunakan Source Code
- Masuk ke dalam folder hasil clone
- Jalankan program menggunakan command berikut:  
```
cd src ; py Main.py
```
- Setelah program berjalan, akan disediakan 3 buah cara pengambilan Puzzle-15 yang berbeda. Anda dapat memilih cara masukan yang diinginkan dan akan diarahkan melalui UI program.

## Output Program
* Setelah melakukan pemilihan cara masukan dan masukan puzzle, akan ditampilkan beberapa hal sebagai berikut:
    * Tabel KURANG(i)
    * Hasil Bounding_Function
    * Langkah-Langkah penyelesaian
    * Path yang dilalui
    * Waktu Eksekusi Implementasi Algoritma B&B
    * Banyak simpul yang dibangkitkan (simpul hidup)
    * Banyak langkah yang dibutuhkan

### Pengujian Author
Terdapat beberapa dataset Puzzle-15 di folder "test", Anda dapat memakainya sebagai dummy file.

## Author
Rahmat Rafid Akbar - 13520090
K03