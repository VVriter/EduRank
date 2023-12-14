FROM node
EXPOSE 80
WORKDIR ./
COPY . .
RUN yarn install
CMD ["yarn", "host"]