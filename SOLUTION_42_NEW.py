import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import time
import random

st.set_page_config(
    page_title="🧠 SOLUTION 42",
    page_icon="42",
    layout="wide"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0a0f0f 0%, #1a1f2a 100%);
    }
    .answer-42 {
        font-size: 120px;
        font-weight: 900;
        color: #00ff00;
        text-align: center;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.8; }
        100% { opacity: 1; }
    }
    .big-42 {
        font-size: 60px;
        color: #0f0;
        text-align: center;
    }
    .stButton button {
        background: linear-gradient(90deg, #00ff00, #00ffff);
        color: black;
        font-size: 24px;
        font-weight: bold;
        border-radius: 50px;
    }
</style>
""", unsafe_allow_html=True)

# ======================================================================
# TITLE SECTION
# ======================================================================

st.markdown("""
<div style='text-align: center; padding: 20px;'>
    <h1 style='color: #00ff00; font-size: 80px;'>🧠 SOLUTION 42</h1>
    <h2 style='color: #00ffff;'>The Answer to Life, the Universe, and Everything</h2>
    <div class='answer-42'>42</div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ======================================================================
# STEP 1: YOUR QUESTION
# ======================================================================

st.markdown("<h3 style='color: #0f0;'>❓ WHAT IS YOUR QUESTION?</h3>", unsafe_allow_html=True)

question = st.text_input(
    " ", 
    placeholder="e.g., What is my purpose? Will I be successful? Does she love me?",
    label_visibility="collapsed"
)

st.markdown("---")

# ======================================================================
# STEP 2: YOUR DETAILS - BIRTH YEAR 2020 READY!
# ======================================================================

st.markdown("<h3 style='color: #0f0;'>🧬 WHO ARE YOU?</h3>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    name = st.text_input("Your Name", placeholder="Enter your name", value="")
    
    # ===== 🔥 BIRTH DATE - 2020 TAK READY! =====
    birth_date = st.date_input(
        "Your Birth Date",
        datetime(2010, 1, 1),  # Default 2010 - you can change to 2020, 2007, anything!
        min_value=datetime(1900, 1, 1),
        max_value=datetime.now(),
        help="When did you arrive in this universe?"
    )
    
    # Age Calculator
    today = datetime.now()
    age = today.year - birth_date.year
    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1
    
    st.success(f"🎂 **Age: {age} years** • Born in **{birth_date.year}**")

with col2:
    favorite_number = st.number_input(
        "Favorite Number", 
        min_value=1, 
        max_value=1000, 
        value=42,
        help="42 is always correct!"
    )
    
    life_rating = st.slider(
        "Life Rating (0-100)", 
        0, 100, 50,
        help="How's life treating you?"
    )

with col3:
    universe_type = st.selectbox(
        "The Universe Is...",
        ["🌌 Infinite", "🌀 Cyclical", "🎲 Random", "🧠 Simulated", "⚛️ Quantum", "🎭 Mysterious"]
    )
    
    towel_ready = st.checkbox(
        "🧻 I know where my towel is", 
        value=True,
        help="Any true hitchhiker always knows!"
    )

st.markdown("---")

# ======================================================================
# STEP 3: THE ANSWER BUTTON
# ======================================================================

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    find_button = st.button("🔮 FIND THE ANSWER", use_container_width=True)

if find_button:
    
    # ==================================================================
    # COMPUTING ANIMATION
    # ==================================================================
    
    with st.spinner("🧠 Deep Thought is computing..."):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        computing_messages = [
            "Accessing universal database...",
            "Calculating probability matrix...",
            "Consulting the Guide...",
            "Measuring quantum fluctuations...",
            "Decoding 42 billion possibilities...",
            f"Analyzing {name if name else 'your'} destiny...",
            "Warming up Infinite Improbability Drive...",
            "7.5 million years remaining...",
            "Almost there..."
        ]
        
        for i in range(101):
            if i % 12 == 0:
                status_text.info(random.choice(computing_messages))
            progress_bar.progress(i)
            time.sleep(0.02)
        
        progress_bar.empty()
        status_text.empty()
    
    # ==================================================================
    # THE ANSWER - 42!
    # ==================================================================
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; padding: 40px; background: linear-gradient(45deg, #0a2a2a, #1a3a3a); border-radius: 20px;'>
        <h2 style='color: #fff;'>✨ THE ANSWER TO YOUR QUESTION IS... ✨</h2>
        <div style='font-size: 150px; font-weight: 900; color: #0f0; text-shadow: 0 0 50px #0f0;'>42</div>
        <p style='color: #afa; font-size: 20px;'>"I checked it very thoroughly," said the computer, "and that quite definitely is the answer."</p>
    </div>
    """, unsafe_allow_html=True)
    
    # ==================================================================
    # YOUR PERSONAL 42
    # ==================================================================
    
    st.markdown("---")
    st.markdown("<h2 style='color: #0f0; text-align: center;'>🎯 YOUR PERSONAL 42</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Personality Type
        personality_types = [
            ("🌟 The Philosopher", "You question everything, even the question itself."),
            ("🚀 The Adventurer", "You don't wait for answers, you find them."),
            ("🔬 The Scientist", "You need proof, even when proof is impossible."),
            ("🎨 The Artist", "You feel the answer before you know it."),
            ("🧙 The Mystic", "You knew the answer before you asked."),
            ("⚙️ The Engineer", "You want to build the answer."),
            ("💫 The Dreamer", "Your imagination creates reality."),
            ("🔮 The Seeker", "The journey is the destination.")
        ]
        
        personality = random.choice(personality_types)
        st.markdown(f"""
        <div style='background: rgba(0,255,0,0.1); padding: 25px; border-radius: 15px; border-left: 5px solid #0f0; height: 200px;'>
            <h3 style='color: #0ff;'>{personality[0]}</h3>
            <p style='color: #fff; font-size: 18px; margin-top: 20px;'>{personality[1]}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Personal 42 Message
        birth_year = birth_date.year
        future_42 = birth_year + 42
        
        messages = [
            f"✨ **42%** of your life journey is already written.",
            f"📅 You were born in **{birth_year}**. When you turn **42** in **{future_42}**, the universe will reveal more.",
            f"🌍 You've been on Earth for **{age * 365} days**. That's **{age * 365 * 24} hours** of cosmic experience!",
            f"🎯 Your destiny number is **{sum([ord(c) for c in name if c != ' ']) % 42 if name else 42}**.",
            f"💫 The universe has **42 billion galaxies**, and you are unique in all of them.",
            f"🧠 Deep Thought computed that your question has a **{random.randint(42, 99)}%** probability of positive outcome."
        ]
        
        st.markdown(f"""
        <div style='background: rgba(0,255,255,0.1); padding: 25px; border-radius: 15px; border-left: 5px solid #0ff; height: 200px;'>
            <h3 style='color: #0ff;'>🔮 YOUR 42</h3>
            <p style='color: #fff; font-size: 18px; margin-top: 20px;'>{random.choice(messages)}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # ==================================================================
    # DESTINY & CAREER
    # ==================================================================
    
    st.markdown("---")
    st.markdown("<h2 style='color: #0f0; text-align: center;'>🗺️ YOUR DESTINY</h2>", unsafe_allow_html=True)
    
    careers = [
        "🚀 **Astronaut** - You belong among the stars!",
        "🧠 **Scientist** - You will discover something amazing!",
        "🎬 **Artist** - Your creativity will inspire millions!",
        "💻 **Engineer** - You will build the future!",
        "📚 **Teacher** - You will shape young minds!",
        "🏥 **Doctor** - You will save lives!",
        "⚖️ **Lawyer** - You will fight for justice!",
        "🌍 **Explorer** - You will see places no one has seen!",
        "🎮 **Game Developer** - You will create worlds!",
        "🤖 **AI Researcher** - You will create intelligence!"
    ]
    
    destiny_number = sum([ord(c) for c in name]) % 42 if name else 42
    confidence = random.randint(42, 99)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div style='background: rgba(255,255,255,0.05); padding: 20px; border-radius: 10px; text-align: center;'>
            <h3 style='color: #0ff;'>💼 CAREER</h3>
            <p style='color: #fff; font-size: 18px;'>{random.choice(careers)}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style='background: rgba(255,255,255,0.05); padding: 20px; border-radius: 10px; text-align: center;'>
            <h3 style='color: #0ff;'>🔢 DESTINY NUMBER</h3>
            <p style='color: #0f0; font-size: 50px; font-weight: bold;'>{destiny_number}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style='background: rgba(255,255,255,0.05); padding: 20px; border-radius: 10px; text-align: center;'>
            <h3 style='color: #0ff;'>📊 CONFIDENCE</h3>
            <p style='color: #0f0; font-size: 50px; font-weight: bold;'>{confidence}%</p>
        </div>
        """, unsafe_allow_html=True)
    
    # ==================================================================
    # LIFE MILESTONES TIMELINE
    # ==================================================================
    
    st.markdown("---")
    st.markdown("<h3 style='color: #0f0;'>⏳ YOUR LIFE MILESTONES</h3>", unsafe_allow_html=True)
    
    milestones = []
    current_year = datetime.now().year
    
    for i in range(1, 6):
        milestone_year = birth_year + (i * 10)
        if milestone_year < current_year:
            milestone_year = current_year + (i * 2)
        
        milestones.append({
            "Age": milestone_year - birth_year,
            "Year": milestone_year,
            "Event": random.choice([
                "Major discovery 🏆",
                "Life-changing meeting 💖",
                "Career breakthrough 💼",
                "Adventure begins 🚀",
                "Wisdom gained 🧠",
                "Dream comes true ✨",
                "New beginning 🌅",
                "Challenge overcome 💪"
            ])
        })
    
    milestones_df = pd.DataFrame(milestones)
    st.dataframe(milestones_df, use_container_width=True, hide_index=True)
    
    # ==================================================================
    # QUANTUM PROBABILITY MATRIX
    # ==================================================================
    
    st.markdown("---")
    st.markdown("<h3 style='color: #0f0;'>⚛️ QUANTUM PROBABILITY MATRIX</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        love_prob = random.uniform(42, 99)
        st.metric("❤️ Love", f"{love_prob:.1f}%", f"{love_prob-50:+.1f}%")
    
    with col2:
        career_prob = random.uniform(42, 99)
        st.metric("💼 Career", f"{career_prob:.1f}%", f"{career_prob-50:+.1f}%")
    
    with col3:
        happiness_prob = random.uniform(42, 99)
        st.metric("😊 Happiness", f"{happiness_prob:.1f}%", f"{happiness_prob-50:+.1f}%")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        wealth_prob = random.uniform(42, 99)
        st.metric("💰 Wealth", f"{wealth_prob:.1f}%", f"{wealth_prob-50:+.1f}%")
    
    with col2:
        health_prob = random.uniform(42, 99)
        st.metric("🏥 Health", f"{health_prob:.1f}%", f"{health_prob-50:+.1f}%")
    
    with col3:
        meaning_prob = 42.0  # Always 42%
        st.metric("🎯 Meaning", f"{meaning_prob:.1f}%", "0.0%")
    
    # ==================================================================
    # TOWEL DAY COUNTDOWN
    # ==================================================================
    
    st.markdown("---")
    
    today = datetime.now()
    towel_day = datetime(today.year, 5, 25)
    
    if today > towel_day:
        towel_day = datetime(today.year + 1, 5, 25)
    
    days_to_towel = (towel_day - today).days
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("""
        <div style='text-align: center;'>
            <h1 style='font-size: 100px; margin: 0;'>🧻</h1>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style='background: rgba(0,255,0,0.1); padding: 20px; border-radius: 15px;'>
            <h3 style='color: #0f0;'>TOWEL DAY COUNTDOWN</h3>
            <h1 style='color: #0ff; font-size: 48px;'>{days_to_towel} DAYS</h1>
            <p style='color: #afa;'>May 25th - Always know where your towel is!</p>
            <p style='color: #6f6; font-style: italic;'>"Don't Panic!"</p>
        </div>
        """, unsafe_allow_html=True)

else:
    # ==================================================================
    # HITCHHIKER'S GUIDE - WELCOME SCREEN
    # ==================================================================
    
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style='background: rgba(0,255,0,0.05); padding: 30px; border-radius: 15px; text-align: center;'>
            <h1 style='font-size: 60px;'>🧠</h1>
            <h3 style='color: #0f0;'>DEEP THOUGHT</h3>
            <p style='color: #afa;'>The second greatest computer of all time. Took 7.5 million years to compute the answer: 42.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: rgba(0,255,0,0.05); padding: 30px; border-radius: 15px; text-align: center;'>
            <h1 style='font-size: 60px;'>🧻</h1>
            <h3 style='color: #0f0;'>TOWEL</h3>
            <p style='color: #afa;'>The most massively useful thing an interstellar hitchhiker can have.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style='background: rgba(0,255,0,0.05); padding: 30px; border-radius: 15px; text-align: center;'>
            <h1 style='font-size: 60px;'>🐠</h1>
            <h3 style='color: #0f0;'>BABEL FISH</h3>
            <p style='color: #afa;'>Stick it in your ear - instantly understand any language.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 42 Facts Carousel
    st.markdown("<h3 style='color: #0f0; text-align: center;'>🔢 42 INTERESTING FACTS</h3>", unsafe_allow_html=True)
    
    facts = [
        "Douglas Adams chose 42 because it was 'an ordinary, small number'.",
        "In binary, 42 is 101010 - beautifully symmetrical!",
        "The angle of a rainbow is 42 degrees.",
        "42 is the atomic number of molybdenum.",
        "There are 42 laws of Ma'at in Egyptian mythology.",
        "Lewis Carroll's 'Rule 42' in Alice in Wonderland.",
        "42 is the number of chromosomes in a human embryo.",
        "The 42nd parallel north is the border of New York.",
        "42 is the answer to the meaning of life in Hitchhiker's Guide.",
        "Your birth year {birth_date.year} + 42 = {birth_date.year + 42}!"
    ]
    
    for i in range(4):
        st.info(f"**42 >** {random.choice(facts)}")

# ======================================================================
# FOOTER
# ======================================================================

st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 40px; background: rgba(0,0,0,0.3); border-radius: 20px;'>
    <h1 style='color: #0f0; font-size: 48px;'>42</h1>
    <p style='color: #afa; font-size: 18px;'>
        "There is a theory which states that if ever anyone discovers exactly what the Universe is for and why it is here, 
        it will instantly disappear and be replaced by something even more bizarre and inexplicable. 
        There is another theory which states that this has already happened."
    </p>
    <p style='color: #0f0; margin-top: 20px;'>— Douglas Adams, The Hitchhiker's Guide to the Galaxy</p>
    <p style='color: #666; margin-top: 40px; font-size: 12px;'>
        🧠 SOLUTION 42 v2.0 • Powered by Deep Thought • 7.5 Million Years in the Making<br>
        "So Long, and Thanks for All the Fish!" 🐬
    </p>
</div>
""", unsafe_allow_html=True)