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
    },
    "리신": {
        "role": "전사",
        "description": "눈이 멀었지만, 내면의 시야로 싸우는 승려.",
        "region": "아이오니아"
    },
    "미스포츈": {
        "role": "원거리 딜러",
        "description": "뛰어난 사격 솜씨를 지닌 현상금 사냥꾼.",
        "region": "빌지워터"
    },
    "제드": {
        "role": "암살자",
        "description": "어둠의 힘을 다루는 무자비한 닌자.",
        "region": "아이오니아"
    },
    "럭스": {
        "role": "마법사",
        "description": "빛의 힘으로 적을 물리치는 데마시아의 소녀.",
        "region": "데마시아"
    },
    "에코": {
        "role": "암살자",
        "description": "시간을 조종하는 젊은 발명가.",
        "region": "자운"
    },
    # 추가된 챔피언들
    "드레이븐": {
        "role": "원거리 딜러",
        "description": "관중의 사랑을 받는 자만심 강한 도끼 투척사.",
        "region": "녹서스"
    },
    "애쉬": {
        "role": "원거리 딜러",
        "description": "아바로사 부족의 얼음궁수 여왕.",
        "region": "프렐요드"
    },
    "다리우스": {
        "role": "전사",
        "description": "녹서스의 위엄을 상징하는 강력한 장군.",
        "region": "녹서스"
    },
    "카타리나": {
        "role": "암살자",
        "description": "치명적인 칼날을 다루는 녹서스의 암살자.",
        "region": "녹서스"
    },
    "피오라": {
        "role": "전사",
        "description": "칼을 다루는 데 예술적 경지를 자랑하는 자존심 강한 결투사.",
        "region": "데마시아"
    },
    "쉔": {
        "role": "탱커",
        "description": "균형을 유지하기 위해 그림자 속에서 활동하는 아이오니아의 닌자.",
        "region": "아이오니아"
    },
    "베인": {
        "role": "원거리 딜러",
        "description": "어둠의 존재를 사냥하는 정의로운 복수자.",
        "region": "데마시아"
    },
    "오리아나": {
        "role": "마법사",
        "description": "춤추는 기계 소녀와 그녀의 마법 구체.",
        "region": "필트오버"
    },
    "리븐": {
        "role": "전사",
        "description": "녹서스를 떠난 전사로, 자신의 과거와 싸우고 있다.",
        "region": "아이오니아"
    },
    "티모": {
        "role": "원거리 딜러",
        "description": "요들 정찰병으로, 적을 함정으로 유인하는 데 능숙하다.",
        "region": "밴들 시티"
    }
}

st.title("리그 오브 레전드 챔피언 소개")

# 사용자 입력을 받아 챔피언 정보 표시
champion_name = st.text_input("챔피언 이름을 입력하세요:")

if st.button("챔피언 정보 보기"):
    if champion_name in champions:
        champion_info = champions[champion_name]
        st.subheader(f"챔피언: {champion_name}")
        st.write(f"역할: {champion_info['role']}")
        st.write(f"설명: {champion_info['description']}")
        st.write(f"지역: {champion_info['region']}")
    else:
        st.write("입력하신 챔피언이 데이터에 없습니다. 다시 시도해주세요.")

st.write("리그 오브 레전드에 대한 더 많은 정보를 원하시면 [여기](https://www.leagueoflegends.com)를 방문하세요.")


