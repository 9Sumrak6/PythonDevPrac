from http.server import test
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
test(bind=s.getsockname()[0], port=1234)
print(s.getsockname()[0])
s.close()
