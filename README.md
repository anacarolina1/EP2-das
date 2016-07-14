# EP2-das

O projeto está utilizando o *django-plugins*, para criar um plugin que gerencia a criação de urls.

O projeto não está rodando porque ele deu o seguinte erro ao importar o plugin dentro da models.py:

acls@acls:~/EP2-das/ep2$ python manage.py runserver
Unhandled exception in thread started by <function wrapper at 0x7fec88c92050>
Traceback (most recent call last):
  File "/usr/local/lib/python2.7/dist-packages/django/utils/autoreload.py", line 226, in wrapper
    fn(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/django/core/management/commands/runserver.py", line 109, in inner_run
    autoreload.raise_last_exception()
  File "/usr/local/lib/python2.7/dist-packages/django/utils/autoreload.py", line 249, in raise_last_exception
    six.reraise(*_exception)
  File "/usr/local/lib/python2.7/dist-packages/django/utils/autoreload.py", line 226, in wrapper
    fn(*args, **kwargs)
  File "/usr/local/lib/python2.7/dist-packages/django/__init__.py", line 18, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "/usr/local/lib/python2.7/dist-packages/django/apps/registry.py", line 108, in populate
    app_config.import_models(all_models)
  File "/usr/local/lib/python2.7/dist-packages/django/apps/config.py", line 202, in import_models
    self.models_module = import_module(models_module_name)
  File "/usr/lib/python2.7/importlib/__init__.py", line 37, in import_module
    __import__(name)
  File "/home/acls/EP2-das/ep2/ep2Site/models.py", line 5, in <module>
    from ep2Site.plugins import ContentType
  File "/home/acls/EP2-das/ep2/ep2Site/plugins.py", line 8, in <module>
    import ep2Site.views
  File "/home/acls/EP2-das/ep2/ep2Site/views.py", line 2, in <module>
    from forms import ReviewForm
  File "/home/acls/EP2-das/ep2/ep2Site/forms.py", line 3, in <module>
    from .models import Review
ImportError: cannot import name Review

