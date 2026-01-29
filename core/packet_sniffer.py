from scapy.all import sniff, IP

def handle_packet(packet):
    if IP in packet:
        print(packet[IP].src, "->", packet[IP].dst)

sniff(prn=handle_packet, store=False)
