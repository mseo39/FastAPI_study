from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel
import requests

app=FastAPI()

db=[]

#====================
#
#=====================
class City(BaseModel):
    name: str
    timezone: str

class CityModify(BaseModel):
    id: int
    name:str
    timezone: str

templates = Jinja2Templates(directory="templates")

@app.get("/")
def root():
    return {"Hello":"World"}

# 도시 리스트 가져오기
@app.get('/cities', response_class=HTMLResponse)
def get_cities(request: Request):
    context={}
    rsCity = []
    cnt=0
    for city in db:
        strs=f"https://worldtimeapi.org/api/timezone/{city['timezone']}"
        r= requests.get(strs)
        cur_time =r.json()["datetime"]
        cnt+=1
        rsCity.append({'id':cnt,'name':city['name'], 'timezone':city['timezone'], 'current_time':cur_time})
    
    context['request']=request
    context['rsCity']=rsCity

    return templates.TemplateResponse('city_list.html',context)

# 특정 도시 정보 가져오기
@app.get('/cities/{city_id}', response_class=HTMLResponse)
def get_city(request: Request, city_id: int):
    city = db[city_id-1]
    r = requests.get(f"http://worldtimeapi.org/api/timezone/{city['timezone']}")
    cur_time = r.json()['datetime']

    # return {'name':city['name'], 'timezone':city['timezone'], 'current_time': cur_time}
    context = {'request':request, 'name':city['name'], 'timezone':city['timezone'], 'current_time': cur_time}
    return templates.TemplateResponse("city_detail.html", context)

# 등록
@app.post('/cities')
def create_city(city: City):
    db.append(dict(city))
    return db[-1]

# 수정
@app.put('/cities')
def modify_city(city: CityModify):
    db[city.id-1]={'name':city.name, 'timezone':city.timezone}
    #수정된 값을 리턴
    return db[city.id-1]

# 삭제
@app.delete('/cities/{city_id}')
def delete_city(city_id: int):
    db.pop(city_id-1)
    return{}