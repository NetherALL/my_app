import streamlit as st

import base64

# 로컬 이미지 파일을 읽고 Base64로 인코딩하는 함수
def get_base64_image(file_path):
    with open(file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

# 이미지 파일 경로
image_file_path = "background.webp"  # 로컬 이미지 파일 경로

# Base64로 인코딩된 이미지 가져오기
encoded_image = get_base64_image(image_file_path)

# HTML과 CSS를 사용하여 배경 설정
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{encoded_image}");
        background-size: cover;
        color : yellow;
    }}
    </style>
    """,
    unsafe_allow_html=True
)




# 챔피언 데이터
champions = {
    "아리": {
        "role": "마법사",
        "description": "마법에 능숙한 매혹적인 여우.",
        "region": "아이오니아",
        
    },
    "야스오": {
        "role": "전사",
        "description": "바람의 힘을 사용하는 빠른 검객.",
        "region": "아이오니아",
        
    },
    "징크스": {
        "role": "원거리 딜러",
        "description": "혼돈을 사랑하는 미친 범죄자.",
        "region": "자운",
        
    },
    "쓰레쉬": {
        "role": "서포터",
        "description": "영혼을 가두는 유령 간수.",
        "region": "그림자 군도",
       
    },
    "가렌": {
        "role": "탱커",
        "description": "불굴의 결의를 가진 고귀한 전사.",
        "region": "데마시아",
        
    },
    "리신": {
        "role": "전사",
        "description": "눈이 멀었지만, 내면의 시야로 싸우는 승려.",
        "region": "아이오니아",
        
    },
    "미스포츈": {
        "role": "원거리 딜러",
        "description": "뛰어난 사격 솜씨를 지닌 현상금 사냥꾼.",
        "region": "빌지워터",
       
    },
    "제드": {
        "role": "암살자",
        "description": "어둠의 힘을 다루는 무자비한 닌자.",
        "region": "아이오니아",
       
    },
    "럭스": {
        "role": "마법사",
        "description": "빛의 힘으로 적을 물리치는 데마시아의 소녀.",
        "region": "데마시아",
  
    },
    "에코": {
        "role": "암살자",
        "description": "시간을 조종하는 젊은 발명가.",
        "region": "자운",
       
    },
    # 예시로 추가된 챔피언들에 대한 이미지 URL
    "드레이븐": {
        "role": "원거리 딜러",
        "description": "관중의 사랑을 받는 자만심 강한 도끼 투척사.",
        "region": "녹서스",
        
    },
    "애쉬": {
        "role": "원거리 딜러",
        "description": "아바로사 부족의 얼음궁수 여왕.",
        "region": "프렐요드",
       
    },
    # 추가 챔피언들...
    "요네": {
        "role": "전사",
        "description": "두 개의 검을 다루는 바람과 영혼의 전사.",
        "region": "아이오니아",
       
    },
    "볼리베어": {
        "role": "탱커",
        "description": "천둥과 폭풍의 힘을 가진 거대한 곰.",
        "region": "프렐요드",
        
    },
    "갱플랭크": {
        "role": "전사",
        "description": "바다를 지배하는 잔혹한 해적 왕.",
        "region": "빌지워터",
       
    },
    "자크": {
        "role": "탱커",
        "description": "자운의 실험에서 탄생한 탄력 있는 생물.",
        "region": "자운",
        
    },
    "피들스틱": {
        "role": "마법사",
        "description": "공포를 수확하는 고대의 공포.",
        "region": "룬테라 전역",
      
    },
    "초가스": {
        "role": "탱커",
        "description": "끝없는 허기를 가진 공허의 괴수.",
        "region": "공허",
       
    },
    "노틸러스": {
        "role": "탱커",
        "description": "심해의 비밀을 지키는 거대한 잠수부.",
        "region": "빌지워터",
        
    },
    "탈론": {
        "role": "암살자",
        "description": "어둠 속에서 치명적인 칼날을 휘두르는 암살자.",
        "region": "녹서스",
       
    },
    "사일러스": {
        "role": "전사",
        "description": "마법의 족쇄를 풀고 복수를 다짐한 반역자.",
        "region": "데마시아",
        
    },
    "그웬": {
        "role": "전사",
        "description": "생명의 실과 마법 가위를 사용하는 인형사.",
        "region": "그림자 군도",
        "image": "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Gwen_0.jpg"
    }
}


# Streamlit 애플리케이션
st.title("리그 오브 레전드 챔피언 정보")
st.image("league of legends.jpg")

# 사용자 입력
champion_name = st.text_input("")

if st.button("챔피언 정보 보기"):
    if champion_name in champions:
        champion_info = champions[champion_name]
        
        st.subheader(f"챔피언: {champion_name}")
        st.write(f"역할: {champion_info['role']}")
        st.write(f"설명: {champion_info['description']}")
        st.write(f"지역: {champion_info['region']}")
       
    else:
        st.error("입력하신 챔피언이 데이터에 없습니다. 다시 시도해주세요.")
