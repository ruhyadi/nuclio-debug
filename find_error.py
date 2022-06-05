
from glob import glob
import os
import argparse

def find_error(directory: str):
    ERROR = []
    files = glob(os.path.join(directory, '*.log'))

    for file in files:
        with open(file, 'rb') as f:
            log = str(f.read())
            f.close()
        error = log.find('(E)')
        if error != -1:
            ERROR.append('error')
    
    if 'error' in ERROR:
        print('error')
        return 'error'
    else:
        print('success')
        return 'success'

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='Error Finder')
    parser.add_argument('--dir', type=str, help='Directory of logs')

    args = parser.parse_args()

    find_error(directory=args.dir)