from django.utils import timezone
from .models import BlacklistedToken
from django.http import JsonResponse,HttpResponse

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
    
    
class MyMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("One time my initialization")
        
    def __call__(self,request):
        # Code to be executed for each request before the view (and later middleware) are called.
        print("This is before view")
        response=self.get_response(request)
        # Code to be executed for each request/response after the view is called.
        print("this is after view")
        return response    
    
    
class BrotherMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("One time brother initialization")
        
    def __call__(self,request):
        # Code to be executed for each request before the view (and later middleware) are called.
        print("This is Brother before view")
        response=self.get_response(request)
        # Code to be executed for each request/response after the view is called.
        print("this is Brother after view")
        return response 
    

class FatherMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("One time father initialization")
        
    def __call__(self,request):
        # Code to be executed for each request before the view (and later middleware) are called.
        print("This is Father before view")
        # response=self.get_response(request)
        response=HttpResponse("EKhane thekei se response peye jabe") # view function can't execute
        # Code to be executed for each request/response after the view is called.
        print("this is Father after view")
        return response 
    
    
class MotherMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("One time mother initialization")
        
    def __call__(self,request):
        # Code to be executed for each request before the view (and later middleware) are called.
        print("This is Mother before view")
        response=self.get_response(request)
        # Code to be executed for each request/response after the view is called.
        print("this is Mother after view")
        return response 
    

# process_view 
class MyProcessMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        
    def __call__(self,request):
        response=self.get_response(request)
        return response
    
    def process_view(request,*args, **kwargs):
        print("This is process view -before view")
        # return HttpResponse("This is before view") # jodi HttpResponse return kore taile se view k call korbe na and ekhan thekei se response diye dibe
        return None 


class MyExceptionMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        
    def __call__(self,request):
        response=self.get_response(request)
        return response
    
    def process_exception(self,request,exception):
        print("Exception occured")
        msg=exception
        class_name=exception.__class__.__name__
        print(class_name)
        print(msg)
        return HttpResponse(msg)


class MyTemplateResponseMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        
    def __call__(self,request):
        response=self.get_response(request)
        return response
    
    def process_template_response(self,request,response):
        print("Process template response from Middleware")
        response.context_data['name']='karim'
        return response 

    # function based middleware
""" def my_middleware(get_response):
    print("one time initialization")
    def my_function(request):
        print("This is before view")
        response=get_response(request)
        print("this is after view")
        return response
    return my_function """
