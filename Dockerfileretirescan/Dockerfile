# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Install retire globally
RUN npm install -g retire

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install app dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Specify the entry point to run retire scan
ENTRYPOINT ["retire", "--outputformat", "json", "--outputpath", "retirejs_scan.json"]
