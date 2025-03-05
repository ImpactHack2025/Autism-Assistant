let selectedLanguage = 'en';
        
const translations = {
    en: {
        welcome: "Welcome!",
        message: "Click a button to hear the text.",
        calm: "I feel calm",
        focus: "I need focus",
        schedule: "Daily Schedule",
        breakfast: "Time for breakfast",
        playtime: "Time to play",
        nap: "Time to rest",
        emotions: "How Do You Feel?",
        happy: "I am happy",
        sad: "I am sad",
        excited: "I am excited"
    },
    so: {
        welcome: "Soo Dhawoow!",
        message: "Guji badhanka si aad u maqasho qoraalka.",
        calm: "Waan deganahay",
        focus: "Waxaan u baahanahay feejignaan",
        schedule: "Jadwal Maalinle ah",
        breakfast: "Waqtiga quraacda",
        playtime: "Waqtiga ciyaarta",
        nap: "Waqtiga nasashada",
        emotions: "Sidee dareemaysaa?",
        happy: "Waan faraxsanahay",
        sad: "Waan murugaysanahay",
        excited: "Waan xiisay"
    },
    fa: {
        welcome: "خوش آمدید!",
        message: "برای شنیدن متن، روی یک دکمه کلیک کنید.",
        calm: "من آرام هستم",
        focus: "من نیاز به تمرکز دارم",
        schedule: "برنامه روزانه",
        breakfast: "زمان صبحانه",
        playtime: "زمان بازی",
        nap: "زمان استراحت",
        emotions: "احساس شما چیست؟",
        happy: "من خوشحالم",
        sad: "من ناراحتم",
        excited: "من هیجان زده هستم"
    }
};

function speakText(key) {
    let speech = new SpeechSynthesisUtterance(translations[selectedLanguage][key]);
    speech.lang = selectedLanguage === 'fa' ? 'fa-IR' : selectedLanguage === 'so' ? 'so-SO' : 'en-US';
    speech.rate = 0.8;
    window.speechSynthesis.speak(speech);
}

function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
}

function changeLanguage() {
    selectedLanguage = document.getElementById('language').value;
    document.getElementById('welcome-text').innerText = translations[selectedLanguage].welcome;
    document.getElementById('message').innerText = translations[selectedLanguage].message;
    document.getElementById('calm-btn').innerText = translations[selectedLanguage].calm;
    document.getElementById('focus-btn').innerText = translations[selectedLanguage].focus;
    document.getElementById('schedule-title').innerText = translations[selectedLanguage].schedule;
    document.getElementById('breakfast').innerText = "🍽️ " + translations[selectedLanguage].breakfast;
    document.getElementById('playtime').innerText = "🎮 " + translations[selectedLanguage].playtime;
    document.getElementById('nap').innerText = "🛏️ " + translations[selectedLanguage].nap;
    document.getElementById('emotion-title').innerText = translations[selectedLanguage].emotions;
    document.getElementById('happy').innerText = "😊 " + translations[selectedLanguage].happy;
    document.getElementById('sad').innerText = "😢 " + translations[selectedLanguage].sad;
    document.getElementById('excited').innerText = "😃 " + translations[selectedLanguage].excited;
}

function signUp() {
    alert('Sign Up button clicked');
}

function register() {
    alert('Register button clicked');
}