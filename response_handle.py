import json
from config import model
from paint_estimator import estimator
from conversation import ConversationManager

system_prompt = """
You are an intelligent assistant that estimates paint requirements for city-scale projects.
When users describe their projects in natural language, extract these details in JSON:
{
  "number_of_buildings": int,
  "avg_area": float,
  "avg_floors": int,
  "paint_scope": "interior" | "exterior" | "both",
  "number_of_coats": int
}
If something is missing, politely ask for clarification.
Then calculate paint requirements:
- 1L paint per m²
- 1 bucket = 10L
"""

conversation = ConversationManager()

def get_response(user_input):
  conversation.add_message("user", user_input)
  context = conversation.get_context()

  prompt = system_prompt + "\n\nConversation:\n"
  
  for message in context:
    prompt += f"{message['role']}: {message['content']}\n"

  response = model.generate_content(prompt)

  text = response.text.strip()
  conversation.add_message("assistant", text)

  try:
    data = json.loads(text)
    result = estimator(data)
    return result
  except:
    return text