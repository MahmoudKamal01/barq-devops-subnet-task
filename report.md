# Network Analysis Questions & Answers

## 1. Which subnet has the most hosts?

The largest subnets (by host capacity) are all `/22` networks, each supporting **1022 usable hosts**:

- 192.168.100.0/22
- 10.2.0.0/22
- 192.168.20.0/22
- 172.16.48.0/22
- 10.20.4.0/22
- 10.3.0.0/22
- 172.16.60.0/22
- 10.15.4.0/22

## 2. Are there any overlapping subnets?

**No overlapping subnets** exist in this network.

All subnets have:

- Unique network addresses
- Non-overlapping address ranges

## 3. What is the smallest and largest subnet in terms of address space?

| Size     | Subnet         | Host Capacity |
| -------- | -------------- | ------------- |
| Smallest | 192.168.1.0/24 | 254 hosts     |
| Largest  | 10.2.0.0/22    | 1022 hosts    |

## 4. Suggested Subnetting Strategy to Reduce Wasted IPs

### Option 1: Hierarchical Subnetting

Split `10.0.0.0/16` into:

- `/22` for large groups (1022 hosts)
- `/24` for medium teams (254 hosts)
- `/26` for small devices (62 hosts)

### Option 2: Variable Length Subnet Masking (VLSM)

Divide `/23` space flexibly:

- 1x `/24` (254 hosts)
- 2x `/25` (126 hosts each)

This approach minimizes IP waste by matching subnet sizes to actual needs.
