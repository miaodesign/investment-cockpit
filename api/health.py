"""
Health Check API
"""
from datetime import datetime
import json

def handler(environ, start_response):
    headers = [
        ('Content-Type', 'application/json; charset=utf-8'),
        ('Access-Control-Allow-Origin', '*'),
    ]
    body = json.dumps({"status": "ok", "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
    start_response('200', headers)
    return [body.encode('utf-8')]
