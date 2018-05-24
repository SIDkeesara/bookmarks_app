from django.http import HttpResponse
from django.shortcuts import render

def main_page(request):
    output = '''
    <html>
    <head><title>%s</title></head>
    <body>
    <h1>%s</h1>
    <p>%s</p>
    </body>
    </html>''' % (
        'DJango Bookmarks',
        'Welcome to DJango Bookmarks',
        'Where you can store and share bookmarks !!', )

    return HttpResponse(output)    
