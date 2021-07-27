# TEST VARIABLES
d = 1
u = 1

def ISP_notify(d, u):
    if (d):
        print('Download Down, Contact ISP!')
        # telegram message

    if (u):
        print('Upload Down, Contact ISP!')
        # telegram message

if __name__ == '__main__':
    ISP_notify(d, u)