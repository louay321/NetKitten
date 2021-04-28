import time
from socket import *

#get the time for starting the scan
start_t = time.time()

def scanOpenPorts():
    #get the IP adress of target to scan from host name using socket method gethostbyname() or give IP if known
    print('n -> scan by name')
    print('i -> scan by IP')
    choice = input()
    if choice == 'i':
        target_IP = input('IP adress of host : ')
    if choice == 'n':
        host_input = input('name of host target to scan: ')
        target_IP = gethostbyname(host_input)

    min_range = input('minimum range of ports: ')
    max_range = input('maximum range: ')
    print('scanning host of IP: ', target_IP)
    print('please be patient this might take a while...')
    result = []
    for i in range(int(min_range), int(max_range)):
        s = socket(AF_INET, SOCK_STREAM)
        connection = s.connect_ex((target_IP, i))
        if(connection == 0) :
            print('open Port at : ', i)
            result.append(i)
        s.close()
    print('finished in: ', time.time() - start_t)
    return result


