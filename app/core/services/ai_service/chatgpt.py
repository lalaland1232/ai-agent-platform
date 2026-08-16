import requests
from dotenv import load_dotenv
load_dotenv()
import os
import json
from app.core.contracts.AI import AI
class ChatGpt(AI):
    try:
        def get_prompt(self, data: dict) -> str:
            prompt=f"""
                    genereate a prompt for task which can do {data['agent_details']} 
                    input format is {data['input_format']} and output format is {data['output_format']} 
                    and agent name is {data['agent_name']} 
                    constraints: give prompt including main prompt and input output given 
                    and constraints decide it yourself and give me only prompt without any other text

                """
            response=requests.post("https://openrouter.ai/api/v1/chat/completions",headers={
                "Authorization": f"Bearer {os.getenv('API_KEY')}",
                "Content-Type": "application/json"
            },json={
                "model":"openrouter/free",
                "messages":[{"role":"user","content":prompt}]
            })
            if response.status_code==200:
                return response.json()["choices"][0]["message"]["content"]
      
    except Exception as e:
        print(f"Error occurred while generating response: {e}")

    def generate_response(self,prompt:str,input_data:dict)-> str:
        try:
            response=requests.post("https://openrouter.ai/api/v1/chat/completions",headers={
                "Authorization": f"Bearer {os.getenv('API_KEY')}",
                "Content-Type": "application/json"
            },json={
                "model":"openrouter/free",
                "messages":[{"role":"user","content":f"{prompt}+context\n: {input_data}"}],
                
            })      
            if response.status_code==200:
                return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"Error occurred while generating response: {e}")
            
