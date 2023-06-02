FROM node:14-alpine

WORKDIR /app

# Copy package.json and package-lock.json
COPY mangolo/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the app
COPY mangolo/ ./

CMD ["npm", "start"]
