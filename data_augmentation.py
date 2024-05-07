import openai
import json
import os

from dotenv import load_dotenv

load_dotenv()


def generate_qa_pairs(model_name='gpt-3.5-turbo', output_file='2.jsonl'):

    openai.api_key = os.getenv('OPENAI_API_KEY')


    with open(output_file, 'w', encoding='utf-8') as file:
        while True:  # 무한 루프로 계속 입력받기

            # 응답 생성 요청
            answer_prompt = {
                "model": model_name,
                "messages": [{"role": "user", "content": f"다음 질문을 data augmentation 진행하려고 합니다. 다른 어휘를 사용해서 질문을 새로 생성해 주세요 )\n지문 : {text} ."}]

            }
            answer_response = openai.ChatCompletion.create(**answer_prompt)
            answer = answer_response.choices[0].message['content']

            # 질문 생성 요청
            question_prompt = {
                "model": model_name,
                "messages": [{"role": "user", "content": f"아래 지문에 대한 적절한 질문을 만들어주세요 질문-응답쌍으로 만들 예정이기 때문에 질문에도 적절한 정보가 포함되어야 합니다(어떤 정보에 대한 질문인지 필수로 명시되어야함) {answer}"}]
            }
            question_response = openai.ChatCompletion.create(**question_prompt)
            question = question_response.choices[0].message['content']

            # JSONL 형식으로 저장
            json_data = {
                "messages": [
                    {"role": "system", "content": "Your chatbot is a factual chatbot that is also sarcastic."},
                    {"role": "user", "content": question},
                    {"role": "assistant", "content": answer}
                ]
            }
            file.write(json.dumps(json_data, ensure_ascii=False) + '\n')
            print("데이터가 저장되었습니다.")

generate_qa_pairs()