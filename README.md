# django-switchtemplatedir
Django middleware - symply switch template dir
<h2>Setup</h2>

```python
    git pull https://github.com/haykhman/django-switchtemplatedir.git
```

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```

<h2>In settings.py</h2>
<p>Add 'APP_DIR.TemplateDirManager.TemplateDirMiddleware'</p>
<p>Add TEMPLATE_DIR_METHOD string 'switch' or 'subdomain'.</p>
<p>Add TEMPLATE_DIR_SETTINGS dictionary as defoult key named 'default' with value dict with first value string</p>
<p>If need change file format then set value-dict second fild '.format'</p>
<p>Example - TEMPLATE_DIR_SETTINGS = {'default':[''], 'd' : ['desktop/'], 'm':['mobile/', '.html']}</p>

<h3>Usage</h3>
<p></p>
