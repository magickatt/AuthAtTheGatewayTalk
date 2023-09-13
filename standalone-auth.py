from http.server import BaseHTTPRequestHandler, SimpleHTTPRequestHandler, HTTPServer
from auth import authenticate_request
from database import create_database_connection
import logging
from headers import USER_NAME, USER_ID

database_connection = create_database_connection()

class StandaloneAuth(SimpleHTTPRequestHandler):

    def do_GET(self):
        # For the demonstration we just want to allow/deny the orders endpoint,
        # otherwise this would represent any conditional logic you require
        if self.path != "/api-without-auth/orders":
            self.send_response(200)
        else:
        
            # For the orders endpoint we want to handle authentication
            if (user := authenticate_request(self.headers, database_connection)):
                self.send_response(200)
                self.send_header(USER_ID, user.user_id)
                self.send_header(USER_NAME, user.name)
            else:
                self.send_response(401)

        self.send_header("X-Mycompany-Path", self.path)
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
