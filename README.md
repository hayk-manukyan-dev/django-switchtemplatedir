# django-switchtemplatedir
Django middleware - symply switch template dir
<h2>Setup</h2>

```sh
    git pull https://github.com/haykhman/django-switchtemplatedir.git
```

<h3>In settings.py</h3>
<p>Add 'APP_DIR.TemplateDirManager.TemplateDirMiddleware'</p>
<p>Add TEMPLATE_DIR_METHOD string 'switch' or 'subdomain'.</p>
<p>Add TEMPLATE_DIR_SETTINGS dictionary as defoult key named 'default' with value dict with first value string direction of the folder</p>
<p>If need change file format then set value-dict second fild '.format'</p>
<p>Example</p>

```python
    TEMPLATE_DIR_METHOD = 'switch'
    TEMPLATE_DIR_SETTINGS = {'default' : [''], 'd' :  ['desktop/'], 'm' : ['mobile/', '.html']}
```

<p>In this example we use switch method.</p>
<p>Key 'defoult' reach to root folder, 'd' reach to ROOT/desktop folder, 'm' reach to ROOT/mobile and change predetermined in template_name file format to html</p>

<h3>Usage</h3>
<h4>switch</h4>
<p>Recomended to use SwitchTemplateDir method. Import this method from APP_DIR.switcher</p>
<p>In urls add '.../<str:key>' path and switch with key name of TEMPLATE_DIR_SETTINGS</p>
<p>Example</p>    
    
```python
    urls.py
    from APP_DIR.switcher import SwitchTemplateDir
    urlpatterns += [ path('somedir/<str:key>', SwitchTemplateDir.as_view()), ]
```

<p>example url for example settings is /somedir/d for switch to 'desktop/' folder</p>
<p>Or use switchTemplateDir function from TemplateDirManager and give argument one of TEMPLATE_DIR_SETTINGS keys</p>
