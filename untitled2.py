import cgi
import Cookie
import sys
import csv

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class MainHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		p = self.path.split("?")
		params = {}
		if len(p) > 1:
			params = cgi.parse_qs(p[1], True, True)
			with open('log.csv','a') as fluff:
				logwr = csv.writer(fluff,delimiter=',')
				logwr.writerows(params.values())
			fluff.close()

def main(port):
	try:
		server = HTTPServer(('', int(port)), MainHandler)
		print 'started httpserver...'
		server.serve_forever()
	except KeyboardInterrupt:
		print '^C received, shutting down server'
		server.socket.close()

if __name__ == '__main__':
	main(sys.argv[1])
