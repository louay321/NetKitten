import time
import socket

def TCP():
    start_time = time.time()

    network = input('IP address: ')
    network_seg = network.split('.')
    network_affix = network_seg[0] + '.' + network_seg[1] + '.' + network_seg[2] + '.'
    starting = int(input("Starting number of IP : "))
    ending = int(input("Ending number of IP : "))


    def scanner(address):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((address, 445))
        if result == 0:
            return 1
        else :
            return 0

    def run_TCP():
        result = []
        for ip in range(starting, ending):
            address = network_affix + str(ip)
            if(scanner(address)):
                print(address, 'is live')
                result.append(address)
        return result
    print('this my take a while, be patient...')
    result = run_TCP()
    if result == []:
        print('no addresses found live.')
    else:
        print('TCP scan finished successfully!')
    return result



