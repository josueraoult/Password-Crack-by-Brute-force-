import zipfile

def brute_force_zip(zip_file, wordlist):
    zip_file = zipfile.ZipFile(zip_file)
    with open(wordlist, 'r') as file:
        passwords = file.readlines()
    
    for password in passwords:
        password = password.strip('\n')
        try:
            zip_file.extractall(pwd=bytes(password, 'utf-8'))
            print(f'[+] Password found: {password}')
            return
        except (RuntimeError, zipfile.BadZipFile):
            continue
    print('[-] Password not found.')

if __name__ == '__main__':
    zip_file = 'your_file.zip'
    wordlist = 'wordlist.txt'
    brute_force_zip(zip_file, wordlist)
