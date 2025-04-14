from fastapi import FastAPI, Query
from pydantic import BaseModel
import wikipedia

app = FastAPI()

wikipedia.set_lang("ru")

class WikiRequest(BaseModel):
    topic: str


class WikiResponse(BaseModel):
    topic: str
    summary: str


@app.get("/summary/{topic}", response_model=WikiResponse)
def get_summary(topic: str):
    summary = wikipedia.summary(topic)
    return {"topic": topic, "summary": summary}


@app.get("/search", response_model=list[str])
def search_wikipedia(query: str = Query(..., description="Запрос для поиска на Wikipedia")):
    return wikipedia.search(query)


@app.post("/fetch_summary", response_model=WikiResponse)
def fetch_summary(request: WikiRequest):
    summary = wikipedia.summary(request.topic)
    return {"topic": request.topic, "summary": summary}
