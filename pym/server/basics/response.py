class Response:
    """
    Represents an HTTP response.

    This class stores the HTTP status line, headers, and body, and provides
    methods to safely modify headers and status before the response is sent
    to the client.

    Once the response has been marked as sent, headers and status can no
    longer be modified.
    """

    def __init__(self):
        """
        Initialize a new Response object with default values.

        status: HTTP status line (default: '200 OK')
        headers: List of (name, value) header tuples
        body: Raw response body as bytes
        sent: Indicates whether the response has already been sent
        """
        self.status = '200 OK'
        self.headers = []
        self.body = b''
        self.sent = False

    def header(self, name, value, replace=True):
        """
        Add or modify an HTTP header.

        Args:
            name (str): Header name (e.g. 'Content-Type').
            value (str): Header value.
            replace (bool, optional): If True, replaces any existing header
                with the same name (case-insensitive). Defaults to True.

        Raises:
            RuntimeError: If headers have already been sent.
        """
        if self.sent:
            raise RuntimeError('Headers already sent')

        if replace:
            self.headers = [
                (k, v) for k, v in self.headers if k.lower() != name.lower()
            ]

        self.headers.append((name, value))

    def modstatus(self, status):
        """
        Modify the HTTP response status line.

        Args:
            status (str): New HTTP status line (e.g. '404 Not Found').

        Raises:
            RuntimeError: If headers have already been sent.
        """
        if self.sent:
            raise RuntimeError('Headers already sent')

        self.status = status

    def redirect(self, location, status='302 Found'):
        """
        Configure the HTTP response as a redirect.

        Args:
            location (str): Target URL or path for the redirection.
            status (str): HTTP status line to use for the redirect
                (e.g. '302 Found', '301 Moved Permanently').

        Raises:
            RuntimeError: If headers have already been sent.
        """

        self.modstatus(status)
        self.header('Location', location)

    def cookie(
        self,
        name,
        value,
        path='/',
        httponly=True,
        secure=False,
        samesite='Lax'
    ):
        """
        Set an HTTP cookie.

        Args:
            name (str): Cookie name.
            value (str): Cookie value.
            path (str): Cookie path.
            httponly (bool): Prevent access from JavaScript.
            secure (bool): Send cookie only over HTTPS.
            samesite (str): SameSite policy ('Lax', 'Strict', 'None').
        """

        parts = [f"{name}={value}", f"Path={path}"]

        if httponly:
            parts.append("HttpOnly")
        if secure:
            parts.append("Secure")
        if samesite:
            parts.append(f"SameSite={samesite}")

        self.header(
            'Set-Cookie',
            '; '.join(parts),
            replace=False
        )