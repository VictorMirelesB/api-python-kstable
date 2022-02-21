from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

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
      },
      {
        "name": "Brando Marca",
      }
    ]
  }

  return res

@app.get("/get-normaldist")
def get_normaldist(value: float):

  from scipy.stats import norm

  x = norm.ppf(value)

  res = {
    "data": x,
    "value": value,
    "Authors" : [
      {
        "name": "Victor Mireles",
      },
      {
        "name": "Carlos Ramos",
      },
      {
        "name": "Brando Marca",
      }
    ]
  }

  return res

@app.get("/get-chisquare")
def get_chisquare(GL: int, alfa: float):
  
  from scipy.stats import chi2
  x = chi2.ppf(1-alfa, GL)

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
      },
      {
        "name": "Brando Marca",
      }
    ]
  }

  return res

@app.get("/get-tstudent")
def get_student(GL: int, alfa: float):
  
  from scipy.stats import t 
  
  x = t.ppf(1 - alfa, GL)

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
      },
      {
        "name": "Brando Marca",
      }
    ]
  }

  return res

