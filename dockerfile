FROM python:alpine

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY . /app

RUN apk install g++ musl-dev python3-dev linux-headers

# Install the required packages
RUN pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python3", "app.py"]
