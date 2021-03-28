from fastapi import FastAPI, status, Depends
from schemals import Blog
from database import SessionLocal, engine, get_db
import models
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"message": "Hello World"}


@app.get('/blogs')
def get_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get("/blogs/{id}")
def read_blog(id: int):
    return {"blog_id": id}


@app.post("/blogs/")
def create_blog(request: Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.put("/blogs/{id}")
async def update_blog(id: int, request: Blog):
    results = {"title": request.title, "content": request.body}
    return results
