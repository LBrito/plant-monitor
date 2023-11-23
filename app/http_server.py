from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

READINGS_JSON = os.environ["PTM_HOME"] + '/data/readings.json'


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        f = open(READINGS_JSON, 'r')
        readings = json.load(f)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(json.dumps(readings, indent=4), "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer(('0.0.0.0', 8000), MyServer)
    print("Local server started at port 8000")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        webServer.server_close()
        print("Server stopped.")
