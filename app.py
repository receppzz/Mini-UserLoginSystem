import os
import hashlib
import getpass

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    users = {}
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as f:
            for line in f:
                username, password_hash = line.strip().split(":")
                users[username] = password_hash
    return users

def save_user(username, password):
    password_hash = hash_password(password)
    with open("users.txt", "a") as f:
        f.write(f"{username}:{password_hash}\n")

def main():
    while True:
        print("\n--- Mini Kullanıcı Sistemi (Güvenli) ---")
        print("1. Kayıt Ol")
        print("2. Giriş Yap")
        print("3. Çıkış")
        choice = input("Seçim yap (1/2/3): ")

        users = load_users()

        if choice == "1":
            username = input("Kullanıcı adı: ")
            if username in users:
                print("⚠ Bu kullanıcı zaten var!")
            else:
                password = getpass.getpass("Şifre: ")
                save_user(username, password)
                print("✅ Kayıt başarılı!")

        elif choice == "2":
            username = input("Kullanıcı adı: ")
            password = getpass.getpass("Şifre: ")
            password_hash = hash_password(password)
            if username in users and users[username] == password_hash:
                print(f"🎉 Hoşgeldin {username}!")
            else:
                print("❌ Hatalı kullanıcı adı veya şifre.")

        elif choice == "3":
            print("👋 Çıkış yapılıyor...")
            break

        else:
            print("⚠ Geçersiz seçim!")

if __name__ == "__main__":
    main()
