FROM python:latest

WORKDIR /backend

COPY ./back/requirements.txt ./backend/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r ./backend/requirements.txt

COPY ./back/test_api ./

CMD ["uvicorn", "test_api:app", "--host", "0.0.0.0", "--port", "8080"]



FROM python:latest

WORKDIR /backend

RUN pip3 install fastapi==0.103.1 & \
uvicorn==0.23.2
RUN pip3 install fastapi uvicorn
COPY ./ ./backend

CMD ["uvicorn", "backend.test_api:app", "--host", "0.0.0.0", "--port", "8080"]




FROM python:latest

WORKDIR /backend

COPY ./back/requirements.txt ./backend/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r ./backend/requirements.txt

COPY ./back/test_api.py ./backend/test_api.py

CMD ["uvicorn", "backend.test_api:app", "--host", "0.0.0.0", "--port", "8080"]

"result file"
FROM python:latest

WORKDIR /backend

COPY ./back/requirements.txt ./backend/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r ./backend/requirements.txt

COPY ./back/test_api.py ./backend/test_api.py

CMD ["uvicorn", "backend.test_api:app", "--host", "0.0.0.0", "--port", "8080"]