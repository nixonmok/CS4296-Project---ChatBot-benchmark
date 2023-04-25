import Bard
import asyncio
import time
from EdgeGPT import Chatbot, ConversationStyle
import openai
import poe

QUESTION = open("codingQuestionAnswer/LeetcodeQuestion.txt","r").read()
POE_KEY = "POE KEY"
CHATGPT_KEY = "CHATGPT KEY"
BARD_KEY = "BARD KEY"

string_response_time = ""

#poe
poe_client = poe.Client(POE_KEY)
#capybara = Sage
start = time.time()
poe_answer = ""
for chunk in poe_client.send_message("capybara", QUESTION):
    pass
poe_answer = chunk["text"]
print(poe_answer)
print(f"\nresponse time:{time.time()-start}")

open("codingQuestionAnswer/PoeAnswer.py","w").write(poe_answer)
string_response_time += f"POE's response time:{time.time()-start}\n"
#poe end

#chatGPT3.5
openai.api_key = CHATGPT_KEY
def ask(prompt, model="gpt-3.5-turbo"):
    response = openai.ChatCompletion.create(
        model=model,
        messages=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0,
    )
    return response['choices'][0]['message']['content']
testCase = [
    {"role": "user", "content": QUESTION},
]
start = time.time()
chatGPT_answer = ask(testCase)
print(f"response: {chatGPT_answer}\ntime used: {time.time()-start}")

open("codingQuestionAnswer/ChatGPTAnswer.py","w").write(chatGPT_answer)
string_response_time += f"ChatGPT's response time:{time.time()-start}\n"
#chatGPT3.5 end

#bing ai chat
async def main():
    bot = Chatbot(cookie_path='./cookies.json')
    start = time.time()
    response = bot.ask_stream(prompt=QUESTION, conversation_style=ConversationStyle.balanced, wss_link="wss://sydney.bing.com/sydney/ChatHub")
    messageNeeded = None
    async for message in response:
        messageNeeded = message  
    print("Reponse:\n----------------\n",messageNeeded[1]['item']['messages'][1]['text'],f'\n----------------Response time: {time.time()-start}')     

    await bot.close()
    return messageNeeded[1]['item']['messages'][1]['text'], time.time()-start


bing_answer,bing_response_time = asyncio.run(main())
open("codingQuestionAnswer/BingAnswer.py","w").write(bing_answer)
string_response_time += f"Bing's response time:{time.time()-start}\n"
#bing ai chat end

#google bard
chatbot = Bard.Chatbot(BARD_KEY)
start = time.time()
bard_answer = chatbot.ask(QUESTION)
print(bard_answer['content'],f'\n----------------Response time: {time.time()-start}')

open("codingQuestionAnswer/BardAnswer.py","w").write(bard_answer['content'])
string_response_time += f"Bing's response time:{time.time()-start}\n"
#bard end

open("CodingQuestionAnswer/ResponseTime.txt","w").write(string_response_time)
print(string_response_time)