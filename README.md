
# News Autolabel

News auto labeling with the power of OpenAI text generation. Retrieve data from mongoDB, labeling it with gpt chat completion feature, and update it back to the db.
## Demo

![Project Demo](https://i.ibb.co/pJjM1FT/18-11-2023-00-40-41-REC.gif "Project Demo")


## Run Locally

Clone the project

```bash
  git clone https://github.com/wiratana/news-autolabel.git
```

Go to the project directory

```bash
  cd news-autolabel
```

Initialize Environment Variable

```bash
  cp example.env .env
  nano .env
```

Build the Container with Docker

```bash
  docker build -t news-autolabel-app .
```

Start the Container with Docker

```bash
  docker run -i news-autolabel-app
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPEN_API_KEY`

`DB_URI`

`DB_NAME`


## Authors

- [@wiratana](https://github.com/wiratana)

