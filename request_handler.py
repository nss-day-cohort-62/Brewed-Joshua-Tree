import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from views import get_all_products
from views import get_all_employees
from views import get_all_orders


class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def parse_url(self, path):  # NOTE: This is a method (it is written in a class.)
        """Parse the url into the resource and id"""
        parsed_url = urlparse(path)
        path_params = parsed_url.path.split("/")
        resource = path_params[1]

        if parsed_url.query:
            query = parse_qs(parsed_url.query)
            return (resource, query)

        pk = None
        try:
            pk = int(path_params[2])
        except (IndexError, ValueError):
            pass
        return (resource, pk)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers"""
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE")
        self.send_header(
            "Access-Control-Allow-Headers", "X-Requested-With, Content-Type, Accept"
        )
        self.end_headers()

    def do_GET(self):
        """Handle Get requests to the server"""

        # Need to put a default response
        response = None

        # Need the parse URL to grab the returned tuple
        (resource, id) = self.parse_url(self.path)  # connects to defined lists

        # get_all_products initialized here

        if resource == "products" or "orders":
            response = get_all_products()
            # get_single_product()
        elif resource == "orders":
            response = get_all_orders()
        elif resource == "employees":
            response = get_all_employees()
        else:
            response = None
        if response is not None:
            self._set_headers(200)
        else:
            self._set_headers(404)
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Make a post request to the server"""

    def do_PUT(self):
        """Handles PUT requests to the server"""

    def do_DELETE(self):
        """Handle DELETE Requests"""


def main():  # NOTE: This is a function (Outside of class)
    """Starts the server on port 8088 using the HandleRequests class"""
    host = ""
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
