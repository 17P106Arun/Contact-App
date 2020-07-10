from wsgiref.simple_server import make_server
import falcon
class Contact(object):
    def on_get(self,req,resp):
        resp.status=falcon.HTTP_200
        resp.content_type = 'text/html'
        with open('file1.html', 'r') as f:
            resp.body = f.read()
if __name__ == '__main__':
    api=falcon.API()
    api.add_route('/',Contact())
    with make_server('',5000,api) as httpd:
        httpd.serve_forever()
