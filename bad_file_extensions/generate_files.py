import hashlib

def main():
    with open('filetypes.txt', 'r') as f:
        for ext in f.readlines():
            ext = ext.strip()

            hash = hashlib.md5(ext.encode()).hexdigest()

            with open(f'files/{hash}.{ext}', 'w') as f2:
                f2.write(hash)
                f2.close()

if __name__ == '__main__':
    raise SystemExit(main())