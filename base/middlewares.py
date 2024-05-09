from typing import Any


class CustomMiddleware: 
    def __init__(self, get_response):
        self.get_response = get_response
        print("one time initialization")


    def __call__(self,request):
        print("before view call")
        response = self.get_response(request)
        print("after view call")
        return response
    

