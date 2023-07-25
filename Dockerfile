FROM debian:11

# Set the DEBIAN_FRONTEND variable to avoid interactive prompts during installation
ARG DEBIAN_FRONTEND=noninteractive

# Update the package list and install necessary packages
RUN apt-get update && apt-get -y install \
    python3 python3-dev python3-pip python3-venv

# Set the default user to 'root'
ARG USER=root
USER $USER

# Create a virtual environment named 'venv'
RUN python3 -m venv venv

# Set the working directory inside the container to '/app'
WORKDIR /app

# Copy the 'requirements.txt' file and install the dependencies
RUN pip3 install --upgrade pip
RUN pip3 install --cache-dir=/pip_cache -r requirements.txt
RUN mkdir /pip_cache



# Copy the 'fsubbot.py' file into the container
COPY fsubbot.py .

# Expose port 5000 for the application
EXPOSE 5000

# Run the command to start the 'fsubbot.py' script
CMD python3 fsubbot.py
