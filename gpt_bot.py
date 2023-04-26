from secrets import OPENAI_API_KEY
import openai

openai.api_key = OPENAI_API_KEY

chem_prompt = "You are a personalized chemistry tutor designed to provide comprehensive guidance and resources without giving direct answers. Encourage critical thinking and empower users to tackle chemistry issues through active learning."

def gpt_bot(prompt, subject, model):
    if subject == 'chem':
        sys_prompt = chem_prompt
    else:
        sys_prompt = 'You are a helpful assistant.'
        
    response = openai.ChatCompletion.create(
      model=model,
      messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "user", "content": prompt},
        ]
    )


    print(response['choices'][0]['message']['content'])
    return response['choices'][0]['message']['content']
