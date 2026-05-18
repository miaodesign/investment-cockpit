from datetime import datetime
import json

def handler(environ, start_response):
    body = json.dumps({"status": "ok", "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')})
    start_response('200', [('Content-Type', 'application/json; charset=utf-8'), ('Access-Control-Allow-Origin', '*')])
    return [body.encode('utf-8')]
