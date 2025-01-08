import streamlit as st
import random

# 챔피언 데이터 (예시)
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
    "쓰레쉬": {
        "role": "서포터",
        "description": "영혼을 가두는 유령 간수.",
        "region": "그림자 군도",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Thresh_0.jpg"
    },
    "가렌": {
        "role": "탱커",
        "description": "불굴의 결의를 가진 고귀한 전사.",
        "region": "데마시아",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Garen_0.jpg"
    },
    "리신": {
        "role": "전사",
        "description": "눈이 멀었지만, 내면의 시야로 싸우는 승려.",
        "region": "아이오니아",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/LeeSin_0.jpg"
    },
    "미스포츈": {
        "role": "원거리 딜러",
        "description": "뛰어난 사격 솜씨를 지닌 현상금 사냥꾼.",
        "region": "빌지워터",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/MissFortune_0.jpg"
    },
    "제드": {
        "role": "암살자",
        "description": "어둠의 힘을 다루는 무자비한 닌자.",
        "region": "아이오니아",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Zed_0.jpg"
    },
    "럭스": {
        "role": "마법사",
        "description": "빛의 힘으로 적을 물리치는 데마시아의 소녀.",
        "region": "데마시아",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Lux_0.jpg"
    },
    "에코": {
        "role": "암살자",
        "description": "시간을 조종하는 젊은 발명가.",
        "region": "자운",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ekko_0.jpg"
    },
    # 예시로 추가된 챔피언들에 대한 이미지 URL
    "드레이븐": {
        "role": "원거리 딜러",
        "description": "관중의 사랑을 받는 자만심 강한 도끼 투척사.",
        "region": "녹서스",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Draven_0.jpg"
    },
    "애쉬": {
        "role": "원거리 딜러",
        "description": "아바로사 부족의 얼음궁수 여왕.",
        "region": "프렐요드",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ashe_0.jpg"
    },
    # 추가 챔피언들...
    "요네": {
        "role": "전사",
        "description": "두 개의 검을 다루는 바람과 영혼의 전사.",
        "region": "아이오니아",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Yone_0.jpg"
    },
    "볼리베어": {
        "role": "탱커",
        "description": "천둥과 폭풍의 힘을 가진 거대한 곰.",
        "region": "프렐요드",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Volibear_0.jpg"
    },
    "갱플랭크": {
        "role": "전사",
        "description": "바다를 지배하는 잔혹한 해적 왕.",
        "region": "빌지워터",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Gangplank_0.jpg"
    },
    "자크": {
        "role": "탱커",
        "description": "자운의 실험에서 탄생한 탄력 있는 생물.",
        "region": "자운",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Zac_0.jpg"
    },
    "피들스틱": {
        "role": "마법사",
        "description": "공포를 수확하는 고대의 공포.",
        "region": "룬테라 전역",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Fiddlesticks_0.jpg"
    },
    "초가스": {
        "role": "탱커",
        "description": "끝없는 허기를 가진 공허의 괴수.",
        "region": "공허",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Chogath_0.jpg"
    },
    "노틸러스": {
        "role": "탱커",
        "description": "심해의 비밀을 지키는 거대한 잠수부.",
        "region": "빌지워터",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Nautilus_0.jpg"
    },
    "탈론": {
        "role": "암살자",
        "description": "어둠 속에서 치명적인 칼날을 휘두르는 암살자.",
        "region": "녹서스",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Talon_0.jpg"
    },
    "사일러스": {
        "role": "전사",
        "description": "마법의 족쇄를 풀고 복수를 다짐한 반역자.",
        "region": "데마시아",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Sylas_0.jpg"
    }
}

st.title("리그 오브 레전드 챔피언 소개")

# 사용자 입력을 받아 챔피언 정보 표시
champion_name = st.text_input("챔피언 이름을 입력하세요(ex 요네):")

if st.button("챔피언 정보 보기"):
    if champion_name in champions:
        champion_info = champions[champion_name]
        st.subheader(f"챔피언: {champion_name}")
        st.write(f"역할: {champion_info['role']}")
        st.write(f"설명: {champion_info['description']}")
        st.write(f"지역: {champion_info['region']}")
        st.image(champion_info['image'])
    else:
        st.write("입력하신 챔피언이 데이터에 없습니다. 다시 시도해주세요.")

st.write("리그 오브 레전드에 대한 더 많은 정보를 원하시면 [여기](https://www.leagueoflegends.com)를 방문하세요.")


