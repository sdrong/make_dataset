import json

# JSON 파일로부터 데이터 읽어오기
with open('data/motherBoard_gigabyte_ultraDurable.json', 'r', encoding='utf-8') as json_file:
    json_data = json.load(json_file)

# JSON 데이터를 JSONL 파일로 변환
with open('dataset/motherBoard_gigabyte_ultraDurable.jsonl', 'w', encoding='utf-8') as jsonl_file:
    for item in json_data["products"]:
        jsonl_entry = {
            "messages": [
                {
                    "role": "system",
                    "content": "Your chatbot is a factual chatbot that is also sarcastic."
                },
                {
                    "role": "user",
                    "content": str(item["name"]) + "에 대해 설명해줘"
                },
                {
                    "role": "assistant",
                    "content": str(item["name"]) + "은 " + str(item["description"])
                }
            ]
        }
        jsonl_file.write(json.dumps(jsonl_entry, ensure_ascii=False) + '\n')
