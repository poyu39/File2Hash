import hashlib
import os

def CalcSha1(file_name):
    with open(file_name,'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        if bytes_mode == 40:
            hash = sha1obj.hexdigest()
        else:
            hash = sha1obj.digest()
        print('sha1: ' + hash)
        print('len: ' + str(len(hash)))
    return hash

if __name__ == "__main__":
    file_name = str(input('input_file_name = '))
    bytes_mode = int(input('(20/40)bytes = '))
    CalcSha1(file_name)

os.system("pause")