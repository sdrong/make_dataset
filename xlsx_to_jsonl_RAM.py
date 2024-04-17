import pandas as pd
import json

# JSONL 파일에 저장할 데이터 형식을 정의합니다.
data = []

# xlsx 파일에서 데이터를 읽어와 JSONL 파일에 저장합니다.
df = pd.read_excel('data/sdd_skhynix_oem.xlsx', skiprows=6)
for index, row in df.iterrows():
    # 각 행마다 message 리스트를 감싸는 딕셔너리를 생성합니다.
    message_data = {
        "messages": [
            # 첫 번째 메시지: 시스템 메시지
            {
                "role": "system",
                "content": "Your chatbot is a factual chatbot that is also sarcastic."
            },
            # 두 번째 메시지: 사용자 메시지
            {
                "role": "user",
                "content": str(row[1]) + "에 대해 설명해줘"
            },
            # 세 번째 메시지: 어시스턴트 메시지
            {
                "role": "assistant",
                "content": str(row[1]) + "은 " + str(row[2]) + "모델명을 가지고 있으며, 인터페이스는 " + str(row[3]) + "이며, 폼펙터는 " + str(row[4]) + "이며, 용량은 " + str(row[5]) + "이며, product status는 " + str(row[6]) + "이다."
            }
        ]
    }
    data.append(message_data)

# JSONL 파일에 데이터를 씁니다.
with open('dataset/sdd_skhynix_oem.jsonl', 'w', encoding='utf-8') as jsonlfile:
    for message_data in data:
        json.dump(message_data, jsonlfile, ensure_ascii=False)
        jsonlfile.write('\n')
