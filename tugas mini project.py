# Sistem Informasi Pengelolaan Beasiswa Kampus
print("---Sistem Informasi Pengelolaan Beasiswa Kampus---")

# Tahap 1: Data Calon Penerima Beasiswa (Nama,Status Dokumen Lengkap, Status Lolos Seleksi, Status Ipk)
print("\n1. Data Calon Penerima Beasiswa (Nama,Status Dokumen Lengkap, Status Lolos Seleksi, Status Ipk)")
data_pelamar = [
    ("ajun", "ya", "ya", "ya"),
    ("chan", "ya", "tidak", "ya"),
    ("hobie", "ya", "ya", "tidak"),
    ("rose", "tidak", "tidak", "tidak")
]

# Tahap 2: Pendaftaran dan Pengumpulan Dokumen
print("\n2. Pendaftaran dan Pengumpulan Dokumen")
for nama, dokumen_lengkap, _, _, in data_pelamar:
    if dokumen_lengkap == "ya":
        print(f"dokumen {nama} lengkap.")
    else:
        print(f"dokumen {nama} tidak lengkap. pendaftaran dibatalkan.")

# Tahap 3: seleksi Administrasi, Wawancara, dan Penilaian
print("\n3. Seleksi Administrasi, Wawancara, dan Penilaian")
penerima_beasiswa = []
for nama, dokumen_lengkap, lolos_seleksi, _, in data_pelamar:
    if dokumen_lengkap == "ya" and lolos_seleksi == "ya":
        penerima_beasiswa.append(nama)
        print(f"{nama} lolos seleksi. masuk daftar calon penerima.")
    elif dokumen_lengkap == "ya" and lolos_seleksi == "tidak":
        print(f"{nama} tidak lolos seleksi.")

# Tahap 4: Pencairan Dana dan Monitoring
print("\n4. Pencairan Dana dan Monitoring")
for nama, _, _, ipk_memenuhi_syarat in data_pelamar:
    if nama in penerima_beasiswa:
        if ipk_memenuhi_syarat == "ya":
            print(f"selamat, beasiswa {nama} dicairkan.")
        else:
            print(f"beasiswa {nama} dibatalkan karena ipk tidak memenuhi syarat.")

print("\n---Proses Pengelolaan Beasiswa Kampus Selesai")