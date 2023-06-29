from datasets import load_dataset
import os

dataset = load_dataset("bigcode/the-stack", data_dir="data/cobol", split="train")

for data in dataset:
    repo_file = os.path.join(data["max_stars_repo_name"], data["max_stars_repo_path"])
    if not os.path.exists(repo_file):
        repo_file = os.path.normpath(repo_file)
        print(repo_file)
        dir = os.path.dirname(repo_file)
        if not os.path.exists(dir):
            os.makedirs(dir)
        if not os.path.exists(repo_file):
            with open(repo_file, 'w') as file:
                try:
                    file.write(data["content"])
                    print(f"Write {os.path.basename(repo_file)}")
                except UnicodeEncodeError:
                    print("UnicodeEncodeError in {repo_file}")
