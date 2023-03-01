import pytest
import openai

@pytest.mark.skip(reason="This site is down still.")
def test_open_ai():
    openai.api_key = "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"

    response = openai.Completion.create(
    model="text-davinci-002",
    prompt="Classify the sentiment in these tweets:\n\n1. \"CIERO MERO\"\n2. \"Daddy is the greatest\"\n3. \"Aurora wants to go to wrestling\"\n4. \"My cat has worms\"\n5. \"I hate chocolate\"\n\nTweet sentiment ratings:",
    temperature=0,
    max_tokens=60,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    print(response.choices[0].text)

@pytest.mark.skip(reason="This site is down still.")
def test_generate_picture():
    openai.api_key = "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"

    response = openai.Image.create(
    prompt="fat cat holding a baseball bat",
    n=1,
    size="1024x1024"
    )

    image_url = response['data'][0]['url']

    print(image_url)