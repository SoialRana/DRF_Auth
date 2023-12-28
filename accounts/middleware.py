from django.utils import timezone
from .models import BlacklistedToken
from django.http import JsonResponse

class BlacklistTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request contains a token
        authorization_header = request.headers.get('Authorization', '')
        if authorization_header.startswith('Bearer '):
            token = authorization_header.split()[1]
            if BlacklistedToken.objects.filter(token=token).exists():
                return JsonResponse({'detail': 'Token is blacklisted'}, status=401)

        response = self.get_response(request)
        return response