import logging

logger = logging.getLogger(__name__)

class AuthCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):
        logger.debug(f"[AuthCheckMiddleware] Path: {request.path}")
        logger.debug(f"[AuthCheckMiddleware] Is user authenticated: {request.user.is_authenticated}")
        logger.debug(f"[AuthCheckMiddleware] User: {request.user}")
        
        response = self.get_response(request)
        
        logger.debug(f"[AuthCheckMiddleware] After response - Is user authenticated: {request.user.is_authenticated}")
        return response