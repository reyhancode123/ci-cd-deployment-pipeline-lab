import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from app.main import get_app_info


class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path not in ("/", "/health"):
            self.send_response(404)
            self.end_headers()
            return
        data = get_app_info()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

server = HTTPServer(("0.0.0.0", 8000), AppHandler)
print("Application listening on port 8000")
server.serve_forever()
