import sys
import json
import pandas as pd
import matplotlib.pyplot as plt

def get_dataframe(excel_file_name):
       try:
        return pd.read_excel(excel_file_name)
       except FileNotFoundError:
            print(f"Error: File '{excel_file_name}' not found")
            return None
       except Exception as e:
            print(f"Error loading Excel file: {str(e)}")
            return None

def get_ips_data(dataframe):
    data = []
    for index, row in dataframe.iterrows():
        data.append({
            "ip": row["IP Address"],
            "subnet_mask": row["Subnet Mask"]
        })
    return data

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

def get_net_addr(ip,subnet):
    res = []
    ip_arr = convert_dotted_to_array(ip)
    sub_arr = convert_dotted_to_array(subnet)
    for i in range(4):
        res.append(str(int(ip_arr[i]) & int(sub_arr[i])))  
    return ".".join(octet for octet in res)

def get_cidr_notation(ip, subnet):
    network_addr = get_net_addr(ip, subnet)
    return f"{network_addr}/{get_network_bits(ip, subnet)}"


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

def generate_json_report(df):
    input_arr = get_ips_data(df)
    processed_ips = []
    for _, row in df.iterrows():
        ip = row["IP Address"]
        subnet = row["Subnet Mask"]
                
        processed_ips.append({
            "ip": ip,
            "subnet_mask": subnet,
            "cidr_notation": get_cidr_notation(ip, subnet),
            "network_address": get_net_addr(ip, subnet),
            "broadcast_address": get_broadcast_addr(ip, subnet),
            "usable_hosts": get_number_of_usable_hosts(ip, subnet)
        })

    grouped_ips = group_ips(input_arr)

    report = {
        "ip_details": processed_ips,
        "subnet_groups": grouped_ips
    }

    with open("subnet_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("Report generated as subnet_report.json")


if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Error: Please provide the Excel filename as an argument")
        print("Usage: python subnet_analyzer.py <filename.xlsx>")
        sys.exit(1)
    
    excel_file = sys.argv[1]
    
    df = get_dataframe(excel_file)
    if df is not None:  # 
        generate_json_report(df)
