import openai
openai.api_key = "YOUR_API_KEY"

def generate_text(prompt, length=100, temperature=0.5):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=length,
        n=1,
        stop=None,
        temperature=temperature,
    )

    text = response.choices[0].text
    return text.strip()
