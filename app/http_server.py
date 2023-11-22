from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        readings = self.get_sensors()
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(readings, indent=4), "utf-8"))
        
    def get_sensors(self):
        f = open(os.environ["PTM_HOME"] + '/app/data/readings.json', 'r')
        return json.load(f)

if __name__ == "__main__":
    webServer = HTTPServer(('0.0.0.0', 8000), MyServer)
    print("Local server started at port 8000")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")