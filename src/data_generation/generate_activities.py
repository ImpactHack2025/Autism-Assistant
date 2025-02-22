from utils import get_client, store_to_json_file, response_format_for_user_profile, response_format_for_activities


def generate_user_profile(client, index=0):
    response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",  # "gpt-3.5-turbo-1106",  # or "gpt-4-1106-preview"
        messages=[
            {"role": "system",
             "content": "You are an assistant that generates activities for family with autism children in JSON format. "
                        "The activity is for the children. The activity could be both online of off-line. Make sure the the activity looks real."
                        "If the activity is online, make sure to include the link to the website. If the activity is off-line, make sure to include the city and venue address."},

            {"role": "user", "content": "Generate a activity in JSON format."}
        ],
        response_format=response_format_for_activities
    )

    user_profile = response.choices[0].message.content

    path = f"activities/{index}.json"
    store_to_json_file(content=user_profile, path=path)

    return user_profile


def main():
    profile_numer = 10
    client = get_client()
    for i in range(profile_numer):
        generate_user_profile(client, index=i+1)


# Run the app
if __name__ == "__main__":
    main()
