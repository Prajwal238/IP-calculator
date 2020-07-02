import ipaddress
import sys
import random
import math

def ipdetails(targetIP):
    try:
        ip_adrs = ipaddress.IPv4Network(targetIP, strict=False)
        first_octet = int(str(ip_adrs).split('.')[0])
        ipclass = ""

        if first_octet == 0:
            ipclass = "It is source IP address."
        if first_octet >= 1 and first_octet < 127:
            ipclass =" Class - A"
        if first_octet >= 128 and first_octet < 192:
            ipclass = "Class - B"
        if first_octet >= 192 and first_octet < 224:
            ipclass = "Class - C"
        if first_octet >= 224 and first_octet < 240:
            ipclass = "Class - D"
        if first_octet >= 240 and first_octet < 255:
            ipclass = "Class - E"
        if first_octet == 127:
            ipclass = "IP address are reserved for local host."
    except ipaddress.AddressValueError:
        ipclass = "This is not a valid IP address."
    except ipaddress.NetmaskValueError:
        ipclass = "This is not a valid subnet mask."
    if ip_adrs.is_private:
        ipclass = "Private IP address range"

    hosts = []
    for host in ip_adrs.hosts():
        hosts.append(host)

    cidr = int(str(ip_adrs).split('/')[1])

    hps = (math.pow(2, 32-cidr) - 2)

    net_and_sub = (ip_adrs.with_netmask)
    network_id =  str(net_and_sub.split('/')[0])
    subnet_id = str(net_and_sub.split('/')[1])

    print("--------------------\n COMPLETE DETAILS \n -------------------")
    print("IP address belongs to {}".format(ipclass))
    print(f"Network ID : {network_id}")
    print(f"Subnet Mask: {subnet_id}")
    print("Available IP addresses: {}".format(ip_adrs.num_addresses - 2))
    print("Broadcast address: {}".format(ip_adrs.broadcast_address))
    print(f"Host Range: {hosts[0]} - {hosts[len(hosts) - 1]}")
    print(f"Total no.of subnets: {int(hps)}")

    response = str(input("Do you want to generate a random IP address that is available for the respective network ID? (y/n)"))
    if response == 'y':
        random_ip = random.choice(hosts)
        print(f"Available IP: {str(random_ip)} ")

    elif response == 'n':
        print("Thank you for using, See you with another IP")

    else:
        print("invalid choice")


def main():
    targetIP = str(input(" \n Example: 192.168.1.45/24 \n Enter the IP along with CIDR: "))
    ipdetails(targetIP)

if __name__ == "__main__":
    main()    