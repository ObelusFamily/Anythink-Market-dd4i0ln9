import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')


def generate_image(prompt, number_images, size):
    response = openai.Image.create(
            prompt=prompt,
            n=number_images,
            size=size
        )
    return response['data'][0]['url']
    