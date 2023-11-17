import openai
import os
import time
from dotenv import load_dotenv
from mongoengine import connect, StringField, Document

load_dotenv()

class Article(Document):
    title = StringField()
    author = StringField()
    date_published = StringField()
    content = StringField()
    label = StringField()

def app():
    connect(
        db=os.environ.get("DB_NAME"),
        host=os.environ.get("DB_URI")
    )

    openai.api_key = os.environ.get("OPEN_API_KEY")

    prompt = input("prompt : ")
    formatted_prompt = "{prompt}\ntitle : {title}\ncontent : {content}"

    for news in Article.objects():
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": formatted_prompt.format(
                        prompt=prompt,
                        title=news.title,
                        content=news.content
                    )
                 }
            ]
        )

        print("+\tnews : {title}\n\tlabel : {label}\n".format(
            title=news.title,
            label=response.choices[0].message.content))

        news.label = response.choices[0].message.content
        news.save()

        time.sleep(30)

if __name__ == '__main__':
    app()
