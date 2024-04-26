FROM python:3.10

WORKDIR /code

RUN pip install -U gunicorn autogenstudio

RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH \
    AUTOGENSTUDIO_APPDIR=/home/user/app

WORKDIR $HOME/app

COPY --chown=user . $HOME/app
COPY --chown=user datamodel.py /usr/local/lib/python3.10/site-packages/autogenstudio/datamodel.py
COPY --chown=user workflowmanager.py /usr/local/lib/python3.10/site-packages/autogenstudio/workflowmanager.py
COPY --chown=user dbdefaults.json /usr/local/lib/python3.10/site-packages/autogenstudio/utils/dbdefaults.json

EXPOSE 8081

CMD gunicorn -w $((2 * $(getconf _NPROCESSORS_ONLN) + 1)) --timeout 12600 -k uvicorn.workers.UvicornWorker autogenstudio.web.app:app --bind "0.0.0.0:8081"