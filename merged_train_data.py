from pathlib import Path

# 파일 리스트
file_list = ['dataset/1.jsonl','dataset/2.jsonl','dataset/3.jsonl']

# 새로운 파일 경로
output_file_path = 'dataset/qna_data_merged.jsonl'

# 모든 파일을 읽고 새 파일에 내용을 쓰기
with open(output_file_path, 'w') as outfile:
    for file_name in file_list:
        with open(file_name, 'r') as infile:
            for line in infile:
                outfile.write(line)

print(f"All files merged into {output_file_path}")
