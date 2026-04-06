from fastapi import Request
from fastapi.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware


class TokenRefreshMiddleware(BaseHTTPMiddleware):
    """
    Middleware that automatically includes a new access token in response headers
    when the authentication dependency has refreshed an expired token.
    """
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        
        # Check if a new access token was generated during the request
        if hasattr(request.state, 'new_access_token'):
            # Add the new access token to response headers
            response.headers["New-Access-Token"] = request.state.new_access_token
        
        return response
