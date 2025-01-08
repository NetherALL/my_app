import streamlit as st
import random

# 챔피언 데이터 (예시)
champions = {
    "Ahri": {
        "role": "Mage",
        "description": "A charming fox with a knack for magic.",
        "region": "Ionia"
    },
    "Yasuo": {
        "role": "Fighter",
        "description": "A swift swordsman with wind power.",
        "region": "Ionia"
    },
    "Jinx": {
        "role": "Marksman",
        "description": "A crazed criminal with a love for chaos.",
        "region": "Zaun"
    },
    "Thresh": {
        "role": "Support",
        "description": "A spectral warden who traps souls.",
        "region": "Shadow Isles"
    },
    "Garen": {
        "role": "Tank",
        "description": "A noble warrior with unbreakable resolve.",
        "region": "Demacia"
    }
}

st.title("리그 오브 레전드 챔피언 랜덤 소개")

# 버튼을 클릭할 때마다 랜덤 챔피언 선택
if st.button("챔피언 소개하기"):
    champion_name = random.choice(list(champions.keys()))
    champion_info = champions[champion_name]
    
    st.subheader(f"챔피언: {champion_name}")
    st.write(f"역할: {champion_info['role']}")
    st.write(f"설명: {champion_info['description']}")
    st.write(f"지역: {champion_info['region']}")

st.write("리그 오브 레전드에 대한 더 많은 정보를 원하시면 [여기](https://www.leagueoflegends.com)를 방문하세요.")
