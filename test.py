from openai import OpenAI
from pydantic import BaseModel

# Define the schema for the response
class FriendInfo(BaseModel):
    name: str
    age: int 
    is_available: bool

class FriendList(BaseModel):
    friends: list[FriendInfo]



client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama', # required, but unused
)

# response = client.chat.completions.create(
#   model="deepseek-r1:1.5b",
#   messages=[
#             {"role": "user", "content": "I have two friends. The first is Ollama 22 years old busy saving the world, and the second is Alonso 23 years old and wants to hang out. Return a list of friends in JSON format"}
#         ],
    
# )
# print(response.choices[0].message.content)



response = client.beta.chat.completions.parse(
  model="deepseek-r1:1.5b",
  messages=[
            {"role": "user", "content": "I have two friends. The first is Ollama 22 years old busy saving the world, and the second is Alonso 23 years old and wants to hang out. Return a list of friends in JSON format"}
        ],
        response_format=FriendList,
)
#print(response.choices[0].message.content)

friendlist = FriendList.model_validate_json(response.choices[0].message.content)
for friend in friendlist.friends:
    print(friend.name)
    print(friend.age)
    print(friend.is_available)

