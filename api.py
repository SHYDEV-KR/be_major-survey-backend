import requests
import json
import os

headers = {
    "Authorization": os.getenv("NOTION_SECRET_KEY"),
    "Accept": "application/json",
    "Notion-Version": "2022-06-28"
}

def generate_new_page_in_db(db_id, submitted_form):
  request_url = "https://api.notion.com/v1/pages"
  body_data = {
    "parent" : { "database_id" : db_id },
    "properties": {
      "age": {
        "rich_text": [
          {
              "text": {
                  "content": submitted_form["age"]
              }
          }
        ]
      },   
      "gender": {
        "rich_text": [
          {
            "text": {
              "content": submitted_form["gender"]
            }
          }
        ]
      },
      "major": {
        "rich_text": [
          {
            "text": {
              "content": submitted_form["major"]
            }
          }
        ]
      },   
      "career": {
        "rich_text": [
          {
            "text": {
              "content": submitted_form["career"]
            }
          }
        ]
      },
      "correlation": {
        "rich_text": [
          {
            "text": {
              "content": submitted_form["correlation"]
            }
          }
        ]
      },   
      "needs": {
        "rich_text": [
          {
            "text": {
              "content": submitted_form["needs"]
            }
          }
        ]
      },
      "feedback": {
        "rich_text": [
          {
            "text": {
              "content": submitted_form["feedback"]
            }
          }
        ]
      },   
      "insta": {
        "rich_text": [
          {
              "text": {
                "content": submitted_form["insta"]
              }
            }
        ]
      },
      "phone": {
          "rich_text": [
            {
              "text": {
                "content": submitted_form["phone"]
              }
            }
          ]
      }   
    } 
  }

  response = requests.post(request_url, json=body_data, headers=headers)
  if response.status_code == 200:
    json_data = json.loads(response.text)
    return json_data
  else:
    print(response)
    return f"{response.status_code}"