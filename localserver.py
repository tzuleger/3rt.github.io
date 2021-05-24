import http.server
import socketserver
import socket
import sys

DEFAULT_PORT = 8080

o_port_num = False
if len(sys.argv) > 1:
    o_port_num = '-p' in sys.argv

PORT = int(sys.argv[sys.argv.index('-p')+1]) if o_port_num else DEFAULT_PORT

print("Server running on port " + str(PORT) + ", you can connect remotely (same network) by typing \"" + socket.gethostbyname(socket.gethostname()) + ":" + str(PORT) + "\" into the URL of a browser.")

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update(
{
    ".js" : "application/javascript",
    ".wasm" : "application/wasm"
});

httpd = socketserver.TCPServer(("", PORT), Handler)
httpd.serve_forever()
