import re

def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""


def get_str_from_food_dict(food_dict: dict):
    return ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])

if __name__ == "__main__":
    print(get_str_from_food_dict({"samosa": 3, "chole": 2}))

    # print(extract_session_id("projects/ayesha-chatbot-for-food-d-wh9i/agent/sessions/8bda609a-36f4-5607-15a7-2a3cdc861da3/contexts/ongoing-order"))