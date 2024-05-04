import pandas as pd
import json


def load_and_process_data(file_path):
    # 파일을 읽어 데이터프레임으로 로드, 첫 번째 열을 인덱스로 사용
    data = pd.read_csv(file_path, skiprows=2, delimiter=',', index_col=0)
    return data


def convert_to_jsonl(data, file_path):
    # JSONL 파일에 질문-응답 쌍으로 데이터 저장
    with open(file_path, 'w', encoding='utf-8') as f:
        for column in data.columns:
            # 각 열의 데이터를 질문-응답 형태로 추출하여 저장
            descriptions = [f"{index.strip()}: {value.strip()}" for index, value in data[column].dropna().items()]
            description = ", ".join(descriptions)
            qna_pair = {
                "messages": [
                    {
                        "role": "system",
                        "content": "Your chatbot is a factual chatbot that is also sarcastic."
                    },
                    {
                        "role": "user",
                        "content": f"{column.strip()}에 대해 설명해줘"
                    },
                    {
                        "role": "assistant",
                        "content": description
                    }
                ]
            }
            f.write(json.dumps(qna_pair, ensure_ascii=False) + '\n')


def main():
    file_path = 'data/intelCPU/IntelCore_Ultra.csv'
    data = load_and_process_data(file_path)

    # 하나의 JSONL 파일로 모든 데이터 저장
    jsonl_file_path = 'dataset/test/IntelCore_Ultra.jsonl'
    convert_to_jsonl(data, jsonl_file_path)

    print(f'{jsonl_file_path} has been created.')


if __name__ == "__main__":
    main()
