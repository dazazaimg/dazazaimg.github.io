import os
import time


if __name__ == '__main__':
    years = [2006,2007,2008,2009,2010,2011,2012]
    for y in years:
        for m in range(1, 13):
            path = 'img/%s/%s/\*' % (str(y), str(m))
            print('\n')
            print(path)
            print('WILL GIT PUSH...')
            time.sleep(3)
            os.system('./dazazaimgpush.sh %s' % path)
            time.sleep(10)