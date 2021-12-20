from fastapi import FastAPI

app = FastAPI()

@app.get("/get-kstable")
def get_kstable(GL: int, alfa: float):
  
  from scipy.stats import ksone
  x = ksone.ppf(1-alfa/2, GL)

  res = {
    "data": x,
    "Grado de Libertad": GL,
    "Alfa": alfa,
    "Authors" : [
      {
        "name": "Victor Mireles",
      },
      {
        "name": "Carlos Ramos",
      }
    ]
  }

  return res