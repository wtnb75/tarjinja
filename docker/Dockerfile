FROM python:3-alpine
ARG tag=master
RUN apk add --no-cache git
RUN pip install -r https://raw.githubusercontent.com/wtnb75/tarjinja/${tag}/requirements.txt
RUN pip install https://github.com/wtnb75/tarjinja/archive/${tag}.zip
ENTRYPOINT ["tarjinja"]
