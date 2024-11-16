From python:3.9
SHELL ["powershell", "pip install plyer"]
COPY BlogReminder.pyw /BlogReminder.pyw
CMD ["python", "/BlogReminder.pyw"]