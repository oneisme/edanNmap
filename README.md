# edanNmap

# EdanNmap
Bagaimana cara kerja edanNmap?
Saya menemukan kerentanan XSPA di API pengembang Facebook dan saya melaporkannya ke tim keamanan mereka. Tetapi untuk beberapa alasan, mereka mengatakan itu fitur dan bukan kerentanan. Jadi saya membuat edanNmap untuk melakukan scan port anonim dengan menggunakan kerentanan ini. Saya berencana untuk menambahkan fungsi pendeteksian host langsung di masa depan.

Apa itu kerentanan XSPA?
Aplikasi rentan terhadap Cross Site Port Attacks jika aplikasi memproses URL yang diberikan pengguna dan tidak memverifikasi / membersihkan respons backend yang diterima dari server jauh sebelum mengirimnya kembali ke klien. Tanggapan, dalam kasus-kasus tertentu, dapat dipelajari untuk mengidentifikasi ketersediaan layanan (status port, spanduk, dll.) Dan bahkan mengambil data dari layanan jarak jauh dengan cara yang tidak konvensional.

Memasang dan Menggunakan edanNmap
Buka terminal dan masukkan

git clone https://github.com/oneisme/edanNmap.git

cd edanNmap
Akhirnya, jalankan skrip dengan memasukkan

python edanNmap.py
Anda dapat memasukkan alamat IP ...
# Bagaimana mencari cookies Facebook
# Buka browser Anda dan arahkan ke alat pengembang -> Jaringan. Ini adalah fitur yang datang preinsalled di sebagian besar browser modern. Di Firefox, Anda dapat membukanya dengan menekan Ctrl + Shift + Q. Setelah membukanya, kunjungi halaman dan facebook dan Anda akan melihat semua permintaan yang dibuat oleh pengguna di panel pengembang. Klik pada setiap permintaan dan temukan dan salin nilai Cookie dari Header. Catatan: Jika anoNmap menunjukkan semua port sebagai tertutup, maka pertimbangkan untuk meningkatkan nilai batas waktu.
Kaliyan bisa cari cookies di google
