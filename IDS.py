import pcapy
import socket
import struct

class NetworkMonitor:
    def __init__(self, interface, callback):
        self.interface = interface
        self.callback = callback

    def start_capture(self):
        try:
            # Open network interface for capturing packets
            cap = pcapy.open_live(self.interface, 65536, True, 100)

            # Set callback function to process each captured packet
            cap.loop(-1, self.process_packet)
        except pcapy.PcapError as e:
            print(f"Error opening interface {self.interface}: {e}")

    def process_packet(self, header, data):
        try:
            # Parse Ethernet frame
            eth_header = data[:14]
            eth_header_unpack = struct.unpack('!6s6sH', eth_header)
            eth_protocol = socket.ntohs(eth_header_unpack[2])

            # Parse IP header
            if eth_protocol == 8:  # IPv4
                ip_header = data[14:34]
                ip_header_unpack = struct.unpack('!BBHHHBBH4s4s', ip_header)
                src_ip = socket.inet_ntoa(ip_header_unpack[8])
                dest_ip = socket.inet_ntoa(ip_header_unpack[9])

                # Call callback function with packet information
                self.callback(src_ip, dest_ip)
        except Exception as e:
            print(f"Error processing packet: {e}")

# Example usage
def packet_callback(src_ip, dest_ip):
    print(f"Received packet from {src_ip} to {dest_ip}")

# Start network monitoring on the specified interface
monitor = NetworkMonitor("eth0", packet_callback)
monitor.start_capture()
