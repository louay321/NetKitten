from scapy.all import *
from collections import Counter

# setting up counter for number of packets
packet_counts = Counter()

# this function will be used as sniff() parameter to return tuples of packets ip source and destination
def packet_tuples(packet):
    tuples = tuple(sorted([packet[0][1].src, packet[0][1].dst]))
    packet_counts.update([tuples])
    print('Packet #', sum(packet_counts.values()), ': ', packet[0][1].src, ' --> ', packet[0][1].dst)

def ScapySniff():
    sniff(filter='ip', prn=packet_tuples, count=10)
    # printing packets count for each src -> dst
    for ip, count in packet_counts.items():
        print('\n', ip[0], '==>', ip[1], ':', count)
