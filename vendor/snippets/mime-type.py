# Author: Reganto -> https://gitlab.com/reganto


# Show pdf

class PDFHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header('content-type', 'application/pdf')
        with open('sample.pdf', 'rb') as f:
            self.write(f.read())


# Automatic download pdf

class PDFHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header('content-type', 'application/pdf')
        self.set_header('content-disposition', 'attachment; filename=sample.pdf')
        with open('sample.pdf' as 'rb'):
            self.write(f.read())

