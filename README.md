# TUGAS KECIL 3
> Tugas Kecil 3 Strategi Algoritma IF2122

## Pembagian Tugas
<table>
    <tr>
        <td>No.</td>
        <td>Nama</td>
        <td>NIM</td>
	<td>Pembagian Kerja</td>
    </tr>
    <tr>
        <td>1.</td>
        <td>Afifah Fathimah Qur'ani</td>
        <td>13519183</td>
	<td>1. Algoritma A*<br/>
	2. Buat testcase</td>
    </tr>
    <tr>
        <td>2.</td>
        <td>Awwala Nisa Kamila</td>
        <td>13519208</td>
	<td>1. Program untuk baca file testcase<br/>
	2. Buat laporan<br/>
    3. Visualisasi graf </td>
    </tr>
</table>

## Cara menjalankan program
1. Pastikan sudah terinstall python
2. Buka terminal di direktori Tucil3-Stima
3. run kode graf.py di direktori Tucil3-Stima/src
4. apabila file testcase tidak dapat dibaca, ubah kode pada fungsi readfile dan fungsi readposisi dari "../test" menjadi "./test/" atau sebaliknya
5. masukkan nama file graf dan file posisi/koordinat (dua file terpisah)
6. masukkan simpul asal dan simpul tujuan
7. program akan menampilkan path solusi

## Cara menjalankan program yang telah ada visualisasi graf
1. buka folder src/.ipynb_checkpoints dan pilih file printGraf.ipynb
2. Ganti path file pada line 9 :
file = open('C:\\Users\\Asus\\Documents\\Tubes 3 Stima\\test\\' + namafilegraf + '.txt', 'r')
menjadi 
file = open(direktori penyimapan file + namafilegraf + '.txt', 'r'
3. Ganti path file pada line 22 :
file = open('C:\\Users\\Asus\\Documents\\Tubes 3 Stima\\test\\' + namafileposisi + '.txt','r')
menjadi
file = open(direktori penyimapan file + namafileposisi + '.txt','r')
4. Masukkan nama file graf pada perintah "Masukkan file graf : " yang muncul dalam bentuk popup
5. Masukkan nama file posisi/koordinat pada perintah "Masukkan file posisi : " yang muncul dalam bentuk popup
6. masukkan simpul asal pada perintah "Masukkan simpul asal : " yang muncul dalam bentuk popup
6. masukkan simpul tujuan pada perintah "Masukkan simpul tujuan: " yang muncul dalam bentuk popup 
7. program akan menampilkan path solusi jarak terdekat dari simpul asal ke simpul tujuan yang ditandai dengan simpul berwarna kuning