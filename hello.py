def wsgi_application(environ, start_response):
  # бизнес-логика
  status = '200 OK'
  headers = [
  ('Content-Type', 'text/plain')
  ]
  start_response(status, headers )
  return [ "\r\n".join(environ['QUERY_STRING'].split("&")) ]
