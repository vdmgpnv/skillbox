import datetime


class GetInfo:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
        
    def __call__(self, request):
        with open('log.txt', 'a') as f:
            f.write(request.META.get('REMOTE_ADDR') + datetime.datetime.now().strftime('%m.%h.%y %d.%m.%Y') + '\n')
        
        response = self.get_response(request)
        
        return response