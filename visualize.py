import json
import matplotlib.pyplot as plt
import sys

try:
    # Try to open and load the JSON file
    with open('subnet_report.json') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print("Error: The JSON file is malformed or corrupted")
            sys.exit(1)

    # Get unique subnets and host counts
    subnets = []
    hosts = []
    seen = set()

    try:
        for entry in data['ip_details']:
            cidr = entry['cidr_notation']
            if cidr not in seen:
                seen.add(cidr)
                subnets.append(cidr)
                hosts.append(entry['usable_hosts'])
    except KeyError as e:
        print(f"Error: Missing expected key in JSON data - {str(e)}")
        sys.exit(1)

    # Create and show plot
    plt.bar(subnets, hosts)
    plt.xticks(rotation=90)
    plt.title('Usable Hosts per Subnet')
    plt.xlabel('Subnet (CIDR Notation)')
    plt.ylabel('Number of Hosts')
    plt.tight_layout()
    
    try:
        plt.savefig('network_plot.png')
        print("Plot saved successfully as hosts_per_subnet.png")
    except Exception as e:
        print(f"Error saving plot: {str(e)}")
    
    plt.show()

except FileNotFoundError:
    print("Error: subnet_report.json file not found")
    print("Please run the analysis script first to generate the report")
    sys.exit(1)
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
    sys.exit(1)