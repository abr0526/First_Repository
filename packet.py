from scapy.all import scapy, sniff, Ether

print("Importing from Scapy")

val = input("how many packets")

print(f"You selected {val}")

packets = sniff (filter="not ip6", count=int(val))

for i in packets: 
	print(i.summary())


