from django.shortcuts import HttpResponse
from rest_framework.response import Response


class CustomMiddleware: 
    def __init__(self, get_response):
        self.get_response = get_response
        print("class based middleware - one time initialization")


    def __call__(self,request):
        print("class based middleware - before view call")
        response = self.get_response(request)
        print("class based middleware - after view call")
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        '''
        this hook is just called before the view is called
        if you return None, the view will be called
        else it will not be called
        '''
        # print("class based middleware - process view")
        return None
      
        # return HttpResponse(content="reponse from process view",status=400)
        
    def process_exception(self,request, exception): 
        print("class based middleware - process exception")
        return HttpResponse(content=f"reponse from process exception exeption = {exception}",status=400)
    


def my_middleware(get_response):
    print("function based middleware - one time initialization")
    def middleware(request):
        print("function based middleware - before view call")
        response = get_response(request)
        print("function based middleware - after view call")
        return response
    return middleware