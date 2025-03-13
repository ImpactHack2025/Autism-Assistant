from flask import Flask, render_template, jsonify
import random
import json
from src.data_generation.utils import get_client

app = Flask(__name__)

def read_activities(activity_numer):
    activities = []
    # Set your lower and upper bounds
    file_index_lower_bound = 0
    file_index_upper_bound = 10
    activity_numer = 5
    for _ in range(activity_numer):
        index=random.randint(file_index_lower_bound, file_index_upper_bound) 
        file_name = f"//home/cheli243/Desktop/CodeToGit/forked-data-generation/Autism-Assistant/src/data_generation/activities/{index}.json"
        with open(file_name, 'r') as content_file:
            activities.append(json.load(content_file))
    return activities

def recommend(user_profile,activities):
    client = get_client()
    user_profile_str = json.dumps(user_profile, indent=2)
    activities_str = "\n".join(
        [f"Index {i}: {json.dumps(activity, indent=2)}" for i, activity in enumerate(activities)]
    )
    # Construct the prompt with clear instructions
    prompt = (
        f"User Profile:\n{user_profile_str}\n\n"
        f"Activities (with indices):\n{activities_str}\n\n"
        "Based on the above, please recommend the best activity for this user. "
        "Return your answer in exactly two lines with no extra text:\n"
        "1. The first line should contain only the index (an integer) of the selected activity.\n"
        "2. The second line should contain only the dictionary of the selected activity (exactly as provided in the input).\n"
    )
    
    # Call ChatGPT API (make sure you have set your OpenAI API key)
    response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",  # or "gpt-3.5-turbo" if that's what you use
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    # response = openai.ChatCompletion.create(
    #     model="gpt-4",  # or "gpt-3.5-turbo" if that's what you use
    #     messages=[
    #         {"role": "user", "content": prompt}
    #     ],
    #     temperature=0.7,
    #     max_tokens=500
    # )
    # Get the assistant's reply
    
    reply = response.choices[0].message.content.strip()
    
  
    recomended_index=reply[0]
    
    return recomended_index


def recommend_next_activity():
    user_profile={}
    #read activities
    activity_number = 5
    activities = read_activities(activity_number)

    #recommend
    recommended_activity_index = recommend(user_profile, activities)  

    # print(recommended_activity_index)
   
    #return "text"

    return activities[recommended_activity_index]










@app.route('/')
def home():
    return render_template('new_index.html')

@app.route('/get_recommendation', methods=['GET'])
def get_recommendation():
    result = recommend_next_activity()
    return jsonify({'recommendation': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
