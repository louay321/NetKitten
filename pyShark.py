import pyshark

def shark():
    packets_result = []
    capture = pyshark.LiveCapture(interface='eth0')
    capture.sniff(timeout=50)
    print(capture)
    print(capture[3])
    for packet in capture.sniff_continuously(packet_count=5):
        print ('Just arrived:', packet)
        packets_result.append(packet)
    return packets_result
