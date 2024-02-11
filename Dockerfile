FROM python:slim-bookworm

WORKDIR /app

COPY . /app 
RUN for file in $(grep -Rin localhost /app 2>/dev/null | awk -F: '{print $1}' | uniq); do \
sed -i 's/localhost:8000/fastapi:8000/g' $file; \
done
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8001
CMD ["streamlit", "run", "--server.port", "8001", "login.py"]
