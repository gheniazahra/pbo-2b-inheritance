from src.game import Game
from src.helper.hash_generator.hash_manager import HashManager
from src.helper.hash_generator.md5_hash import MD5Hash
from src.helper.hash_generator.sha256_hash import SHA256Hash

if __name__ == "__main__":
    # --- 1. Bagian Testing Hash (Ditambahkan) ---
    print("=== Uji Coba Hash Generator ===")
    manager = HashManager()
    teks = "Password123"
    
    manager.set_algorithm(MD5Hash())
    print(f"MD5: {manager.generate_hash(teks)}")
    
    manager.set_algorithm(SHA256Hash())
    print(f"SHA-256: {manager.generate_hash(teks)}")
    print("===============================\n")

    # --- 2. Bagian Utama Game (Kode Asli) ---
    game = Game() # membuat object game
    game.play_game()