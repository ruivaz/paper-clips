from django.http import HttpResponse
import datetime

def hello(request):
  return HttpResponse("Hello World")

def current_time(request):
  now = datetime.datetime.now()
  return HttpResponse(now)

def hours_ahead(request, offset):
  try:
    offset = int(offset)
  except ValueError:
    raise Http404()
  dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
  return HttpResponse(dt)
     

