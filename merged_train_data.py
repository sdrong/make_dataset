from pathlib import Path

# 파일 리스트
file_list = ['dataset/cpu_amd_merged_train_data.jsonl','dataset/cpu_Intel_merged_train_data.jsonl','dataset/gpu_merged.jsonl','dataset/gpu_qna_merged.jsonl','dataset/motherBoard_merged.jsonl','dataset/power.jsonl','dataset/qna_augmented.jsonl','dataset/ram_merged.jsonl','dataset/ssd_merged.jsonl',]

# 새로운 파일 경로
output_file_path = 'dataset/all.jsonl'

# 모든 파일을 읽고 새 파일에 내용을 쓰기
with open(output_file_path, 'w') as outfile:
    for file_name in file_list:
        with open(file_name, 'r') as infile:
            for line in infile:
                outfile.write(line)

print(f"All files merged into {output_file_path}")
