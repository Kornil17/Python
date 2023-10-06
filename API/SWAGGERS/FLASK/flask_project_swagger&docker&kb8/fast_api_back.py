from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
app = FastAPI()
# app.add_middleware(HTTPSRedirectMiddleware)

@app.get("/")
def main_page():
    return 'Welcome to our website!'


@app.get("/test")
def endpoint():
    return "It's the test page"
@app.get('/html', response_class=HTMLResponse)
def html():
    html_content = """
        <html>
            <head>
                <title>Some HTML in here</title>
            </head>
            <body>
                <h1>Look ma! HTML!</h1>
            </body>
        </html>
        """
    return HTMLResponse(content=html_content, status_code=200)

if __name__ == '__main__':
    uvicorn.run("fast_api_back:app", host="0.0.0.0", port=4444, reload=True)

# if __name__ == '__main__':
#     uvicorn.run("fast_api_back:app", host="0.0.0.0", port=8080, reload=True, ssl_keyfile='./certbot/conf/live/webspace.moscow/privkey.pem',ssl_certfile='./certbot/conf/live/webspace.moscow/fullchain.pem')

