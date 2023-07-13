import openai
from dotenv import load_dotenv
import os
load_dotenv()

print("Connecting chatgpt!")
def ChatGPT(prompt, API_KEY=os.environ.get("YOUR_API_KEY")):

    # api key 設定
    openai.api_key = API_KEY

    # ChatGPT API callおよび最新言語modelであるtext-davinci-003を使う
    # engine = 'text-davinci-003' 'text-curie-001' 'text-babbage-001' 'text-ada-001'
    print("Called to openai!", openai.Completion)
    completion = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = prompt,
        temperature = 0.5,
        max_tokens = 1024,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0)
    print("Get completion!", completion)
    return completion['choices'][0]['text']

def main():
    print("Test to input!")
    # 入力
    prompt = input("Insert a prompt: ")
    print(ChatGPT(prompt).strip())

if __name__ == '__main__':
    main()
