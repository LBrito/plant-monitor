from http.server import BaseHTTPRequestHandler, HTTPServer
import sys
import json
from datetime import datetime

sys.path.append('../')
from sensor_board import SensorBoard

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        readings = SensorBoard().read_sensors()
        readings['timestamp'] = datetime.utcnow().isoformat() + 'Z'
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Simple Server</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<pre>" + json.dumps(readings, indent=4) + "</pre>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer(('192.168.1.193', 8000), MyServer)
    print("Local server started at port 8000")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")