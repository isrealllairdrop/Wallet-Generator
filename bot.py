# ==============================================================================
# Import Library
# ==============================================================================
import os
import json
import time
from typing import Dict, List, Optional, Any
from mnemonic import Mnemonic

try:
    from bip_utils import (
        Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes
    )
except ImportError:
    print("Error: Library 'bip-utils' tidak ditemukan. Silakan install dengan 'pip install bip-utils'")
    exit()

# ==============================================================================
# Konstanta & Konfigurasi
# ==============================================================================
# File & Folder
INPUT_FILE_NAME = "mnemonic.txt"
NEW_GEN_FOLDER = "Gbaru"
EXISTING_GEN_FOLDER = "Glama"
ALL_NETWORKS_FOLDER = "ALL"
COMPREHENSIVE_OUTPUT_FILE = "wallets_lengkap.txt"

# Jaringan yang didukung
SUPPORTED_NETWORKS = {
    "1": "EVM",
    "2": "SOLANA",
}
ALL_NETWORKS_CHOICE = "3"
ALL_NETWORKS_KEY = "ALL"
ALL_NETWORKS_LIST = list(SUPPORTED_NETWORKS.values())

# Warna untuk Terminal
class Colors:
    """ANSI color codes for professional terminal output."""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# ==============================================================================
# Fungsi Inti
# ==============================================================================

def display_banner() -> None:
    """Menampilkan banner utama dan peringatan keamanan."""
    banner = f"""{Colors.OKCYAN}
 GGGGG EEEEE N   N EEEEE RRRR   AAA  TTTTT EEEEE      W   W  AAA  L     L     EEEEE TTTTT 
G      E     NN  N E     R   R A   A   T   E          W   W A   A L     L     E       T   
G  GG  EEE   N N N EEE   RRRR  AAAAA   T   EEE        W W W AAAAA L     L     EEE     T   
G   G  E     N  NN E     R R   A   A   T   E          WW WW A   A L     L     E       T   
 GGGGG EEEEE N   N EEEEE R  RR A   A   T   EEEEE      W   W A   A LLLLL LLLLL EEEEE   T   
    {Colors.ENDC}"""
    print(banner)
    print("="*100)
    print(f"{Colors.BOLD}{'by ISREALLL AIRDROP'.center(100)}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}{'https://t.me/Isrealll1'.center(100)}{Colors.ENDC}")
    print("="*100)
    print(f"\n{Colors.WARNING}{'#' * 85}")
    print("###                             PERINGATAN KEAMANAN:                             ###")
    print("###   1. Bisa dijalankan secara offline jika sudah menginstal semua modulnya      ###")
    print("###   2. JANGAN PERNAH membagikan Private Key atau Mnemonic Phrase Anda.          ###")
    print("###   3. Anda bertanggung jawab penuh atas keamanan wallet yang Anda buat.        ###")
    print(f"{'#' * 85}{Colors.ENDC}\n")
    time.sleep(2)

def generate_single_wallet(mnemonic_phrase: str, network_name: str) -> Optional[Dict[str, str]]:
    """
    Menghasilkan satu wallet untuk satu jaringan spesifik dari satu mnemonic.
    """
    try:
        coin_map = {
            "EVM": Bip44Coins.ETHEREUM,
            "SOLANA": Bip44Coins.SOLANA,
        }
        if network_name not in coin_map:
            return None

        coin_type = coin_map[network_name]
        seed_bytes = Bip39SeedGenerator(mnemonic_phrase).Generate()
        bip44_mst_ctx = Bip44.FromSeed(seed_bytes, coin_type)
        bip44_addr_ctx = bip44_mst_ctx.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT).AddressIndex(0)
        
        return {
            "address": bip44_addr_ctx.PublicKey().ToAddress(),
            "private_key": bip44_addr_ctx.PrivateKey().Raw().ToHex()
        }
    except Exception:
        return None

def process_mnemonic(phrase: str, network_name: str) -> Dict[str, Any]:
    """
    Memproses satu mnemonic untuk menghasilkan data wallet sesuai pilihan jaringan.
    """
    if network_name == ALL_NETWORKS_KEY:
        combined_data = {"mnemonic": phrase, "wallets": {}}
        for net in ALL_NETWORKS_LIST:
            wallet_info = generate_single_wallet(phrase, net)
            if wallet_info:
                combined_data["wallets"][net] = wallet_info
        return combined_data
    else:
        wallet_info = generate_single_wallet(phrase, network_name)
        if wallet_info:
            return {
                "mnemonic": phrase,
                "address": wallet_info['address'],
                "private_key": wallet_info['private_key']
            }
    return {}

