from fastapi import FastAPI
import random
import string as strp

num = ""
result = ""
arr = list(strp.ascii_letters + strp.digits)
apps = FastAPI()
@apps.get("/generator")


def get_data():
   return{
       "Твой пароль" : result
   }
num = random.choices(arr, k=8)
result = "".join(num)