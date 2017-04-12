import sys


def main(in_file, mode):
    if mode is 'e':
        with open(in_file, 'r+') as f:
            encrypt(f)
    elif mode is 'd':
        with open(in_file, 'r+') as f:
            decrypt(f)


def encrypt(in_file):
    pass


def decrypt(in_file):
    pass


def corr_num_args(argv):
    return len(argv) is 3

if __name__ == '__main__':
    if corr_num_args(sys.argv):
        main(sys.argv[0], sys.argv[2])
    else:
        print 'Wrong number of args, must enter existing filename followed by \'e\' or \'d\''
        sys.exit(1)

