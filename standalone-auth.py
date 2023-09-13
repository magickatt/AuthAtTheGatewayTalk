from http.server import BaseHTTPRequestHandler, HTTPServer
from auth import authenticate_request
from database import create_database_connection
import logging

database_connection = create_database_connection()

class StandaloneAuth(BaseHTTPRequestHandler):

    def do_GET(self):
        if (user := authenticate_request(self.headers, database_connection)):
            self.send_header("x-mycompany-user-id", user.user_id)
            self.send_header("x-mycompany-user-name", user.name)
            self.send_response(200)
        else:
            self.send_response(401)
        self.end_headers()

if __name__ == "__main__":        
    host = ""
    port = 8080
    http_server = HTTPServer((host, port), StandaloneAuth)
    logging.info("Standalone Auth started at http://%s:%s", host, port)

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        pass

    http_server.server_close()
    logging.info("Standalone Auth stopped.")
