#!/bin/bash

if [[ "${1}" == "celery" ]]; then
  celery -A core.tasks.tasks worker -l INFO
elif [[ "${1}" == "celery-beat" ]]; then
  celery -A core.tasks.tasks beat -l INFO
elif [[ "${1}" == "flower" ]]; then
  celery -A core.tasks.tasks flower
 fi