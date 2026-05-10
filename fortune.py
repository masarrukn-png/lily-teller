import streamlit as st
import random

# All the text in every language, organized neatly
translations = {
    "English 🇬🇧": {
        "title": "🔮 Magic Fortune Teller 🔮",
        "intro": "I can see your future...",
        "name_prompt": "What is your name, brave seeker?",
        "greeting": "Hello, **{name}** — the spirits know you well!",
        "question_prompt": "Ask me a yes/no question:",
        "you_ask": "Hmm, you ask: *{question}*",
        "button": "🔮 Consult the spirits!",
        "spirits_say": "🔮 The spirits say: **{fortune}**",
        "credit": "✨ Experimental work by Valen from Repton ✨",
        "fortunes": [
            "Yes, definitely!",
            "No way!",
            "Ask again later...",
            "The stars say YES! ⭐",
            "Hmm, doesn't look good 😬",
            "Absolutely!",
            "Try again tomorrow",
            "It is certain!"
        ]
    },
    "Français 🇫🇷": {
        "title": "🔮 La Diseuse de Bonne Aventure 🔮",
        "intro": "Je peux voir ton avenir...",
        "name_prompt": "Quel est ton nom, brave chercheur?",
        "greeting": "Bonjour, **{name}** — les esprits te connaissent bien!",
        "question_prompt": "Pose-moi une question oui/non:",
        "you_ask": "Hmm, tu demandes: *{question}*",
        "button": "🔮 Consulter les esprits!",
        "spirits_say": "🔮 Les esprits disent: **{fortune}**",
        "credit": "✨ Œuvre expérimentale par Valen de Repton ✨",
        "fortunes": [
            "Oui, absolument!",
            "Pas du tout!",
            "Demande plus tard...",
            "Les étoiles disent OUI! ⭐",
            "Hmm, ça n'a pas l'air bon 😬",
            "Absolument!",
            "Réessaye demain",
            "C'est certain!"
        ]
    },
    "中文 🇨🇳": {
        "title": "🔮 神奇算命师 🔮",
        "intro": "我能看到你的未来...",
        "name_prompt": "勇敢的探索者,你叫什么名字?",
        "greeting": "你好,**{name}** — 神灵很了解你!",
        "question_prompt": "问我一个是/否的问题:",
        "you_ask": "嗯,你问: *{question}*",
        "button": "🔮 询问神灵!",
        "spirits_say": "🔮 神灵说: **{fortune}**",
        "credit": "✨ Valen (Repton) 的实验作品 ✨",
        "fortunes": [
            "是的,绝对是!",
            "没门!",
            "稍后再问...",
            "星星说是的! ⭐",
            "嗯,看起来不太好 😬",
            "绝对的!",
            "明天再试试",
            "这是肯定的!"
        ]
    },
    "العربية 🇸🇦": {
        "title": "🔮 العرّافة السحرية 🔮",
        "intro": "أستطيع أن أرى مستقبلك...",
        "name_prompt": "ما اسمك أيها الباحث الشجاع؟",
        "greeting": "مرحبًا، **{name}** — الأرواح تعرفك جيدًا!",
        "question_prompt": "اسألني سؤالًا بنعم أو لا:",
        "you_ask": "همم، أنت تسأل: *{question}*",
        "button": "🔮 استشر الأرواح!",
        "spirits_say": "🔮 الأرواح تقول: **{fortune}**",
        "credit": "✨ عمل تجريبي من إعداد فالين من ريبتون ✨",
        "fortunes": [
            "نعم، بالتأكيد!",
            "مستحيل!",
            "اسأل مرة أخرى لاحقًا...",
            "النجوم تقول نعم! ⭐",
            "همم، لا يبدو جيدًا 😬",
            "بالتأكيد!",
            "حاول مرة أخرى غدًا",
            "إنه أمر مؤكد!"
        ]
    }
}

# Language picker at the top
language = st.selectbox("🌍 Language / Langue / 语言 / اللغة", list(translations.keys()))

# Grab the right set of words for the chosen language
t = translations[language]

# Now build the page using t["..."] instead of hardcoded text
st.title(t["title"])
st.write(t["intro"])

name = st.text_input(t["name_prompt"])

if name:
    st.write(t["greeting"].format(name=name))

    question = st.text_input(t["question_prompt"])

    if question:
        st.write(t["you_ask"].format(question=question))
        if st.button(t["button"]):
            fortune = random.choice(t["fortunes"])
            st.success(t["spirits_say"].format(fortune=fortune))

st.caption(t["credit"])
