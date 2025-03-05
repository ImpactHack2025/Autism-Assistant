let selectedLanguage = 'en';
        
const translations = {
    "so": { // Somali
        "welcome-text": "Ku soo dhawoow Kaaliyahaaga Autism!",
        "visit-site": "Booqo Mitt Speciella Barn si aad wax badan uga ogaato!",
        "signup-signin": "Saxiix / Gal",
        "message": "Guji badhanka si aad u maqasho qoraalka!",
        "select-language": "Dooro Luuqadda:",
        "calm-btn": "Dajin",
        "focus-btn": "Diirad saar",
        "toggle-dark": "Beddel Habka Mugdiga",
        "schedule-title": "Jadwalka Maalinlaha ah",
        "breakfast": "🍽️ Quraac",
        "playtime": "🎮 Waqti Ciyaar",
        "nap": "🛏️ Hurdo",
        "emotion-title": "Sidee Dareemaysaa?",
        "happy": "😊 Faraxsan",
        "sad": "😢 Murugaysan",
        "excited": "😃 Waan Faraxsanahay"
    },
    "fa": { // Persian
        "welcome-text": "به دستیار اوتیسم خود خوش آمدید!",
        "visit-site": "برای کسب اطلاعات بیشتر از Mitt Speciella Barn دیدن کنید!",
        "signup-signin": "ثبت نام / ورود",
        "message": "روی یک دکمه کلیک کنید تا متن را بشنوید!",
        "select-language": "زبان را انتخاب کنید:",
        "calm-btn": "آرامش",
        "focus-btn": "تمرکز",
        "toggle-dark": "حالت تاریک را تغییر دهید",
        "schedule-title": "برنامه روزانه",
        "breakfast": "🍽️ صبحانه",
        "playtime": "🎮 زمان بازی",
        "nap": "🛏️ چرت زدن",
        "emotion-title": "احساس شما چگونه است؟",
        "happy": "😊 خوشحال",
        "sad": "😢 ناراحت",
        "excited": "😃 هیجان زده"
    },
    "en": { // English (Default)
        "welcome-text": "Welcome to your Autism Assistant!",
        "visit-site": "Visit Mitt Speciella Barn to learn more about their vision!",
        "signup-signin": "Sign Up / Sign In",
        "message": "Click a button to hear the text!",
        "select-language": "Select Language:",
        "calm-btn": "Calm",
        "focus-btn": "Focus",
        "toggle-dark": "Toggle Dark Mode",
        "schedule-title": "Daily Schedule",
        "breakfast": "🍽️ Breakfast",
        "playtime": "🎮 Playtime",
        "nap": "🛏️ Nap Time",
        "emotion-title": "How Do You Feel?",
        "happy": "😊 Happy",
        "sad": "😢 Sad",
        "excited": "😃 Excited"
    }
};

function changeLanguage() {
    const selectedLang = document.getElementById("language").value;
    const translation = translations[selectedLang];

    if (!translation) return;

    // Loop through all elements with the `data-i18n` attribute
    document.querySelectorAll("[data-i18n]").forEach(element => {
        const key = element.getAttribute("data-i18n");
        if (translation[key]) {
            element.innerText = translation[key];
        }
    });
}

function speakText(key) {
    const selectedLang = document.getElementById("language").value;
    const translation = translations[selectedLang];

    if (!translation || !translation[key]) {
        console.warn("Translation not found for:", key);
        return;
    }

    let textToSpeak = translation[key];

    // Remove emojis and symbols
    textToSpeak = textToSpeak.replace(/[\p{Emoji_Presentation}\p{Extended_Pictographic}]/gu, "").trim();

    const utterance = new SpeechSynthesisUtterance(textToSpeak);

    // Set language for speech synthesis
    utterance.lang = selectedLang === "so" ? "so-SO" : selectedLang === "fa" ? "fa-IR" : "en-US";

    speechSynthesis.speak(utterance);
}


function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
}

function signUp() {
    alert('Sign Up button clicked');
}

function register() {
    alert('Register button clicked');
}