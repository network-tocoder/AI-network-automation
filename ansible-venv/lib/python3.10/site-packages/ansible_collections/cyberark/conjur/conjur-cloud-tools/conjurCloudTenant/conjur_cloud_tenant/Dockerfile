FROM python:3.12-bullseye

# Provide Poetry with the minimal information needed to build
#   the virtual environment and only later COPY our codebase.
# This allows us to take advantage of Docker's layer caching
#   and avoid reinstalling dependencies when the codebase changes.
COPY pyproject.toml poetry.lock README.md /
COPY .netrc /root/.netrc

RUN pip install poetry

# Poetry caches downloaded packages so that they can be
#   re-used for future installation commands but we don't
#   require this in a Docker image so we can cleanup space
#   by deleting this
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# Poetry --no-root will avoid installing the current project into the virtual environment
RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

# Copy the codebase into the image
COPY . /

# Install the project's dependencies without dev dependencies
RUN poetry install --without dev

WORKDIR /

ENTRYPOINT ["poetry", "run", "python", "conjur_cloud_tenant.py"]