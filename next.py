from src.data_generation.utils import get_client, store_to_json_file, response_format_for_user_profile
import json
import random





def read_activities(activity_numer):
    activities = []
    # Set your lower and upper bounds
    file_index_lower_bound = 0
    file_index_upper_bound = 10
    activity_numer = 5
    for _ in range(activity_numer):
        index=random.randint(file_index_lower_bound, file_index_upper_bound) 
        file_name = f"/Users/darragh/GitHub repos/Autism-Assistant/src/data_generation/activities/{index}.json"
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


def recommend_next_activity(user_profile):
    #read activities
    activity_number = 5
    activities = read_activities(activity_number)

    #recommend
    recommended_actiity_index = recommend(user_profile, activities)  

    print(recommended_actiity_index)
   




    #test

    return recommended_actiity_index

def main():
    # profile_numer = 10
    # client = get_client()
    # for i in range(profile_numer):
    #     generate_user_profile(client, index=i+1)

    user_profile_file_name="/Users/darragh/GitHub repos/Autism-Assistant/src/data_generation/user_profiles/1.json"
    with open(user_profile_file_name, 'r') as content_file:
            user_profile=json.load(content_file)

    recommend_next_activity(user_profile)


# Run the app
if __name__ == "__main__":
    main()
