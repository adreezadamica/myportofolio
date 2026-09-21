Nama: Damica Adreeza Ramadhan

NPM: 2506625193

Kelas: PBP B

### Tugas 1

1. Ya, saya menggunakan elemen semantik seperti `<section>` dan `<article>`. Pada website saya, `<section>` digunakan untuk membagi bagian utama website, seperti bagian Profile dan Currently Learning. Kemudian, `<article>` digunakan untuk setiap topik yang sedang saya pelajari pada bagian Currently Learning. Penggunaan elemen tersebut membuat struktur HTML saya lebih terorganisir dan lebih mudah dibaca karena setiap bagian memiliki fungsi yang jelas. Hal ini juga memudahkan saya ketika mengatur styling CSS untuk masing-masing bagian.

2. Tantangan responsive yang saya temukan adalah menyesuaikan layout desktop agar tetap nyaman dilihat di mobile. Pada desktop, beberapa elemen bisa diletakkan berdampingan, tetapi pada mobile lebih baik disusun menjadi satu kolom. Saya menggunakan media query untuk mengubah layout, ukuran gambar, dan spacing berdasarkan ukuran layar.

3. Tiap perubahan informasi masih harus dilakukan secara manual melalui kode HTML. Untuk pengembangan selanjutnya, saya ingin membuat bagian Projects menjadi dinamis, misal dengan menyimpan data project di database dan menampilkannya secara otomatis di website.

AI Disclosure: Dalam pengerjaan tugas ini, saya menggunakan ChatGPT sebagai alat bantu untuk memahami penggunaan HTML dan CSS, mencari alternatif struktur website, serta mendapatkan masukan mengenai responsive design. Beberapa saran dari ChatGPT saya gunakan sebagai referensi, kemudian saya sesuaikan kembali dengan kebutuhan dan desain website yang saya buat.

### Tugas 3

1. - Mengapa pakai ModelForm? Kalau membuat form HTML manual, kita harus mengetik tag input satu per satu, mencocokkan tipe data secara manual, membuat validasi sendiri, sampai menulis kode query untuk simpan ke database. ModelForm jauh lebih praktis karena langsung terhubung dengan model database yang sudah kita buat. ModelForm otomatis membuatkan input field, aturan validasi, dan label yang sesuai. Kita juga bisa langsung menyimpan data yang diisi pengguna ke database cukup dengan memanggil form.save(). Cara ini menghemat waktu dan mengurangi risiko salah ketik atau celah keamanan.
- Mengapa wajib ada csrf_token? Tag ini berguna untuk mencegah serangan keamanan yang bernama Cross-Site Request Forgery (CSRF). Serangan ini terjadi saat ada situs luar atau pihak jahat yang mencoba mengirimkan data formulir palsu atas nama kita yang sedang login. Dengan menyertakan csrf_token, Django akan memberikan token rahasia di dalam form untuk memastikan bahwa data yang dikirim memang benar-benar berasal dari halaman website kita sendiri, bukan dari website lain.

2. Mengapa JSON lebih disukai dibandingkan XML pada aplikasi web modern:
   - Ukuran data lebih ringkas
   - Sangat cocok dengan JavaScript
   - Lebih mudah dibaca

3. Alur view mengembalikan JSON dan alasan perlunya serialization:
     a. Browser atau pengguna membuka URL endpoint data (misalnya /api/projects).
     b. Django memeriksa berkas urls.py lalu memanggil fungsi view yang sesuai (misalnya get_projects_json).
     c. Di dalam view, Django mengambil data dari database lewat model menggunakan perintah seperti Projects.objects.all().
     d. Kumpulan data dari database tersebut kemudian diubah menjadi teks berformat JSON lewat proses serializers.serialize().
     e. View mengembalikan teks JSON tersebut ke browser menggunakan HttpResponse dengan format application/json.

   - Perlu serialization karena data yang diambil langsung dari database Django berbentuk objek Python yang ada di memori program. Objek Python ini tidak bisa langsung dikirim begitu saja lewat internet dan tidak bisa dipahami oleh browser atau aplikasi lain. Serialization dibutuhkan untuk menerjemahkan objek Python tersebut menjadi format teks standar (seperti JSON) supaya bisa dikirim lewat jaringan dan dibaca dengan mudah oleh browser, JavaScript, atau aplikasi HP.