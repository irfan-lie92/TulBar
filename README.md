# Tulbar

## Deskripsi
Tulbar adalah aplikasi yang dirancang untuk membantu individu dengan gangguan penglihatan, terutama tunanetra, dalam mengidentifikasi gambar melalui kombinasi pola getaran dan analisis suara ketukan. Aplikasi ini mengartikan suara ketukan dan menerjemahkannya menjadi pola getaran, memberikan cara taktil bagi pengguna untuk memahami konten gambar. Selain itu, gambar yang diartikan dapat dibagikan dengan orang lain untuk meningkatkan komunikasi.

## Instalasi

**Instal Dependensi:**
   - Instal semua dependensi yang diperlukan dengan menjalankan perintah berikut:
     ```bash
     pip install -r requirements.txt
     ```

## Penggunaan
1. **Persiapkan Gambar dan Suara Ketukan:**
   - Letakkan file gambar yang ingin Anda uji di direktori proyek.
   - Gantilah `<path_to_your_image.jpg>` dan `<path_to_your_sound.wav>` dalam kode dengan path sebenarnya ke file gambar dan suara ketukan Anda.

2. **Jalankan Aplikasi:**
   - Jalankan skrip utama dengan perintah berikut:
     ```bash
     python TulBar.py
     ```

3. **Interpretasi Suara Ketukan:**
   - Aplikasi akan mendeteksi suara ketukan dan menghasilkan pola getaran yang sesuai.
   - Jika suara ketukan diidentifikasi, gambar akan diartikan, dan hasilnya akan ditampilkan.

4. **Interpretasi Gambar:**
   - Pahami hasil interpretasi dengan merasakan pola getaran yang dihasilkan.
   - Gambar yang diartikan juga dapat diubah menjadi representasi visual dan dibagikan dengan orang lain.

**Catatan:**
- Pastikan untuk menggantikan placeholder seperti `<your_username>`, `<path_to_your_image.jpg>`, dan `<path_to_your_sound.wav>` dengan nilai yang sesuai.
- Sesuaikan ambang batas deteksi suara ketukan dan parameter lainnya sesuai kebutuhan proyek Anda.

### Menangani Masalah dengan ffmpeg dan ffprobe

Jika Anda mengalami peringatan atau kesalahan terkait dengan ffmpeg dan ffprobe selama eksekusi skrip, ikuti langkah-langkah ini:

1. **Instal ffmpeg:**
   - Unduh dan instal ffmpeg dari situs web resmi: [ffmpeg download page](https://ffmpeg.org/download.html).
   - Pastikan ffmpeg ditambahkan ke PATH sistem Anda.

2. **Atur PATH Sistem:**
   - Tambahkan path ke direktori di mana ffmpeg diinstal ke variabel PATH sistem Anda. Pada Windows, Anda dapat melakukannya melalui Pengaturan Sistem atau menggunakan Command Prompt:
     ```bash
     set PATH=%PATH%;C:\path\to\ffmpeg\bin
     ```
     Gantilah `C:\path\to\ffmpeg\bin` dengan path sebenarnya ke direktori bin instalasi ffmpeg Anda.

3. **Instal ffprobe:**
   - Pydub juga memerlukan ffprobe. Anda dapat mendapatkannya dari paket ffmpeg atau mengunduh ffprobe secara terpisah. Pastikan ffprobe juga dapat diakses dari PATH sistem.

4. **Restart Terminal atau Command Prompt:**
   - Setelah melakukan perubahan pada PATH, restart terminal atau command prompt Anda.

Sekarang, coba jalankan skrip Tulbar lagi.

### Masalah Umum

- **RuntimeWarning: Couldn't find ffmpeg or avconv:**
  Jika Anda melihat peringatan ini, pastikan ffmpeg diinstal dan ditambahkan ke PATH. Ikuti langkah-langkah di atas untuk memperbaiki.

- **FileNotFoundError: [WinError 2] The system cannot find the file specified:**
  Kesalahan ini menunjukkan bahwa skrip tidak dapat menemukan file ffmpeg atau ffprobe yang diperlukan. Pastikan bahwa mereka diinstal dengan benar dan dapat diakses dari PATH sistem.
