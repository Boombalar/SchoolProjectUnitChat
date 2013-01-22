import web

urls = (
	'/', 'index','/world','world'
)
app = web.application(urls,globals())

class index:
	def GET(self):
		return "Hello, "  + "!"

if __name__ == "__main__":
	app.run()
