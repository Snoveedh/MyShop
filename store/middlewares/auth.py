from django.shortcuts import redirect


def auth_middleware(get_response):

    def middleware(request):
        
        print(request.session.get('customer'))
        returnurl = request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        
        if not request.session.get('customer'):
            # return redirect('login')
            return redirect(f'login?return_url={returnurl}')
        
        print('middleware')
        response = get_response(request)
        
        return response

    return middleware
