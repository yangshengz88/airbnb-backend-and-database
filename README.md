#  [`Fullstack Airbnb Clone`](http://13.58.48.85/) - Next.js 15 / React, Tailwind, Django, Django Rest Framework, Postgresql, AWS EC2

 Click [`Airbnb Clone`](http://13.58.48.85/) to see the whole website

This repo is the only backend part of Fullstack Airbnb Clone project. You can find the front part here [`airbnb-frontend`](https://github.com/yangshengz88/airbnb-frontend).

## What I Use
Frontend:

- Next.js 15 / React
- Tailwind
- Typescript
- Node.js 20

Backend:
- Django
- Django rest framework
- Docker compose
- Postgresql
- JWT-based Authentication
- Nginx

Deployment on AWS EC2


## Getting Started locally

First, run the backend development server locally:

```bash
docker compose -f docker-compose.yml up --build
```
Then, run the [`frontend development server`](https://github.com/yangshengz88/airbnb-frontend) locally:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```
Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.
