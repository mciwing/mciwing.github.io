FROM python:3.12-slim AS builder

WORKDIR /site

# install git
RUN apt-get update && apt-get install -y git && apt-get clean

# install dependencies
COPY pyproject.toml poetry.lock ./
RUN python -m pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

# copy the project
COPY . .

# disable mkdocs-git-revision-date-localized-plugin &
# mkdocs-git-committers-plugin-2
ENV ENABLE_GIT_COMMITTERS=false
ENV ENABLE_GIT_REVISION_DATE=false

# build the site
RUN mkdocs build

# use a lightweight server for production
FROM nginx:alpine

# copy the built static files from the builder stage
COPY --from=builder /site/site /usr/share/nginx/html

EXPOSE 80

# start nginx in foreground
CMD ["nginx", "-g", "daemon off;"]
