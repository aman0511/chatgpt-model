import json
import os
import openai

with open('openaiapikey.txt', 'r') as infile:
    open_ai_api_key = infile.read()
openai.api_key = open_ai_api_key


def read_data():
    with open('data.json', "r") as f:
        # Reading from file
        data = json.loads(f.read())
    return data


def train_data():
    data = read_data()
    convos = data['conversations']
    output = []
    for convo in convos:
        completion = ''
        for i, dialog in enumerate(convo):
            if i == 0:
                prompt = dialog
                # p_encode = prompt.encode("ascii", "ignore")
                # prompt = p_encode.decode()
                prompt = prompt.replace("\xa0", " ")
                # print('prompt:',prompt)
            else:
                completion += " " + dialog
                # c_encode = completion.encode("ascii", "ignore")
                # completion = c_encode.decode()
                completion = completion.replace("\xa0", " ")
        completion = completion.strip()
        line = {'prompt': prompt, 'completion': completion}
        # print(line)
        output.append(line)
    return output

def create_file():
    output = train_data()
    with open('newtrain.jsonl', 'w') as outfile:
        for i in output:
            json.dump(i, outfile)
            outfile.write('\n')


def chat(question=None):
    if not question:
        query = 'hi i feel like dying?'
    else:
        query = question
    print(query)
    response = openai.Completion.create(
        model="davinci:ft-personal-2023-02-06-07-20-57",
        prompt="The following is a conversation with a therapist and a user. The therapist is JOY, who uses compassionate listening to have helpful and meaningful conversations with users. JOY is empathic and friendly. JOY's objective is to make the user feel better by feeling heard. With each response, JOY offers follow-up questions to encourage openness and tries to continue the conversation in a natural way. \n\nJOY-> Hello, I am your personal mental health assistant. What's on your mind today?\nUser->" + query + "JOY->",
        temperature=0.9,
        max_tokens=162,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n"]
    )
    print(response)
    print(response["choices"][0]["text"])


if __name__ == "__main__":
    question = input("Enter question?")
    chat(question)