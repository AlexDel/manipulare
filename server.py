import os
import sys

from django.conf import settings
from django.http import JsonResponse
from django.template import Template, Context
from django.views.decorators.http import require_GET, require_POST
from process import predict

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

settings.configure(
  DEBUG=DEBUG,
  SECRET_KEY=SECRET_KEY,
  ALLOWED_HOSTS=ALLOWED_HOSTS,
  ROOT_URLCONF=__name__,
  MIDDLEWARE_CLASSES=(
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
  ),
  TEMPLATES = [
    {
      'BACKEND': 'django.template.backends.django.DjangoTemplates',
      'DIRS': [],
      'APP_DIRS': True
    },
  ]
)

from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse


@require_GET
def index(req):
  homepage = '''
  <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
      <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0"/>
      <title>Text bias estimation - SFU Applied linguistics and cognitive research lab</title>

      <!-- CSS  -->
      <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
      <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
      <link href="/static/css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>
      <link href="/static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
    </head>
    <body>
      <!--  Scripts-->
      <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
      <script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.6.5/angular.js"></script>
      <script src="/static/js/materialize.js"></script>
      <script src="/static/js/app.js"></script>

      </body>
    </html>
  '''
  return HttpResponse(Template(homepage).render(Context({})))


@require_POST
def estimate(req):
  code = req.POST['code']
  if code != 'test':
    HttpResponse('Invalid code', status=401)
  else:
    estimation = predict(req.POST['text'])
    return JsonResponse(estimation)

urlpatterns = (
  url(r'^$', index),
  url(r'^api/text/estimate$', estimate)
)


application = get_wsgi_application()


if __name__ == "__main__":
  from django.core.management import execute_from_command_line

  execute_from_command_line(sys.argv)