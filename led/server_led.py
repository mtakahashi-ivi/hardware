# -*- coding:utf-8 -*-
import cgi
import RPi.GPIO as GPIO
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler


class MyHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/serial':
            form = cgi.FieldStorage(fp=self.rfile, headers=self.headers,
                                    environ={'REQUEST_METHOD':'POST'})
            code = form['code'].value
            print code

            if code == "led1":
                GPIO.output( 14, True )
            elif code == "led2":
                GPIO.output( 15, True )
            elif code == "led3":
                GPIO.output( 18, True )
            elif code == "reset":
                GPIO.output( 14, False )
                GPIO.output( 15, False )
                GPIO.output( 18, False )

            self.send_response(100)
            self.send_header('Content-type', 'text/html')
            return
        return self.do_GET()

GPIO.setmode( GPIO.BCM )
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.output( 14, False )
GPIO.output( 15, False )
GPIO.output( 18, False )
server = HTTPServer(('', 8081), MyHandler).serve_forever()

