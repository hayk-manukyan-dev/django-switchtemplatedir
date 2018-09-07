from django.conf import settings

template_dir_settings = settings.TEMPLATE_DIR_SETTINGS

from urllib.parse import urlsplit

template_dir = 'default'

def switchTemplateDir(dir):
    global template_dir
    template_dir = dir



class GetTemplateDir(object):
    def subdomain(self, request):
        bits = urlsplit(request.META['HTTP_HOST'])[0].split('.')[0]
        if bits in template_dir_settings:
            return template_dir_settings[bits]
        raise ValueError('TempateDirManager.GetTemplateDir >> subdomain was not registered in settings.TEMPLATE_DIR_SETTINGS')

    def switch(self, request):
        if template_dir in template_dir_settings:
            return template_dir_settings[template_dir]
        print('+++++++  ' + str(template_dir))
        raise ValueError('TemplateDirSwitcher >> switcher was not registered in settings.TEMPLATE_DIR_SETTINGS')

    def templateDir(self, request):
        return getattr(GetTemplateDir(), settings.TEMPLATE_DIR_METHOD)(request)



class TemplateDirMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        template_dir = GetTemplateDir().templateDir(request)
        print('--1--')
#        try:
        print('--2--')
        response = self.get_response(request)
        if type(template_dir) == list and len(template_dir) > 0:
            print('if')
            response.template_name = [response.template_name[0].split('.')[0] + template_dir[1]]
            print(response.template_name[0])
        response.template_name =  [template_dir[0] + str(response.template_name[0])]
        print(response.template_name)
        response.content = response.rendered_content
        print('--3--')
        return response
#        except:
#            print('--4--')
#            return self.get_response(request)


