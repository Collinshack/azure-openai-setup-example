
#Example1
import os
from openai import AzureOpenAI
    
client = AzureOpenAI(
    api_key= "REPLACE_WITH_YOUR_KEY_VALUE_HERE", 
    api_version="2024-02-01",
    azure_endpoint ="REPLACE_WITH_YOUR_KEY_VALUE_HERE"
    )
    
deployment_name="REPLACE_WITH_YOUR_KEY_VALUE_HERE" 


prompt = 'Write me 5 post titles on AI'
response = client.completions.create(model=deployment_name, prompt=prompt, max_tokens=10)
print(response.choices[0].text)






#Example2
 
import os  
from openai import AzureOpenAI  
    
endpoint = os.getenv("ENDPOINT_URL", "REPLACE_WITH_YOUR_KEY_VALUE_HERE")  
deployment = os.getenv("DEPLOYMENT_NAME", "REPLACE_WITH_YOUR_KEY_VALUE_HERE")  
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "REPLACE_WITH_YOUR_KEY_VALUE_HERE")  
    
    # Initialize Azure OpenAI client with key-based authentication
client = AzureOpenAI(  
        azure_endpoint=endpoint,  
        api_key=subscription_key,  
        api_version="2024-05-01-preview",  
    )  
      
    # Prepare the chat prompt  
chat_prompt = [
    {
        "role": "system",
        "content": "You are an AI assistant that helps people find information."
    }
]  
    
    # Include speech result if speech is enabled  
speech_result = chat_prompt  
    
    # Generate the completion  
completion = client.chat.completions.create(  
        model=deployment,  
        messages=speech_result,  
        past_messages=10,  
        max_tokens=800,  
        temperature=0.7,  
        top_p=0.95,  
        frequency_penalty=0,  
        presence_penalty=0,  
        stop=None,  
        stream=False  
    )  
      
print(completion.to_json())  
    