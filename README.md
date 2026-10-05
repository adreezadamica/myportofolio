Nama: Damica Adreeza Ramadhan

NPM: 2506625193

Kelas: PBP B

### Tugas 5

1. Debouncing adalah teknik menunda eksekusi suatu fungsi sampai user berhenti melakukan aksi selama waktu tertentu. Di halaman Experience, kolom cari memakai setTimeout 300 ms, dan timer di-reset (clearTimeout) setiap kali user mengetik lagi. Request baru dikirim hanya kalau user berhenti mengetik selama 300 ms.

Ini penting karena tanpa debouncing, mengetik "backend" (7 huruf) bisa mengirim 7 request. Akibatnya server terbebani, jaringan terpakai sia-sia, dan hasil request lama bisa tiba setelah yang baru sehingga tampilan salah. Dengan debouncing, request jauh lebih sedikit.

2. fetch() mengembalikan sebuah Promise, bukan data langsung, karena permintaan ke server perlu waktu. await memberi jeda eksekusi fungsi async sampai Promise selesai, lalu memberi hasilnya (objek Response) tanpa memblokir halaman. Contohnya di fetchExperiences: const response = await fetch(url) dan const data = await response.json().

Kalau tidak pakai await, variabel response hanya berisi Promise yang belum selesai. Kode selanjutnya langsung jalan, jadi response.ok atau response.json() bekerja pada objek yang belum siap. Hasilnya daftar tidak tampil atau muncul error, dan try/catch tidak menangkap error dari request itu.

3. XSS adalah salah satu jenis serangan ketika seseorang menyisipkan skrip berbahaya, misalnya `<script>...</script>`, melalui input yang kemudian ditampilkan kepada user lain. Jika input tersebut tidak ditangani dengan baik, skrip bisa dijalankan di browser korban. Dampaknya bisa berupa pencurian cookie sesi, perubahan tampilan halaman, atau bahkan menjalankan aksi tertentu menggunakan akun korban.

Pada template Django, variabel yang ditulis menggunakan {{ variabel }} secara default sudah melalui proses auto-escape. Misalnya, karakter < akan diubah menjadi &lt;, sehingga kode HTML yang dimasukkan oleh user hanya ditampilkan sebagai teks dan tidak dijalankan oleh browser.

Namun, pada JavaScript saya menggunakan innerHTML untuk membuat HTML secara dinamis menggunakan template string. Berbeda dengan template Django, innerHTML tidak melakukan escape secara otomatis. Oleh karena itu, jika data dari server langsung dimasukkan ke dalam innerHTML, data tersebut berpotensi mengandung HTML atau script berbahaya yang kemudian dijalankan oleh browser.

Untuk mengatasinya, saya menggunakan fungsi escapeHtml di sisi JavaScript sebelum memasukkan data ke dalam HTML. Selain itu, pada sisi server saya juga menggunakan strip_tags di clean_`<field>` pada ModelForm. Dengan begitu, terdapat perlindungan dari dua sisi: data dibersihkan di server dan juga di-escape sebelum digunakan untuk membuat HTML di browser.

# AI Disclosure: Saya menggunakan Claude Sonnet 5.5 sebagai alat bantu dalam mengerjakan tugas ini, terutama untuk memandu penerapan pola Tutorial 5 ke halaman Experience. Saya menerapkan, menjalankan dan menguji hasilnya pada semua peran (pengunjung, user biasa, dan superuser), menghubungkannya ke proyek saya, serta memutuskan sendiri pilihan seperti menambahkan fitur star pada Experience. 