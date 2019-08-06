from uuid import uuid4


class InjectTrace(object):
    """
        Middleware to inject uuid and IP to the request.

    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """

            This function is to intercept the request besfore and after the view is reached.

            :param request: This param contain all the information associated to the request.
            :param type request: Request
            :return: The request with an uuid and the request ip added.
            :rtype: Request
        """

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        data = {
            'request_uuid': uuid4().hex,
            'ip': ip,
        }

        request.session.update(data)
        response = self.get_response(request)
        return response
