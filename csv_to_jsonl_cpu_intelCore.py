import csv
import json

# JSONL 파일에 저장할 데이터 형식을 정의합니다.
data = []

# CSV 파일에서 데이터를 읽어와 JSONL 파일에 저장합니다.
with open('data/cpu_intel_intelCore.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # 헤더를 건너뜁니다.
    for row in reader:
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
                    "content": row[0] + "에 대해 설명해줘"
                },
                # 세 번째 메시지: 어시스턴트 메시지
                {
                    "role": "assistant",
                    "content": row[0] + "은 " + row[1] + " 제품군이며, " + row[2] + " 시리즈이며, " + row[3] + "개의 CPU cores 수와 " +
                    row[4] + "개의 스레드 수를 가지고 있으며, MAX Boost Clock은 " + row[5] + "이며, Base clock은 " + row[6] + "이며, All Core Boost Clock은 " +
                    row[7] + "이며, L3 Cache는 " + row[8] + "이며, 1ku Pricing은 " + row[9] + "이며, Defalut TDP는 " + row[10] +
                    "이며, AMD COnfigurable TDP (cTDP)는 " + row[11] + "이며, CPU socket은 " + row[12] + "이며, Socket Count는 " + row[13] +
                    "PCI Express Version은 " + row[14] + "이며, System Memory Type은 " + row[15] + "이며, Memory Channels는 " + row[16] +
                    "이며, System Memory Specification은 " + row[17] + "이며, Per Socket Mem BW는 " + row[18] + "이며, Product Id Boxed는 " + row[19] +
                    "이며, product ID Tray는 " + row[20] + "이고, 지원 기술은 " + row[21] + "이다."
                }
            ]
        }
        data.append(message_data)

# JSONL 파일에 데이터를 씁니다.
with open('dataset/cpu_amd_intelCore.jsonl', 'w', encoding='utf-8') as jsonlfile:
    for message_data in data:
        json.dump(message_data, jsonlfile, ensure_ascii=False)
        jsonlfile.write('\n')
