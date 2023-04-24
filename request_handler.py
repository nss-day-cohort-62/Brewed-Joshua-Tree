import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from views import (
    get_all_products,
    get_single_product,
    create_product,
    get_all_employees,
    get_single_employee,
    get_all_orders,
    get_single_order,
)


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
        self.send_header("Access-Control-Allow-Methods",
                         "GET, POST, PUT, DELETE")
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

        if resource == "products":
            if id is not None:
                response = get_single_product(id)
            else:
                response = get_all_products()
        elif resource == "orders":
            if id is not None:
                response = get_single_order(id)
            else:
                response = get_all_orders()
        elif resource == "employees":
            if id is not None:
                response = get_single_employee(id)
            else:
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
        # Frankie products create
        self._set_headers(201)
        content_len = int(self.headers.get("content-length", 0))
        post_body = self.rfile.read(content_len)

        post_body = json.loads(post_body)

        (resource, id) = self.parse_url(self.path)
        # resource, id = self.parse_url(self.path)

        new_dictionary = None

        if resource == "products":
            new_dictionary = create_product(post_body)

        # elif resource == "employees":
        #     new_dictionary = create_employee(post_body)
        # elif resource == "orders":
        #     new_dictionary = create_order(post_body)
        # else:
        #     new_dictionary = {
        #         "message": f'{"Post could not be completed."}'
        #         }

        self.wfile.write(json.dumps(new_dictionary).encode())

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
