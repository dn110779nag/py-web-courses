from tastypie.authentication import Authentication

class CustomAuthentication(Authentication):
    def is_authenticated(self, request, **kwargs):
        if request.method == 'GET':
            return True
        else:
            return super().is_authenticated(request, **kwargs)