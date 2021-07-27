from speedtest import ISP_test
from monitor import ISP_check
from notify import ISP_notify

# STAGE 1 - MEASURE SPEED (OOKLA)
p, down, up = ISP_test()

# STAGE 2 - VERIFY SPEED DATA
nD, nU = ISP_check(p, down, up)

# STAGE 3 - NOTIFY USER (TELEGRAM)
ISP_notify(nD, nU)