FROM python:latest

WORKDIR /backend

COPY ./requirements.txt ./backend/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r ./backend/requirements.txt

COPY ./ ./backend

CMD ["uvicorn", "backend.test_api:app", "--host", "0.0.0.0", "--port", "80"]



FROM python:latest

WORKDIR /backend

RUN pip3 install fastapi==0.103.1 & \
uvicorn==0.23.2
RUN pip3 install fastapi uvicorn
COPY ./back/test_api.py ./

CMD ["uvicorn", "test_api:app", "--host", "0.0.0.0", "--port", "80"]