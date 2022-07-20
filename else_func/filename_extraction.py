from pathlib import Path

file_path = r"C:\Users\user\Documents\data_generation\program\file9.csv"

file_name = Path(file_path).stem

print(file_name)