FROM python:3.8-slim as builder

RUN mkdir /install
WORKDIR /install

RUN apt-get update \
    && apt-get install git -y \
    && apt-get install make \
    && apt-get install dos2unix \
    && apt-get install -y --reinstall ca-certificates \
    && pip install pipenv \
    && pip install toml


COPY requirements.txt .
RUN pip install --prefix=/install --ignore-installed -r requirements.txt


FROM python:3.8-slim

ENV TZ=Asia/Bangkok
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


RUN mkdir /home/urbox
RUN adduser urbox

WORKDIR /home/urbox

COPY --from=builder /install /usr/local
COPY app/ app/
COPY flask_app/ flask_app/

COPY entry-point.sh .
COPY manage.py manage.py
COPY flask_manage.py flask_manage.py

RUN sed -i -e 's/\r$//' entry-point.sh
RUN chmod +x entry-point.sh

USER urbox

EXPOSE 8000

#ENTRYPOINT ["./entry-point.sh"]
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]