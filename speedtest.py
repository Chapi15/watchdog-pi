import os
import re
import subprocess
import time

def ISP_test():
    response = subprocess.Popen('/usr/local/Cellar/speedtest/1.0.0/bin/speedtest --accept-license --accept-gdpr', 
        shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    
    '''
    rawSpeed = open('/Users/aro/Documents/Python/EG/monitorRed/_test_.txt', 'a+')
    rawSpeed.write(time.strftime('%d/%m/%y') + ' ' + time.strftime('%H:%M:%S'))
    rawSpeed.write('\n')
    #rawSpeed.write(time.ctime())
    rawSpeed.write(response)
    rawSpeed.close()
    '''

    # EXTRACT VALUES FROM RAW DATA
    ping = re.search('Latency:\s+(.*?)\s', response, re.MULTILINE)
    download = re.search('Download:\s+(.*?)\s', response, re.MULTILINE)
    upload = re.search('Upload:\s+(.*?)\s', response, re.MULTILINE)
    jitter = re.search('\((.*?)\s.+jitter\)\s', response, re.MULTILINE)

    try:
        ping = ping.group(1)
        download = download.group(1)
        upload = upload.group(1)
        jitter = jitter.group(1)
    except:
        print('Error in SpeedTest CLI')

    # WRITE VALUES TO A LOG FILE
    try:
        f = open('/Users/aro/Documents/Python/EG/monitorRed/speedtest.txt', 'a+')
        if os.stat('/Users/aro/Documents/Python/EG/monitorRed/speedtest.txt').st_size == 0:
                f.write('Date,Time,Ping (ms),Jitter (ms),Download (Mbps),Upload (Mbps)\r\n')
    except:
        pass

    f.write('{},{},{},{},{},{}\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), 
        ping, jitter, download, upload))
    f.close()

    return ping, download, upload

if __name__ == '__main__':
    ISP_test()