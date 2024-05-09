from typing import Any


class CustomMiddleware: 
    def __init__(self, get_response):
        self.get_response = get_response
        print("class based middleware - one time initialization")


    def __call__(self,request):
        print("class based middleware - before view call")
        response = self.get_response(request)
        print("class based middleware - after view call")
        return response
    


def my_middleware(get_response):
    print("function based middleware - one time initialization")
    def middleware(request):
        print("function based middleware - before view call")
        response = get_response(request)
        print("function based middleware - after view call")
        return response
    return middleware