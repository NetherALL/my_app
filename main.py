import streamlit as st

# 챔피언 데이터
champions = {
    "아리": {
        "role": "마법사",
        "description": "마법에 능숙한 매혹적인 여우.",
        "region": "아이오니아",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ahri_0.jpg"
    },
    "야스오": {
        "role": "전사",
        "description": "바람의 힘을 사용하는 빠른 검객.",
        "region": "아이오니아",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Yasuo_0.jpg"
    },
    "징크스": {
        "role": "원거리 딜러",
        "description": "혼돈을 사랑하는 미친 범죄자.",
        "region": "자운",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Jinx_0.jpg"
    },
    # ... (다른 챔피언들 추가)
    "사일러스": {
        "role": "전사",
        "description": "마법의 족쇄를 풀고 복수를 다짐한 반역자.",
        "region": "데마시아",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Sylas_0.jpg"
    }
}

# Streamlit 애플리케이션
st.title("리그 오브 레전드 챔피언 정보")

# 사용자 입력
champion_name = st.text_input("챔피언 이름을 입력하세요:")

if st.button("챔피언 정보 보기"):
    if champion_name in champions:
        champion_info = champions[champion_name]
        
        st.subheader(f"챔피언: {champion_name}")
        st.write(f"역할: {champion_info['role']}")
        st.write(f"설명: {champion_info['description']}")
        st.write(f"지역: {champion_info['region']}")
        st.image(champion_info['image'], caption=f"{champion_name}의 이미지", use_column_width=True)
    else:
        st.error("입력하신 챔피언이 데이터에 없습니다. 다시 시도해주세요.")
