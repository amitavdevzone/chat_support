from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/api/webhook")
async def webhook(request: Request, token):
    body = await request.json()
    message = body.get("content")
    print(f"Body is: {message}")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=3002, reload=True)
