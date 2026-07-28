FROM python:3-alpine AS build
COPY ./ /app
RUN cd /app && pip install build && python -m build -w

FROM python:3-alpine
ENV PYTHONDONTWRITEBYTECODE=1
RUN apk add --no-cache git
COPY --from=build /app/dist/tarjinja*.whl /dist/
RUN --mount=type=cache,target=/root/.cache pip install --no-compile /dist/*.whl
ENTRYPOINT ["tarjinja"]
