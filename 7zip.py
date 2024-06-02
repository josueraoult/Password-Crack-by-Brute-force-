import py7zr

def brute_force_7z(file_7z, wordlist):
    with open(wordlist, 'r') as file:
        passwords = file.readlines()
    
    for password in passwords:
        password = password.strip('\n')
        try:
            with py7zr.SevenZipFile(file_7z, mode='r', password=password) as archive:
                archive.extractall()
            print(f'[+] Password found: {password}')
            return
        except py7zr.exceptions.Bad7zFile:
            continue
        except py7zr.exceptions.PasswordRequired:
            continue
    print('[-] Password not found.')

if __name__ == '__main__':
    file_7z = 'your_file.7z'
    wordlist = 'wordlist.txt'
    brute_force_7z(file_7z, wordlist)
