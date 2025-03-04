import streamlit as st
import openai  # Assumes OpenAI API for AI-powered recommendations
from googletrans import Translator

def get_recommendations(diagnosis, age, interests, needs, language):
    """Generate recommendations based on user input using AI."""
    prompt = f"""
    Provide inclusive activity and support recommendations for a child with {diagnosis}, aged {age}, 
    with interests in {interests} and needs including {needs}. The recommendations should be practical 
    and consider accessibility and available community resources.
    """
    
    openai.api_key = "your-api-key-here"
    
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an inclusive AI assistant."},
                  {"role": "user", "content": prompt}]
    )
    recommendations = response.choices[0].message.content
    
    if language != "English":
        translator = Translator()
        recommendations = translator.translate(recommendations, dest=language).text
    
    return recommendations

# Streamlit UI
st.set_page_config(page_title="Inclusive AI Assistant", layout="wide")
st.title("Inclusive AI Assistant for Families")

st.sidebar.header("Search for Activities and Support")
diagnosis = st.sidebar.text_input("Child's Diagnosis", "Autism, ADHD, etc.")
age = st.sidebar.number_input("Child's Age", min_value=1, max_value=18, step=1)
interests = st.sidebar.text_area("Interests", "Music, Sports, Art, etc.")
needs = st.sidebar.text_area("Specific Needs", "Wheelchair accessible, sensory-friendly, etc.")
language = st.sidebar.selectbox("Preferred Language", ["English", "Somali", "Persian"])

# Initialize recommendations as an empty string
recommendations = ""

if st.sidebar.button("Find Activities & Support"):
    with st.spinner("Finding the best recommendations..."):
        recommendations = get_recommendations(diagnosis, age, interests, needs, language)
        st.subheader("Personalized Recommendations:")
        st.write(recommendations)

# Accessibility Features (Only show if recommendations exist)
if recommendations and st.checkbox("Enable Text-to-Speech"):
    st.write("Click below to hear the recommendations:")
    st.audio("https://translate.google.com/translate_tts?ie=UTF-8&q=" + recommendations + "&tl=" + language.lower() + "&client=tw-ob")

st.info("This AI assistant helps families find inclusive activities and resources tailored to their children's needs.")
