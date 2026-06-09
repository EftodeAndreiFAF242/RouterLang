import socket
import threading
import paramiko

# Generate a host key once
HOST_KEY = paramiko.RSAKey.generate(2048)

class FakeServer(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()
    def check_channel_request(self, kind, chanid):
        if kind == "session":
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    def check_auth_password(self, username, password):
        if username == "admin" and password == "admin":
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED
    def check_channel_shell_request(self, channel):
        self.event.set()
        return True
    def check_channel_subsystem_request(self, channel, name):
        self.event.set()
        return True

def handle_client(client_sock, addr, port):
    transport = paramiko.Transport(client_sock)
    transport.add_server_key(HOST_KEY)
    server = FakeServer()
    transport.start_server(server=server)
    chan = transport.accept(20)
    if chan:
        chan.send(b"\nFake Cisco IOS on port %d\n" % port)
        chan.close()
    transport.close()

def start_fake_router(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("127.0.0.1", port))
    sock.listen(5)
    print(f"  Fake router listening on 127.0.0.1:{port}")
    while True:
        client, addr = sock.accept()
        t = threading.Thread(target=handle_client, args=(client, addr, port))
        t.daemon = True
        t.start()

if __name__ == "__main__":
    ports = {
        "R-SPINE-1": 6001, "R-SPINE-2": 6002,
        "R-LEAF-1":  6003, "R-LEAF-2":  6004,
        "R-LEAF-3":  6005, "R-LEAF-4":  6006,
        "R-EDGE-1":  6007, "R-EDGE-2":  6008,
    }
    print("\n  Starting 8 fake Cisco routers...\n")
    for name, port in ports.items():
        t = threading.Thread(target=start_fake_router, args=(port,))
        t.daemon = True
        t.start()
    print(f"\n  All 8 routers running. Press Ctrl+C to stop.\n")
    try:
        threading.Event().wait()
    except KeyboardInterrupt:
        print("\n  Stopped.")