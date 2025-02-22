from openai import OpenAI
import json
from pydantic import BaseModel
from typing import List, Union
from enum import Enum


def get_client():
    # Load the API key from a file
    with open("../../../API-key", "r") as file:
        content = file.read().strip("\n")
    api_key = content
    if not api_key:
        raise ValueError("API key not found. Set OPENAI_API_KEY environment variable.")

    client = OpenAI(api_key=api_key)
    return client


def store_to_json_file(content, path):
    # Ensure the response is valid JSON
    try:
        user_profile = json.loads(content)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON response from OpenAI API")

    # Save to a file
    with open(path, "w") as file:
        json.dump(user_profile, file, indent=4)


class response_format_for_user_profile(BaseModel):
    name: str
    age: int
    gender: str
    language_preference: str
    city: str
    interests: List[str]
    preferred_sensory: str
    communication_level: str
    communication_method: str
    time_preference: List[str]
    Allergens: List[str]
    emergency_contact_name: str
    emergency_contact_number: str


class collaborate_type(Enum):
    parent_assisted = "Parent_assisted"
    independent = "Independent"
    group_based = "Group-based"


class activity_format(Enum):
    online = "Online"
    offline = "Off-line"
    hybrid = "hybrid"


class response_format_for_activities(BaseModel):
    activity_name: str
    Activity_format: activity_format
    Website: str
    city: str
    venue: str
    age_range: List[int]
    skills_required: List[str]
    sensory_avoid: List[str]
    materials_to_prepare: List[str]
    steps: List[str]
    safety: str
    date: str
    start_at: str
    duration: str
    collborate_type: collaborate_type
    cost: str
    contact_person: str
    contact_number: str
