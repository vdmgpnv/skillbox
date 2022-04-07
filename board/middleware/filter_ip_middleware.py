from itertools import count
from django.core.exceptions import PermissionDenied
import time


count = 0

class FilterIPMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
        
    def __call__(self, request):
        allowed_ips = ['127.0.0.1']
        ip = request.META.get('REMOTE_ADDR')
        if ip not in allowed_ips:
            raise PermissionDenied
        
        response = self.get_response(request)
        
        return response
    
    
class PauseForEvery5request:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
        
    def __call__(self, request):
        global count
        count += 1
        if count == 5:
            time.sleep(10)
            count = 0
            
        response = self.get_response(request)
        
        return response
    
    