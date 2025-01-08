import streamlit as st
import random

# 챔피언 데이터 (예시)
champions = {
    "아리": {
        "role": "마법사",
        "description": "마법에 능숙한 매혹적인 여우.",
        "region": "아이오니아"
    },
    "야스오": {
        "role": "전사",
        "description": "바람의 힘을 사용하는 빠른 검객.",
        "region": "아이오니아"
    },
    "징크스": {
        "role": "원거리 딜러",
        "description": "혼돈을 사랑하는 미친 범죄자.",
        "region": "자운"
    },
    "쓰레쉬": {
        "role": "서포터",
        "description": "영혼을 가두는 유령 간수.",
        "region": "그림자 군도"
    },
    "가렌": {
        "role": "탱커",
        "description": "불굴의 결의를 가진 고귀한 전사.",
        "region": "데마시아"
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
