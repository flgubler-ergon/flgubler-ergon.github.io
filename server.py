import http.server

# Beware: this script must be executed in the context of the `docs` folder.
# this means, open a console in the `docs` folder and from there, run `python ../server.py`

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Send CSP header
        self.send_header("Content-Security-Policy", "default-src 'self' ws:; style-src 'self' 'unsafe-inline'; img-src 'self' data:; script-src 'self'; object-src 'none'; trusted-types angular dompurify default webpack-dev-server#overlay; require-trusted-types-for 'script'")
        # Send Frame-Options header
        self.send_header("X-FRAME-OPTIONS", "SAMEORIGIN")
        # Call superclass's end_headers()
        http.server.SimpleHTTPRequestHandler.end_headers(self)

# Create server object
server = http.server.HTTPServer(("", 5050), MyHTTPRequestHandler)
# Start server
server.serve_forever()
