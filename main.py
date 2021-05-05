"""NetKitten
this is a python project for network security dedicated to the IT-security class
Created by Nahdi Louay
Neptun id : FLWN1K
"""

from openPortScanner import scanOpenPorts
import TCPscan
from wifiSniffing import ScapySniff
from pyShark import shark
import ARPspoofing
def start():
    print('\n-->> NetKitten <<--\n')
    print('s : scan host for open ports by name')
    print('t : run a TCP ping scan for live connections')
    print('n : sniff packets in network')
    print('h : sniff packets using pyShark')
    print('a : ARP poisoning')
    print('q : Exit')
    choice = input()

    if choice == 's':
        result_ports = scanOpenPorts()

    if choice == 't':
        result_tcp = TCPscan.TCP()

    if choice == 'n':
        result_sniff = ScapySniff()

    if choice == 'h':
        result_shark = shark()

    if choice =='a':
        result_arp = ARPspoofing.ARPstart()
    if choice == 'q':
        return 0

    return 1


if __name__ == '__main__':
    running = 1
    while running:
        running = start()


