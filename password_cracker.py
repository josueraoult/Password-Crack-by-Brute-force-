import zipfile
import py7zr
import os
from colorama import Fore, Style, init

# Initialiser colorama
init(autoreset=True)

def brute_force_zip(zip_file, wordlist):
    try:
        zip_file = zipfile.ZipFile(zip_file)
        with open(wordlist, 'r') as file:
            passwords = file.readlines()
        
        for password in passwords:
            password = password.strip('\n')
            try:
                zip_file.extractall(pwd=bytes(password, 'utf-8'))
                print(Fore.GREEN + f'[+] Password found: {password}')
                return password
            except (RuntimeError, zipfile.BadZipFile):
                continue
        print(Fore.RED + '[-] Password not found.')
        return None
    except Exception as e:
        print(Fore.RED + f"Error: {e}")
        return None

def brute_force_7z(file_7z, wordlist):
    try:
        with open(wordlist, 'r') as file:
            passwords = file.readlines()
        
        for password in passwords:
            password = password.strip('\n')
            try:
                with py7zr.SevenZipFile(file_7z, mode='r', password=password) as archive:
                    archive.extractall()
                print(Fore.GREEN + f'[+] Password found: {password}')
                return password
            except py7zr.exceptions.Bad7zFile:
                continue
            except py7zr.exceptions.PasswordRequired:
                continue
        print(Fore.RED + '[-] Password not found.')
        return None
    except Exception as e:
        print(Fore.RED + f"Error: {e}")
        return None

def main():
    print(Fore.CYAN + Style.BRIGHT + "=== ZIP/7z Password Cracker ===")
    
    file_path = input(Fore.YELLOW + "Enter the path to your zip or 7z file: ").strip()
    if not os.path.isfile(file_path):
        print(Fore.RED + "Invalid file path. Please try again.")
        return

    file_extension = os.path.splitext(file_path)[1].lower()
    
    wordlist_path = input(Fore.YELLOW + "Enter the path to your wordlist file: ").strip()
    if not os.path.isfile(wordlist_path):
        print(Fore.RED + "Invalid wordlist file path. Please try again.")
        return

    if file_extension == '.zip':
        password = brute_force_zip(file_path, wordlist_path)
    elif file_extension == '.7z':
        password = brute_force_7z(file_path, wordlist_path)
    else:
        print(Fore.RED + "Unsupported file type. Only zip and 7z are supported.")
        return

    if password:
        print(Fore.GREEN + f"Success! The password is: {password}")
    else:
        print(Fore.RED + "Failed to find the password.")

if __name__ == '__main__':
    main()
          
