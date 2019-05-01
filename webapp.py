import web
render = web.template.render('templates/')
url = ( '/','index')

class index:
 def GET(self):
  name = 'sudi'
  return render.index(name)

if __name__ == "__main__":
 app = web.application(url,globals())
 app.run()
