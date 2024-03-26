FROM python:3

WORKDIR /app

#install packages 
#RUN apt install -y python3 python3-pip
#COPY requirements.txt ./
RUN pip install --upgrade pip
#RUN pip install -r  requirements.txt

#copy the rests of the application
COPY . .

#make script executable 
#RUN chmod +x start.sh && ./start.sh

#run script
CMD ["python", "app.py", "sh"]

