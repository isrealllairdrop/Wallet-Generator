<div align="center">
  <pre>
 GGGGG EEEEE N   N EEEEE RRRR   AAA  TTTTT EEEEE      W   W  AAA  L     L     EEEEE TTTTT 
G      E     NN  N E     R   R A   A   T   E          W   W A   A L     L     E       T   
G  GG  EEE   N N N EEE   RRRR  AAAAA   T   EEE        W W W AAAAA L     L     EEE     T   
G   G  E     N  NN E     R R   A   A   T   E          WW WW A   A L     L     E       T   
 GGGGG EEEEE N   N EEEEE R  RR A   A   T   EEEEE      W   W A   A LLLLL LLLLL EEEEE   T   
  </pre>
  <h1>Wallet Generator</h1>
  <h3>by ISREALLL AIRDROP</h3>
</div>

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Stabil-brightgreen?style=for-the-badge)

Selamat datang di **Wallet Generator**, sebuah skrip *powerful* yang dirancang untuk kebutuhan pembuatan wallet kripto secara massal maupun tunggal dengan cepat, aman, dan bisa dijalankan secara offline.

> **Hubungi kami di Telegram:** [https://t.me/Isrealll1](https://t.me/Isrealll1)
>> **Hubungi kami di Web:** [https://isrealllairdrop.tech/](https://isrealllairdrop.tech/)

---

## 🔥 Fitur Unggulan

* **✅ Multi-Jaringan:** Mendukung pembuatan wallet untuk **EVM Chains** (Ethereum, BSC, Polygon, Avax, dll.) dan **Solana**.
* **✨ Fleksibel:** Bisa membuat wallet dari **mnemonic baru** atau mengimpor dari **daftar mnemonic yang sudah ada**.
* **🚀 Pembuatan Massal (Bulk):** Mampu membuat ribuan wallet baru hanya dengan satu perintah.
* **🌐 Opsi "Semua Jaringan":** Buat wallet EVM dan Solana sekaligus dari satu mnemonic untuk efisiensi maksimal.
* **📄 Format Output Profesional:** Hasil disimpan dalam format `.txt` yang mudah dibaca dan `.json` yang terstruktur dengan urutan kunci yang rapi.
* **🎨 Tampilan Menarik:** Antarmuka terminal yang dilengkapi warna untuk membedakan instruksi, pesan sukses, dan peringatan.
* **🔒 Bisa 100% Offline & Aman:** Dirancang untuk dijalankan di lingkungan *air-gapped* (tanpa koneksi internet) untuk keamanan kunci privat Anda.

---

> ## ☢️ PERINGATAN KEAMANAN KRUSIAL ☢️
>
> * **JALANKAN OFFLINE:** Skrip ini **BISA** dijalankan di komputer yang sepenuhnya terisolasi dari koneksi internet untuk mencegah pencurian kunci.(INSTALL MODULNYA DULU).
> * **ANDA BERTANGGUNG JAWAB:** Keamanan *mnemonic phrase* dan *private key* yang Anda buat adalah tanggung jawab Anda sepenuhnya. Simpan di tempat yang sangat aman.
> * **BUKAN UNTUK ASET BESAR:** Alat ini ditujukan untuk pembuatan wallet dalam jumlah besar untuk kebutuhan airdrop, testing, atau aktivitas serupa. Untuk menyimpan aset dalam jumlah signifikan, sangat disarankan menggunakan **Hardware Wallet** (seperti Ledger atau Trezor).
> * **GUNAKAN DENGAN RISIKO ANDA SENDIRI.**

---

## 🛠️ Instalasi

Pastikan Anda memiliki Python versi 3.10 atau yang lebih baru.

1.  **Clone Repositori (atau Unduh File)**
    Jika Anda menggunakan git:
    ```bash
    git clone https://github.com/isrealllairdrop/Wallet-Generator.git
    cd Wallet-Generator
    ```
    Atau cukup unduh file skripnya.

2.  **Install Library yang Dibutuhkan**
    Buka terminal di folder proyek dan jalankan perintah ini. Menggunakan path Python absolut sangat disarankan untuk menghindari masalah lingkungan.
    ```bash
    python3 -m pip install bip-utils mnemonic
    ```

---

## 🚀 Cara Penggunaan

Jalankan skrip menggunakan terminal. Anda akan dipandu oleh menu interaktif yang berwarna dan mudah diikuti.

```bash
python3 bot.py
```

---

##  Mode Operasi

### 🧠 Gunakan Mnemonic yang Sudah Ada
1. Buat file bernama `mnemonic.txt` di direktori yang sama dengan skrip.
2. Masukkan daftar mnemonic Anda, **satu baris per mnemonic**.
3. Jalankan skrip dan pilih **Opsi [1]**.

### ✨ Buat Mnemonic Baru
1. Jalankan skrip dan pilih **Opsi [2]**.
2. Masukkan jumlah wallet yang ingin Anda buat.

---

## 🌐 Pilihan Jaringan
Pilih jaringan saat menjalankan skrip:

- `[1] EVM` – Membuat wallet Ethereum Virtual Machine.
- `[2] SOLANA` – Membuat wallet Solana.
- `[3] SEMUA JARINGAN` – Membuat wallet untuk **EVM dan Solana** dari setiap mnemonic.

---

## 🗂️ Struktur Folder Output

Skript secara otomatis membuat struktur folder sebagai berikut:

### 🔹 Jika Menggunakan Mnemonic Lama
```shell
Glama/
└── EVM/
    ├── address.txt
    ├── privatekey.txt
    ├── mnemonic.txt
    └── wallet.json
```
### 🔹 Jika Membuat Mnemonic Baru
```shell
Gbaru/
└── EVM/ atau SOLANA/ atau ALL/
    ├── address.txt
    ├── privatekey.txt
    ├── mnemonic.txt
    └── wallet.json
```

---

## 🧾 Contoh Struktur File JSON

### 🔸 Output wallet.json (Single Chain):
```json
{
  "wallet 1": {
    "mnemonic": "first mnemonic phrase...",
    "address": "0x...",
    "private_key": "0x..."
  }
}
```
🔸 Output wallet.json (Multi-Chain):
```json
{
  "wallet 1": {
    "mnemonic": "the mnemonic phrase...",
    "wallets": {
      "EVM": {
        "address": "0x...",
        "private_key": "0x..."
      },
      "SOLANA": {
        "address": "SoL...",
        "private_key": "sol_pk..."
      }
    }
  }
}
```
