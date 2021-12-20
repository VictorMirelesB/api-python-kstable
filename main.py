from fastapi import FastAPI

app = FastAPI()

@app.get("/get-kstable")
def get_kstable(GL: int, alfa: float):
  
  from scipy.stats import ksone
  x = ksone.ppf(1-alfa/2, GL)
  return {"data": x, "GL": GL, "alfa": alfa, "author": "Victor Mireles"}