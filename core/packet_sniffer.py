from scapy.all import sniff, IP
from core.detector import handle_packet

def process(packet):
    if IP in packet:
        data = {
            "src": packet[IP].src,
            "dst": packet[IP].dst,
            "proto": packet.proto,
            "size": len(packet)
        }
        handle_packet(data)

def start():
    sniff(prn=process, store=False)

if __name__ == "__main__":
    start()

