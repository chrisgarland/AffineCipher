# .../Ass1/AffineCipher/affine_cipher.py
import sys

shift = 27

def main(in_file, mode):
    if mode is 'e':
        encrypt(in_file)
    elif mode is 'd':
        decrypt(in_file)


def encrypt(in_file):
    file_contents = in_file.readlines()
    f.seek(0)
    for line in file_contents:
        for c in line:
            if c.isalpha():
                ch = chr(ord(c)+(shift%26))
            else:
                ch =  c
            in_file.write(ch)


def decrypt(in_file):
    file_contents = in_file.readlines()
    f.seek(0)
    for line in file_contents:
        for c in line:
            if c.isalpha():
                ch = chr(ord(c)-(shift%26))
            else:
                ch =  c
            in_file.write(ch)


def corr_num_args(argv):
    return len(argv) is 3

if __name__ == '__main__':
    if corr_num_args(sys.argv):
        f = open(sys.argv[1], 'r+')
        main(f, sys.argv[2])
        f.close()
    else:
        print 'Wrong number of args, must enter existing filename followed by \'e\' or \'d\''
        sys.exit(1)

