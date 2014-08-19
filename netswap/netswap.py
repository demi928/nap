#coding:utf-8
import os,sys,re,time
from configobj import ConfigObj
from validate import Validator

def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path): 
        return path 
    elif os.path.isfile(path): 
        return os.path.dirname(path) 

def swap_net(gateway):
    global isSwap
    if isSwap == "True" :
        return isSwap

    swap_route(gateway)
    set_isSwap("True")

    return "swap_net"

def restore_net(gateway):
    global isSwap
    if isSwap == "False" :
        return isSwap
    
    swap_route(gateway)
    set_isSwap("False")
    
    return "restore_net"

def set_isSwap(status):
    global swap_status,isSwap
    swap_status["swap"] = status
    swap_status.write()
    isSwap = status
    
def swap_route(gateway):
#    online todo: demi
    os.popen("/bin/stadmin -t %s"%gateway)
    os.popen("/sbin/route del default")
    os.popen("/sbin/route add default gw %s"%gateway)
    
def test_ping(ip):
    Pingnum=10
    Timeout=15
    cmd="/bin/ping %s -c %s -w %s"%(ip,Pingnum,Timeout)    
    tmp = os.popen(cmd).read() 
    lost_rate_match = re.compile('(\d+)\spackets transmitted, (\d+)\sreceived,\s(\d+(.\d+)?)')
    lost_rate = lost_rate_match.findall(tmp)
    if ( not lost_rate or int(lost_rate[0][2]) >= 100 ):
        return False
    return True

####################### main process start ##############
pythonPath = cur_file_dir()
configFile = pythonPath+"/netswap.conf"
configSpec = pythonPath+"/netswap.confspec"
swapFile = pythonPath+"/is_swap.status"

if not os.path.isfile(swapFile):
    os.popen("/bin/echo swap = False > "+swapFile)

swap_status = ConfigObj(swapFile,encoding='UTF8')
isSwap = swap_status["swap"]

if not os.path.isfile(configFile):
    print "file "+configFile+" not exist."
    sys.exit()

config = ConfigObj(configFile,configspec=configSpec,encoding='UTF8')
val = Validator()
test = config.validate(val)
if not test == True:
    print "Configuration file parameters errors"
    exit()
    
section = config["main"]

while True:
    result = test_ping(section["ip1"])
    if result :
        restore_net(section["gateway1"])
    else:
        swap_net(section["gateway2"])
    time.sleep(3)
    
    
