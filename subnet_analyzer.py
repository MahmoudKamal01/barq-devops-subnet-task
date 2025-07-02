import pandas as pd

df = pd.read_excel("ip_data.xlsx") 

input_arr = [
    {"ip": row["IP Address"], "subnet_mask": row["Subnet Mask"]}
    for _, row in df.iterrows()
]

print(input_arr)


def convert_to_bin(num):
    return bin(int(num))[2:]

def convert_dotted_to_array(ip):
    return ip.split(sep=".")

def count_ones(num):
    x = str(num)
    return x.count('1')

def get_network_bits(ip,subnet):
    network_bits = 0
    subnet_arr = convert_dotted_to_array(subnet)
    for i in subnet_arr:
        if(i=="255"):
            network_bits+=8
            continue
        binary_octet = convert_to_bin(i)
        network_bits += count_ones(binary_octet)
    return network_bits
# calc cidr notation
def get_cidr_notation(ip,subnet):
    return f"{ip}/{get_network_bits(ip,subnet)}"

# get network address
def get_net_addr(ip,subnet):
    res = []
    ip_arr = convert_dotted_to_array(ip)
    sub_arr = convert_dotted_to_array(subnet)
    for i in range(4):
        res.append(str(int(ip_arr[i]) & int(sub_arr[i])))
    return ".".join(octet for octet in res)


def get_broadcast_addr(ip,subnet):
    res = []
    ip_arr = convert_dotted_to_array(ip)
    sub_arr = convert_dotted_to_array(subnet)
    inverted_subnet_mask = []
    for i in sub_arr:
        inverted_subnet_mask.append(255 - int(i))
    for i in range(4):
        res.append(str(int(ip_arr[i]) | int(inverted_subnet_mask[i])))
    return ".".join(res)


def get_number_of_usable_hosts(ip,subnet):
    return 2 ** (32-get_network_bits(ip,subnet)) -2



def group_ips(input_arr):
    networks = {}
    for row in input_arr:
        net_addr = get_cidr_notation(row["ip"], row["subnet_mask"])
        
        if net_addr not in networks:
            networks[net_addr] = [] 

        networks[net_addr].append(row["ip"])
    return networks


# print(get_number_of_usable_hosts(ip,subnet_mask)-2)
# print(get_broadcast_addr(ip,subnet_mask))
# print(get_net_addr(ip,subnet_mask))

# print(30 & 24)
