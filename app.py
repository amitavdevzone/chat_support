from fastapi import FastAPI, Request
import uvicorn
import requests

app = FastAPI()

@app.post("/api/webhook")
async def webhook(request: Request, token):
    body = await request.json()
    message = body.get("content")
    if message == 'Hi':
        url =""
        data = {"content": "Hello. How are you?"}
        headers = {"api_access_token": ""}
        response = requests.post(url=url, json=data, headers=headers)
        
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=3002, reload=True)
