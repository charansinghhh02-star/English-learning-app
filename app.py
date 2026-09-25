import streamlit as st
import json
import os

# --- PAGE SETUP ---
st.set_page_config(page_title="English Mastery Suite", page_icon="🇬🇧", layout="centered")

# Custom UI Styling
st.markdown("""
    <style>
    .main-header { font-size: 2.3rem; color: #1e3a8a; font-weight: bold; text-align: center; margin-bottom: 5px; }
    .sub-header { font-size: 1.05rem; color: #4b5563; text-align: center; margin-bottom: 5px; }
    .creator-tag { font-size: 0.95rem; color: #2563eb; font-weight: 600; text-align: center; margin-bottom: 25px; font-style: italic; }
    .topic-card { background-color: #f0fdf4; border-left: 5px solid #16a34a; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
    .metric-box { background-color: #f8fafc; border: 1px solid #e2e8f0; padding: 15px; border-radius: 8px; text-align: center; font-weight: bold; }
    .result-box { background-color: #eff6ff; border: 2px dashed #2563eb; padding: 30px; border-radius: 12px; text-align: center; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- 1. DYNAMIC 365-DAY CURRICULUM DATA ---
MODULES = [
    {"title": "Advanced Syntax & Grammar", "concept": "Focusing on sentence structures, relative clauses, inversion techniques, and perfect aspect shifts.", "track": "Grammar"},
    {"title": "Idiomatic Fluency & Nuance", "concept": "Decoding daily expressions, native phrasal verbs, and subtle conversational context.", "track": "Idioms"},
    {"title": "Executive Business English", "concept": "Corporate vocabulary protocols, formal negotiation phrasing, and professional presentation framing.", "track": "Business"},
    {"title": "Vocabulary Architecture", "concept": "Acquiring precise academic adjectives, high-level vocabulary, and root words to elevate your speech.", "track": "Vocab"},
    {"title": "Stylistic & Professional Writing", "concept": "Achieving text flow, eliminating redundant phrasing, using active voice, and linking concepts.", "track": "Writing"}
]

def get_day_info(day):
    mod = MODULES[(day - 1) % len(MODULES)]
    if day <= 60: phase = "🌱 Phase 1: Core Foundations Expansion"
    elif day <= 180: phase = "🚀 Phase 2: Intermediate Acceleration Hub"
    elif day <= 300: phase = "⚡ Phase 3: Advanced Command & Nuance"
    else: phase = "🏆 Phase 4: Complete Professional Fluency"
    
    return {
        "title": f"Day {day}: {mod['title']}",
        "phase": phase,
        "concept": f"**[Learning Track: {mod['title']}]**\n\n{mod['concept']} Focus deeply on mastering this track today.",
        "track": mod["track"]
    }

# --- 2. UNIQUE 100-QUESTION TEST GENERATOR PER DAY ---
def generate_mock_questions(day_num, track):
    questions = []
    
    vocab_pool = ["eloquent", "meticulous", "ephemeral", "resilient", "pragmatic", "gregarious", "tenacious", "scrutinize", "corroborate", "lucrative"]
    business_pool = ["leverage resources", "optimize workflow", "synergize milestones", "mitigate liabilities", "streamline assets", "expedite deliverables"]
    idiom_pool = ["read between the lines", "hit the nail on the head", "burn the midnight oil", "bite the bullet", "break the ice"]

    for i in range(1, 101):
        v_word = vocab_pool[(day_num + i) % len(vocab_pool)]
        b_phrase = business_pool[(day_num + i) % len(business_pool)]
        i_phrase = idiom_pool[(day_num + i) % len(idiom_pool)]
        
        if track == "Grammar":
            if i % 2 == 1:
                questions.append({
                    "id": i,
                    "q": f"Question {i} (Grammar Test): Identify the correct option: 'Seldom ______ such an outstanding performance from a new applicant.'",
                    "options": ["have I witnessed", "I have witnessed", "witnessed I", "had I witness"],
                    "correct": "have I witnessed"
                })
            else:
                questions.append({
                    "id": i,
                    "q": f"Question {i} (Grammar Test): Fill the structural blank: 'If he had arrived earlier for Day {day_num}, he ______ the intro.'",
                    "options": ["would have caught", "will catch", "would catch", "caught"],
                    "correct": "would have caught"
                })
                
        elif track == "Idioms":
            questions.append({
                "id": i,
                "q": f"Question {i} (Idioms Test): What is the logical contextual meaning of the expression '{i_phrase}'?",
                "options": ["To act accurately or understand perfectly", "To ignore clear reality parameters", "To completely delay assignments", "To modify existing rules"],
                "correct": "To act accurately or understand perfectly"
            })
            
        elif track == "Business":
            questions.append({
                "id": i,
                "q": f"Question {i} (Business Test): Select the most formal corporate phrasing to replace basic sentences: 'We need to ______.'",
                "options": [f"{b_phrase} effectively", "do things faster", "get extra stuff", "fix up the problems"],
                "correct": f"{b_phrase} effectively"
            })
            
        elif track == "Vocab":
            questions.append({
                "id": i,
                "q": f"Question {i} (Vocabulary Test): Choose the best option that matches the definition of the word '**{v_word}**':",
                "options": ["Showing careful accuracy and precision", "Extremely quick or instant", "Highly aggressive or disruptive", "Lacking form or value"],
                "correct": "Showing careful accuracy and precision"
            })
            
        else:
            questions.append({
                "id": i,
                "q": f"Question {i} (Writing Test): How can you rewrite a sentence to maximize active voice and clarity?",
                "options": ["Make the subject perform the action directly", "Add words like 'due to the fact that'", "Use passive helping verbs extensively", "Leave out structural transition markers"],
                "correct": "Make the subject perform the action directly"
            })
            
    return questions

# --- 3. PERSISTENT PROGRESS STORAGE MANAGEMENT ---
PROGRESS_FILE = "user_progress_365.json"

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_progress(progress):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f)

global_progress = load_progress()

# --- APP LAYOUT HEADER ---
st.markdown("<div class='main-header'>Fluentify Masterclass Suite</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>365-Day Logical Mastery Path & Dynamic Daily Test System</div>", unsafe_allow_html=True)
st.markdown("<div class='creator-tag'>Created by Charan Singh</div>", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["📖 Daily 365 Tutorial Hub", "📝 Unique 100-Question Test"])

# --- GENERAL NAVIGATION STATE ---
target_day = st.number_input("Select Target Learning Day (1 to 365):", min_value=1, max_value=365, value=1, key="global_day_select")
day_info = get_day_info(target_day)

day_key = str(target_day)
if day_key not in global_progress:
    global_progress[day_key] = {"answers": {}, "current_q": 1}

day_data = global_progress[day_key]
current_q_idx = day_data["current_q"]

if f"answered_day_{day_key}" not in st.session_state:
    st.session_state[f"answered_day_{day_key}"] = False

current_mock_questions = generate_mock_questions(target_day, day_info["track"])

# --- TAB 1: DAILY 365 TUTORIAL HUB ---
with tab1:
    st.subheader("📚 Conceptual Curriculum Path")
    st.caption(f"📍 Current Milestone: {day_info['phase']}")
    
    st.markdown(f"""
        <div class='topic-card'>
            <h4>{day_info['title']}</h4>
            <p style='margin-top: 10px;'>{day_info['concept']}</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.info(f"✨ **Day {target_day} Practical Application Rule:** Keep this logic in mind when taking today's unique mock test.")

# --- TAB 2: UNIQUE 100-QUESTION TEST ARENA ---
with tab2:
    st.subheader(f"🏆 Day {target_day} Dedicated Mock Exam Studio")
    
    # CASE A: Exam is active (Sequential queue 1 to 100)
    if current_q_idx <= 100:
        st.markdown(f"<div class='metric-box'>Day {target_day} Progress Tracker<br><span style='color:#2563eb; font-size:1.5rem;'>{current_q_idx - 1} / 100</span> Questions Answered</div>", unsafe_allow_html=True)
        st.write("")
        st.progress((current_q_idx - 1) / 100)
        st.write("---")
        
        q_item = current_mock_questions[current_q_idx - 1]
        st.markdown(f"#### **{q_item['q']}**")
        
        saved_ans = day_data["answers"].get(str(current_q_idx), None)
        is_disabled = st.session_state[f"answered_day_{day_key}"] or (saved_ans is not None)
        default_idx = q_item["options"].index(saved_ans) if saved_ans in q_item["options"] else None
        
        choice = st.radio(
            "Select the correct answer option:", 
            q_item["options"], 
            index=default_idx, 
            key=f"q_{target_day}_{current_q_idx}",
            disabled=is_disabled
        )
        
        st.write("")
        
        # Action Step 1: Check Answer Button
        if not is_disabled:
            if st.button("🔬 Check Answer", use_container_width=True, key=f"btn_check_{target_day}_{current_q_idx}"):
                if choice is not None:
                    day_data["answers"][str(current_q_idx)] = choice
                    st.session_state[f"answered_day_{day_key}"] = True
                    save_progress(global_progress)
                    st.rerun()
                else:
                    st.warning("⚠️ Please select an answer option first.")
                    
        # Action Step 2: Show immediate feedback banners and next page triggers
        # Action Step 2: Show immediate feedback banners and next page triggers
        if is_disabled:
            final_choice = choice if choice is not None else saved_ans
            if final_choice == q_item["correct"]:
                st.success("🎯 Correct! Flawless sentence structure choice.")
            else:
                st.error(f"❌ Incorrect. The ideal choice is: **{q_item['correct']}**")
                
            st.write("")
            if st.button("Next Question ➡️", use_container_width=True, key=f"btn_next_{target_day}_{current_q_idx}"):
                day_data["current_q"] += 1
                st.session_state[f"answered_day_{day_key}"] = False
                save_progress(global_progress)
                st.rerun()
