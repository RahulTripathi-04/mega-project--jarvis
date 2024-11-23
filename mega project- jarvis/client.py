'''import openai
OpenAI_API_KEY
openai.api_key = os.environ['OPENA']





from openai import OpenAI

client = 
  # Replace with your actual API key

response = client.chat.completions.create(model="gpt-3.5-turbo",  # Use a valid model
messages=[{"role": "user", "content": "Hello, how are you?"}])

print(response.choices[0].message.content)












from openai import OpenAI
client = OpenAI(

    api_key=
)

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)






ompletion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "you are a virtual assistant named jarvis skilled in general task like alexa and Google cloud"},
        {"role": "system", "content": "what is coding"}
    ]
)
print(completion.choices[0].message)'''