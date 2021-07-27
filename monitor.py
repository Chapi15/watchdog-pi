import re

# TEST VARIABLES
p = 10
d = 1
u = 1

def ISP_check(p, d, u):
    # ISP CAPABILITIES
    theoDown = 3
    theoUp = 3

    # CONTROL VARIABLES
    notifyDown = 0
    notifyUp = 0

#def checkISP():
    #result = open('/Users/aro/Documents/Python/EG/monitorRed/test.txt', 'r')
    #result = open('/Users/aro/Documents/Python/EG/monitorRed/speedtest.txt', 'r')
    #response = result.read()

    '''
    # EXTRACT VALUES FROM FILE
    ping = re.search('Latency:\s+(.*?)\s', response, re.MULTILINE)
    download = re.search('Download:\s+(.*?)\s', response, re.MULTILINE)
    upload = re.search('Upload:\s+(.*?)\s', response, re.MULTILINE)
    jitter = re.search('\((.*?)\s.+jitter\)\s', response, re.MULTILINE)
    #URL = re.search('\((.*?)\s.+URL\)\s', response, re.MULTILINE)

    # CONVERT TO FLOAT VALUE
    ping = float(ping.group(1))
    download = float(download.group(1))
    upload = float(upload.group(1))
    jitter = float(jitter.group(1))
    '''

    # CHECK AGAINST THEORETICAL VALUES
    #if ( (download < d) ):
    if ( (float(d) < theoDown) ):
        notifyDown = 1

    #if ( (upload < u) ):
    if ( (float(u) < theoUp) ):
        notifyUp = 1

    return notifyDown, notifyUp

if __name__ == '__main__':
    ISP_check(p, d, u)