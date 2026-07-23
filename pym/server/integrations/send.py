from pym.server.basics import Response

# Function to send an application response
def send(response: Response, start_response):
    """
    Auxiliary function for sending responses.
    Restricted to `application` function.
    """

    # If not sending a response
    if not response.sent:
        response.sent = True
        start_response(response.status, response.headers)
    
    # Return HTML, resource, etc
    return [response.body]