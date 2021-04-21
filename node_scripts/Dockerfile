FROM node:15.14.0

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install
COPY . .
#COPY run.sh /usr/src/app/run.sh
RUN chmod +x /usr/src/app/run.sh
#COPY run.sh /run.sh

EXPOSE 3000

ENV PATH="/usr/src/app:${PATH}"
#CMD ["npm", "run", "start"]