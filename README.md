Nama: Damica Adreeza Ramadhan

NPM: 2506625193

Kelas: PBP B

### Tugas 6

1. REST (Representational State Transfer) merupakan sebuah arsitektur perancangan web API yang menempatkan data sebagai resource. Di arsitektur ini, URL bertindak sebagai penunjuk alamat dari resource tersebut, sementara jenis tindakan yang akan dieksekusi ditentukan oleh HTTP Method seperti GET, POST, PUT, PATCH, dan DELETE. Mengembalikan format data JSON saja belum otomatis membuat sebuah API menjadi RESTful. Sebuah API baru dapat dikategorikan RESTful kalau memenuhi kaidah dasar arsitektur REST, yaitu memanfaatkan HTTP method secara semantik, menggunakan status HTTP balasan yang sesuai (seperti 200, 201, 204, 400, 403, atau 404), menjaga sifat stateless, serta mengelola resource melalui struktur endpoint yang konsisten.

Perbedaan utama antara PUT dan PATCH terletak pada cakupan pembaruan datanya. Method PUT digunakan ketika kita ingin mengganti atau memperbarui seluruh representasi resource secara utuh, sehingga jika ada field wajib yang absen dari payload, request tersebut akan ditolak. Contoh penggunaannya adalah saat pengguna mengirimkan ulang seluruh isi formulir pengalaman kerja dari awal. Sebaliknya, PATCH digunakan untuk pembaruan sebagian (partial update) tanpa mengganggu field lain yang tidak dikirimkan. Contoh penerapan PATCH adalah ketika kita hanya ingin mengubah judul suatu pengalaman kerja melalui fitur inline editing tanpa perlu mengirimkan ulang deskripsi maupun tanggalnya.

2. Serializer pada Django REST Framework berfungsi sebagai jembatan dua arah (serialization dan deserialization) antara instance objek Django dan data JSON. Saat membaca data, serializer mengubah objek kompleks seperti QuerySet menjadi tipe data bawaan Python yang siap dirender ke JSON. Saat menerima data dari klien, serializer bertugas menangkap input mentah, memvalidasi aturan tiap field, serta mengonversinya menjadi objek Python yang siap disimpan ke database.

Menggunakan serializer memberi keuntungan besar dibanding merakit manual dengan JsonResponse. Serializer menyediakan mekanisme validasi terpusat yang otomatis menangani pembersihan HTML (strip_tags) dan pengecekan tipe data tanpa memerlukan perulangan kode manual. Selain itu, serializer mempermudah kontrol keamanan field (seperti menyembunyikan kredensial sensitif), mendukung pembuatan field hasil perhitungan (computed fields), dan secara otomatis menyusun struktur respons error per-field yang konsisten saat terjadi kesalahan input.

3. Autentikasi dan otorisasi menangani dua tahap keamanan yang berbeda. Autentikasi adalah proses mengidentifikasi siapa pengirim permintaan tersebut, yang dalam DRF dipetakan melalui SessionAuthentication untuk mengisi request.user. Sementara itu, otorisasi adalah proses menentukan apa saja tindakan yang diizinkan untuk identitas tersebut, yang dipetakan melalui permission class.

Pemeriksaan hak akses wajib dilakukan di sisi server menggunakan permission class karena pengamanan sisi klien (seperti menyembunyikan tombol di template HTML) hanya berfungsi untuk kenyamanan antarmuka (UX). Pengguna dapat dengan mudah melewati batas tampilan antarmuka dengan mengirimkan request HTTP secara langsung melalui browser DevTools, Postman, atau cURL. Tanpa verifikasi otorisasi di server, endpoint API tetap rentan dieksekusi oleh pihak yang tidak berhak.

4. Penggunaan SessionAuthentication mengandalkan cookie session yang dikirimkan secara otomatis oleh browser pada setiap request ke domain yang sama. Mekanisme ini membuka celah serangan Cross-Site Request Forgery (CSRF), di mana situs pihak ketiga yang berbahaya dapat memicu request manipulasi data memanfaatkan session pengguna yang sedang aktif. Untuk memastikan request tersebut benar-benar berasal dari aplikasi kita, header X-CSRFToken tetap wajib disertakan pada setiap permintaan yang mengubah data (POST, PUT, PATCH, DELETE).

Pengujian menggunakan force_authenticate tidak cukup untuk membuktikan berjalannya perlindungan CSRF karena metode tersebut menyuntikkan objek pengguna secara instan ke dalam request uji tanpa melalui alur middleware autentikasi session dan validasi token CSRF yang sebenarnya. Pembuktian nyata terhadap pengamanan CSRF memerlukan pengujian menggunakan APIClient(enforce_csrf_checks=True) yang menguji alur login session serta verifikasi token CSRF secara nyata.

# AI Disclosure: Saya menggunakan Gemini models 3 auto sebagai alat bantu dalam mengerjakan tugas ini, terutama untuk memahami konsep saat menjawab pertanyaan refleksi