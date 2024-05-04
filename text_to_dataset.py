import openai
import json
import os

from dotenv import load_dotenv

load_dotenv()


def generate_qa_pairs(model_name='gpt-3.5-turbo', output_file='2.jsonl'):

    openai.api_key = os.getenv('OPENAI_API_KEY')


    with open(output_file, 'w', encoding='utf-8') as file:
        while True:  # 무한 루프로 계속 입력받기
            text = input("문장을 입력해주세요 (종료하려면 'exit' 입력): ")
            if text.lower() == 'exit':
                print("프로그램을 종료합니다.")
                break  # 'exit' 입력시 루프 종료
            # if not text.strip():  # 입력이 비었는지 확인
            #     print("입력이 비어있습니다. 유효한 문장을 입력해주세요.")
            #     continue  # 입력이 비어있으면 데이터 생성을 건너뛰고 계속 입력 받기

            # 응답 생성 요청
            answer_prompt = {
                "model": model_name,
                "messages": [{"role": "user", "content": f" 다음 지문으로 질문-응답쌍을 만들 것 입니다. 지문의 정보를 빠짐없이 전부 담은 응답이어야 합니다.(질문-응답쌍의 대답이라는 점을 기억해주세요)(응답에 해당하는 부분만 생성해주세요 질문은 만들지 말아주세요)\n지문 : {text} ."}]

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