def save_wallets(wallets_data: Dict[str, Any], base_folder: str, network_name: str) -> None:
    """
    Menyimpan data wallet ke dalam file-file output.
    """
    output_folder_name = ALL_NETWORKS_FOLDER if network_name == ALL_NETWORKS_KEY else network_name
    output_path = os.path.join(base_folder, output_folder_name)

    try:
        os.makedirs(output_path, exist_ok=True)
    except OSError as e:
        print(f"{Colors.FAIL}Error: Gagal membuat direktori {output_path}. Error: {e}{Colors.ENDC}")
        return

    try:
        if network_name == ALL_NETWORKS_KEY:
            with open(os.path.join(output_path, COMPREHENSIVE_OUTPUT_FILE), 'w') as f:
                for wallet_name, data in wallets_data.items():
                    f.write(f"--- {wallet_name.capitalize()} ---\n")
                    f.write(f"Mnemonic: {data['mnemonic']}\n")
                    for net, wallet_info in data['wallets'].items():
                        f.write(f"  {net} Address: {wallet_info['address']}\n")
                        f.write(f"  {net} Private Key: {wallet_info['private_key']}\n")
                    f.write("\n")
        else:
            with open(os.path.join(output_path, "address.txt"), 'w') as f:
                f.write('\n'.join([w['address'] for w in wallets_data.values()]))
            with open(os.path.join(output_path, "privatekey.txt"), 'w') as f:
                f.write('\n'.join([w['private_key'] for w in wallets_data.values()]))
            with open(os.path.join(output_path, "mnemonic.txt"), 'w') as f:
                f.write('\n'.join([w['mnemonic'] for w in wallets_data.values()]))

        with open(os.path.join(output_path, "wallet.json"), 'w') as f:
            json.dump(wallets_data, f, indent=4)

    except IOError as e:
        print(f"{Colors.FAIL}Error: Gagal menulis file di {output_path}. Error: {e}{Colors.ENDC}")
        return
        
    print("\n" + "="*50)
    print(f"{Colors.OKGREEN}✅ PROSES SELESAI ✅{Colors.ENDC}")
    print(f"Berhasil memproses {Colors.BOLD}{len(wallets_data)}{Colors.ENDC} mnemonic.")
    print(f"Hasil disimpan di folder: {Colors.UNDERLINE}{os.path.abspath(output_path)}{Colors.ENDC}")
    print("="*50)

def main() -> None:
    """Fungsi utama untuk menjalankan alur skrip."""
    display_banner()
    
    print(f"{Colors.HEADER}{Colors.BOLD}Pilih Jaringan Wallet:{Colors.ENDC}")
    for key, value in SUPPORTED_NETWORKS.items():
        print(f"  [{key}] {value}")
    print(f"  [{ALL_NETWORKS_CHOICE}] SEMUA JARINGAN ({' & '.join(ALL_NETWORKS_LIST)})")
    
    full_network_map = {**SUPPORTED_NETWORKS, **{ALL_NETWORKS_CHOICE: ALL_NETWORKS_KEY}}
    while True:
        choice = input(f"{Colors.OKCYAN}Masukkan pilihan (1-{ALL_NETWORKS_CHOICE}): {Colors.ENDC}")
        if choice in full_network_map:
            network_name = full_network_map[choice]
            break
        else:
            print(f"{Colors.FAIL}Pilihan tidak valid, silakan coba lagi.{Colors.ENDC}")

    print(f"\n{Colors.HEADER}{Colors.BOLD}Pilih Sumber Mnemonic:{Colors.ENDC}")
    print(f"  [1] Gunakan Mnemonic yang Sudah Ada (dari file '{INPUT_FILE_NAME}')")
    print("  [2] Buat Mnemonic Baru")
    
    while True:
        source_choice = input(f"{Colors.OKCYAN}Masukkan pilihan (1-2): {Colors.ENDC}")
        if source_choice in ["1", "2"]:
            break
        else:
            print(f"{Colors.FAIL}Pilihan tidak valid, silakan coba lagi.{Colors.ENDC}")
            
    all_wallets_data: Dict[str, Any] = {}
    
    if source_choice == '1':
        base_folder = EXISTING_GEN_FOLDER
        print(f"\n{Colors.OKBLUE}Membaca mnemonic dari file '{INPUT_FILE_NAME}'...{Colors.ENDC}")
        
        if not os.path.exists(INPUT_FILE_NAME):
            print(f"{Colors.FAIL}Error: File input '{INPUT_FILE_NAME}' tidak ditemukan!{Colors.ENDC}")
            return
            
        with open(INPUT_FILE_NAME, 'r') as f:
            mnemonics = [line.strip() for line in f if line.strip()]
        
        if not mnemonics:
            print(f"{Colors.FAIL}Error: File '{INPUT_FILE_NAME}' kosong.{Colors.ENDC}")
            return

        for i, phrase in enumerate(mnemonics):
            print(f"Memproses mnemonic ke-{i+1}/{len(mnemonics)}...", end='\r')
            processed_data = process_mnemonic(phrase, network_name)
            if processed_data:
                all_wallets_data[f"wallet {i+1}"] = processed_data

    elif source_choice == '2':
        base_folder = NEW_GEN_FOLDER
        while True:
            try:
                count = int(input(f"\n{Colors.OKCYAN}Berapa banyak mnemonic baru yang ingin dibuat? {Colors.ENDC}"))
                if count > 0:
                    break
                else:
                    print(f"{Colors.FAIL}Jumlah harus lebih dari 0.{Colors.ENDC}")
            except ValueError:
                print(f"{Colors.FAIL}Input tidak valid, masukkan angka.{Colors.ENDC}")
        
        mnemo = Mnemonic("english")
        for i in range(count):
            print(f"Membuat wallet ke-{i+1}/{count}...", end='\r')
            new_phrase = mnemo.generate(strength=128)
            processed_data = process_mnemonic(new_phrase, network_name)
            if processed_data:
                all_wallets_data[f"wallet {i+1}"] = processed_data

    if all_wallets_data:
        save_wallets(all_wallets_data, base_folder, network_name)
    else:
        print(f"\n{Colors.FAIL}Tidak ada wallet yang berhasil dibuat. Proses dihentikan.{Colors.ENDC}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.FAIL}Proses dibatalkan oleh pengguna. Keluar.{Colors.ENDC}")
        exit()
