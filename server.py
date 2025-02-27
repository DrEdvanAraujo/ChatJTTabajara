import http.server
import socketserver
import webbrowser

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

handler = Handler
httpd = socketserver.TCPServer(("", PORT), handler)

print(f"Servidor rodando em http://localhost:{PORT}")
webbrowser.open(f"http://localhost:{PORT}")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("Encerrando servidor...")
    httpd.server_close()
