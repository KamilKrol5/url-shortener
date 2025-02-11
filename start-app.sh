#!/bin/bash

set -e
poetry run python src/url_shortener/manage.py runserver 0.0.0.0:8005
