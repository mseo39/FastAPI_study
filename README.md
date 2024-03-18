# FastAPI

## python 가상환경에서 설치 및 띄워보기
```python
pip install fastapi
pip install uvicorn
pip intstall hypercorn
# 띄우기
python -m uvicorn main:app --reload
```
### uvicorn이란?
* Python으로 작성된 고성능 비동기 웹 서버
* ASGI (Asynchronous Server Gateway Interface) 프레임워크를 사용하여 비동기 웹 애플리케이션을 처리
* 가벼우면서도 높은 성능을 제공

### fasr api에서 uvicorn을 왜 사용해?
* FastAPI는 ASGI(Asynchronous Server Gateway Interface)를 사용하여 비동기 웹 애플리케이션을 구축하는 데 중점을 둔 웹 프레임워크
* Uvicorn은 비동기 처리를 지원하여 대용량 트래픽을 처리할 때 높은 성능을 제공
* FastAPI는 ASGI를 기반으로 구축되었으며, Uvicorn도 ASGI를 지원
* FastAPI는 비동기 코드 작성을 지원하며, Uvicorn은 이를 효율적으로 실행