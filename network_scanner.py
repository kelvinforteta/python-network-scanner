#!/usr/bin/env python

# for scanning IP addresses
import scapy.all as scapy


def scan(ip_address):
    arp_request = scapy.ARP(pdst=ip_address)
    # arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    # print(arp_request_broadcast.summary())
    # arp_request_broadcast.show()
    # scapy.ls(scapy.ARP()) this list all the field we can set
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    print("IP\t\t\tMAC Address\n----------------------------------------------------------------")
    for element in answered_list:
        print(element[1].psrc)
        print(element[1].hwsrc)
        print("--------------------------------------------------------------------")


scan("192.168.1.2/24")

