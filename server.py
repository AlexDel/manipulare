import os
import sys
import json

from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.template import Template, Context
from django.views.decorators.http import require_GET, require_POST
from django.views.static import serve
from django.views.decorators.csrf import csrf_exempt
from process import predict

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

ALLOWED_HOSTS = ['*']

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

settings.configure(
  DEBUG=True,
  SECRET_KEY=SECRET_KEY,
  ALLOWED_HOSTS=ALLOWED_HOSTS,
  ROOT_URLCONF=__name__,
  MIDDLEWARE_CLASSES=(
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
  ),
  STATIC_URL = '/static/',
  STATIC_ROOT = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'media'),
  TEMPLATES = [
    {
      'BACKEND': 'django.template.backends.django.DjangoTemplates',
      'DIRS': [],
      'APP_DIRS': True
    },
  ],
  TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.static',
  )
)

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
      <div ng-app="bias">
        <bias-wrapper>
        </bias-wrapper>
      </div>
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
@csrf_exempt
def estimate(req):
  reqObj = json.loads(req.body.decode('utf-8'))
  code = reqObj['code']
  if code != 'test':
    return HttpResponse('Invalid code', status=401)
  else:
    estimation = predict(reqObj['text'])
    return JsonResponse(estimation)

urlpatterns = [
  url(r'^$', index),
  url(r'^api/text/estimate$', estimate),
  url(r'^static/(.*)$', serve, {'document_root': STATIC_ROOT, 'show_indexes': True}),
]


application = get_wsgi_application()


if __name__ == "__main__":
  from django.core.management import execute_from_command_line

  execute_from_command_line(sys.argv)