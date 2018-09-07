from django.conf import settings

from django.shortcuts import redirect
from django.views import View
from TemplateDirManager import switchTemplateDir


class SwitchTemplateDir(View):
    def get(self, request, *args, **kwargs):
        if kwargs['key'] in settings.TEMPLATE_DIR_SETTINGS:
            switchTemplateDir(kwargs['key'])
            return redirect(request.META.get('HTTP_REFERER'))
        raise ValueError('TemplateDirSwitcher >> switcher was not registered in settings.TEMPLATE_DIR_SETTINGS')

    def post(self, request, *args, **kwargs):
        if request.POST['key'] in settings.TEMPLATE_DIR_SETTINGS:
            switchTemplateDir(request.POST['key'])
            if request.POST['redirect']:
                return redirect(request.POST['redirect'])
            return redirect(request.META.get('HTTP_REFERER'))
        raise ValueError('TemplateDirSwitcher >> switcher was not registered in settings.TEMPLATE_DIR_SETTINGS')
