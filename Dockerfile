FROM python:3.11-bookworm

EXPOSE 5000
WORKDIR /var/python

COPY entrypoint.sh /usr/local/bin/entrypoint
RUN chmod +x /usr/local/bin/entrypoint

COPY requirements.txt requirements.txt
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

# More concise for a demonstration, usually no need to copy everything
COPY . .

ENV PYTHONPATH "/var/python/src"
ENV PYTHONUNBUFFERED "1"
ENTRYPOINT [ "/usr/local/bin/entrypoint" ]
