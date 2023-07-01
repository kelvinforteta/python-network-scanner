#!/usr/bin/env python

# for scanning IP addresses
import scapy.all as scapy
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target",
                        help="Target IP address to be scanned")
    options = parser.parse_args()
    # Check for empty fields
    if not options.target:
        parser.error(
            "[-] Please specify a target IP address to scan, use --help for more info")
    else:
        return options


def scan(ip_address):
    arp_request = scapy.ARP(pdst=ip_address)
    # arp_request.show()
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    # print(arp_request_broadcast.summary())
    # arp_request_broadcast.show()
    # scapy.ls(scapy.ARP()) this list all the field we can set
    answered_list = scapy.srp(arp_request_broadcast,
                              timeout=1, verbose=False)[0]
    clients_list = []
    for element in answered_list:
        clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(clients_dict)

    return clients_list


def print_result(result_list):
    print("IP\t\t\tMAC Address\n-------------------------------------------------------")

    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])


option = get_arguments()
result = scan(option.target)
print_result(result)
