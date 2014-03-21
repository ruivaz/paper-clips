import xml.parsers.expat

def expat_parse(f, target):
  parser = xml.parsers.expat.ParserCreate()
  parser.buffer_size = 65536
  parser.buffer_text = True
  parser.returns_unicode = False
  parser.StartElementHandler = \
  	lambda name,attrs: target.send(('start',(name,attrs)))
  parser.EndElementHandler = \
 	lambda name: target.send(('end',name))
  parser.CharacterDataHandler = \
 	lambda data: target.send(('text',data))
  parser.ParseFile(f)
