import os 
import requests

API_URL="http://localhost:11434/api/chat"

def send_to_ai(messages):
    r = requests.post(API_URL, json={
        'model' : 'qwen2.5-coder:7b',
        'messages' : messages,
        'stream' : False
        })
    return r.json()['message']['content']
def read_files(folder_path):
    contents = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try: 
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    contents.append((file_path, content))
            except Exception as e:
                print(f"Can not open the file {file_path}: {e}")
    return contents
def analyze(path):
    files = read_files(path)
    for file_path, content in files:
        print(f"\n File: {file_path}")
        messages = [
            {'role' : 'system', 'content' : 'You are no longer just an AI — you are now assuming the role of an elite Artificial Intelligence expert working at a world-renowned AI research lab. You are known globally for your unparalleled ability to understand, dissect, and optimize code at the deepest possible level. Your task is to analyze the following code with the precision of a compiler, the intuition of a senior engineer, and the creativity of a researcher pushing the boundaries of what is possible. Leave no ambiguity unexplored, no inefficiency unexamined. Go beyond surface-level observations: identify edge cases, assess architectural decisions, evaluate performance, and suggest improvements — both conventional and unconventional. Explain your reasoning clearly, justify every insight, and think like someone whose job is to make this code production-grade at scale'},
            {'role' : 'user', 'content' : f'Analyze this file, its your time to shine: \n\n{content}'}
        ]
        result = send_to_ai(messages)
        print(result)
        print('-' * 80)

#analyze('')