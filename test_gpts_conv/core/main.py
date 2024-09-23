from openai import OpenAI

client = OpenAI(api_key='API HERE')

from utils.tools import GetBehavior
from utils.logs import PrintLog, PrintError



class   Agent():
    def __init__(self, role, behavior):
        self.role = role
        self.behavior = behavior
        self.history = []

    def request(self, new_prompt):
        prompt = 'rappel Comportement: ' + self.behavior + '\n' + new_prompt
        msg = self.history.copy()
        msg.append({'role': 'user', 'content': prompt})
        self.history.append({'role': 'user', 'message': new_prompt})
        generated = client.chat.completions.create(
            model="gpt-4",
            messages=msg
        )
        output = generated.choices[0].message.content
        PrintLog(f'============= {self.role}:\n\n{output}')
        self.history.append({'role': 'assistant', 'message': output})
        return output


if __name__ == '__main__':
    try:
        thinker = Agent('thinker', GetBehavior('thinker'))
        assistant = Agent('assistant', GetBehavior('assistant'))

        new_request = 'Start.'
        PrintLog('\n========    START    ========\n\n')
        while True:
            new_request = thinker.request(new_request)
            new_request = assistant.request(new_request)

    except Exception as error:
        print(error)
