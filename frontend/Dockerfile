FROM node:12.16.1-alpine As builder

WORKDIR /usr/src/app
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run-script build --prod

FROM nginx:1.15.8-alpine

COPY ./nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /usr/src/app/dist/ /usr/share/nginx/html
EXPOSE 80
