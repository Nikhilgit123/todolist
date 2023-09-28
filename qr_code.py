import pyqrcode
from pyqrcode import QRCode
link = "192.168.43.155/lets grow more web-dev/demo/let-s-grow-more-main/Task1 To-do_List/index.html"
ce = pyqrcode.create(link)
ce.svg("web.svg" ,scale=9)