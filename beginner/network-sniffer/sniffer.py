from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_handler(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"[+] {ip_layer.src} -> {ip_layer.dst}", end='')

        if TCP in packet:
            print(f" [TCP] {packet[TCP].sport} -> {packet[TCP].dport}")
        elif UDP in packet:
            print(f" [UDP] {packet[UDP].sport} -> {packet[UDP].dport}")
        elif ICMP in packet:
            print(" [ICMP]")
        else:
            print(" [Other]")

sniff(prn=packet_handler, count=20)