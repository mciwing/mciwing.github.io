FROM python:3.12-alpine3.20 AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /site

# install git
RUN apk add --no-cache git

# Set-up the environment
COPY pyproject.toml uv.lock /site/ 
# Sync without updating the uv.lock file
RUN uv sync --frozen

# copy the project
COPY . .

# disable mkdocs-git-revision-date-localized-plugin &
# mkdocs-git-committers-plugin-2
ENV ENABLE_GIT_COMMITTERS=false
ENV ENABLE_GIT_REVISION_DATE=false

# build the site
RUN uv run mkdocs build

# use a lightweight server for production
FROM nginx:alpine

# copy the built static files from the builder stage
COPY --from=builder /site/site /usr/share/nginx/html

EXPOSE 80

# start nginx in foreground
CMD ["nginx", "-g", "daemon off;"]
