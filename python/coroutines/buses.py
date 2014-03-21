import xml.sax
import Queue
from cosax import EventHandler
from coexpat import expat_parse
from threading import Thread

def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.next()
        return cr
    return start

@coroutine
def buses_to_dicts(target):
  while True:
    event, value = (yield)
    if event == 'start' and value[0] == 'bus':
      busdict = {}
      fragments = []
      while True:
        event, value = (yield)
        if event == 'start':  fragments = []
        elif event == 'text': fragments.append(value)
        elif event == 'end': 
          if value != 'bus':
            busdict[value] = "".join(fragments)
          else:
            target.send(busdict)
            break 

@coroutine
def filter_on_field(fieldname, value, target):
  while True:
    d = (yield)
    if d.get(fieldname) == value:
      target.send(d)   

@coroutine
def threaded(target):
  messages = Queue.Queue()
  def run_target():
    while True:
      item = messages.get()
      if item is GeneratorExit:
        target.close()
        return
      else:
        target.send(item)
  Thread(target=run_target).start()
  try:
    while True:
      item = (yield)
      messages.put(item)
  except GeneratorExit:
    messages.put(GeneratorExit)  


@coroutine
def bus_locations():
  while True:
    bus = (yield)
    print "%(route)s,%(id)s,\"%(direction)s\","\
 "%(latitude)s,%(longitude)s" % bus 

xml.sax.parse("buses.xml",
 EventHandler(
 buses_to_dicts(
 filter_on_field("route","147",
 filter_on_field("direction","North Bound",
 bus_locations())))
 ))

expat_parse(open("buses.xml"), 
  buses_to_dicts(
  filter_on_field("route","147",
  filter_on_field("direction","North Bound",
  bus_locations()))
  ))

xml.sax.parse("buses.xml",
 EventHandler(
 buses_to_dicts(threaded(
 filter_on_field("route","147",
 filter_on_field("direction","North Bound",
 bus_locations()))))
 ))
