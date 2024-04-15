import csv
import json

# JSONL 파일에 저장할 데이터 형식을 정의합니다.
data = []

# CSV 파일에서 데이터를 읽어와 JSONL 파일에 저장합니다.
with open('data/cpu_amd_ryzen.csv', 'r', newline='', encoding='utf-8') as csvfile:
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
                    "content": row[0] + "은 " + row[1] + " 제품군이며, " + row[2] + " 시리즈이며, " + row[3] + " 폼팩터를 지원하며 " +
                               row[4] + " 개의 CPU 코어 수를 가지고 있고, " + row[5] + " 개의 스레드로 구성되어 있으며, 최대 부스트 클럭은 " + row[6] + "이며, 베이스 클럭은 " + row[7] + "이며, " +
                               "L2 cache는 " + row[8] + "이며, L3 cache는 " + row[9] + "이며, Default TDP는 " + row[10] + "이며, L1 cache는 " + row[11] + "이며, " +
                               "AMD Configurable TDP는 " + row[12] + "이며, process Technology for CPU Cores는 " + row[13] + "이며, overclocking 락 여부는 " + row[14] + "이며, " +
                               "CPU 소켓은 " + row[15] + "이며, Thermal Solution (PIB)는 " + row[16] + "이며, 추천 쿨러는 " + row[17] + "이며, " +
                               "Thermal Solution (MPK)는 " + row[18] + "이며, Max Operating Temperature (Tjmax)는 " + row[19] + "이며, 출시일은 " + row[20] + "이며, " +
                               "OS Support는 " + row[21] + "이며, PCI Express Version은 " + row[22] + "이며, System Memory Type은 " + row[23] + "이며, " +
                               "Memory Channels는 " + row[24] + "이며, System Memory Specification은 " + row[25] + "이며, Graphics Model은 " + row[26] + "이며, " +
                               "Graphics Core Count는 " + row[27] + "이며, Graphics Frequency는 " + row[28] + "이며, AMD Ryzen AI 사용 가능 여부는 " + row[29] + "이며, " +
                               "Product ID Boxed는 " + row[30] + "이며, Product ID Tray는 " + row[31] + "이며, Product ID MPK는 " + row[32] + "이며, " +
                               "지원 기술은 " + row[33] + "이다."
                }
            ]
        }
        data.append(message_data)

# JSONL 파일에 데이터를 씁니다.
with open('dataset/cpu_amd_ryzen.jsonl', 'w', encoding='utf-8') as jsonlfile:
    for message_data in data:
        json.dump(message_data, jsonlfile, ensure_ascii=False)
        jsonlfile.write('\n')
