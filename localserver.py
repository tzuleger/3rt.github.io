import http.server
import socketserver
import socket
import sys
from urllib.parse import unquote

class SimpleServer(http.server.SimpleHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        self._set_headers()
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.end_headers()

        data = self.data_string
        print(unquote(data))

DEFAULT_PORT = 8080

o_port_num = False
if len(sys.argv) > 1:
    o_port_num = '-p' in sys.argv

PORT = int(sys.argv[sys.argv.index('-p')+1]) if o_port_num else DEFAULT_PORT

print("Server running on port " + str(PORT) + ", you can connect remotely (same network) by typing \"" + socket.gethostbyname(socket.gethostname()) + ":" + str(PORT) + "\" into the URL of a browser.")

Handler = socketserver.TCPServer(("", PORT), SimpleServer);
Handler.serve_forever()
