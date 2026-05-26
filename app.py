from fastapi import FastAPI
from agent import Agent08
app = FastAPI(title="Educational-Tutor")
agent = Agent08()

@app.post("/execute")
async def execute(payload: dict):
    return agent.execute(payload)
