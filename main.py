import streamlit as st
import random
st.title("나의 첫번째 앱")
st.text('\n\n')
st.write('안녕하세요 . 😒 집가고싶네요.')
st.write('저의 이메일 주소는 24_11111@daejin.sen.hs.kr입니다')
st.write('대진고등학교 학생이죠')
st.button("Reset", type="primary")
if st.button("난수생성"):
    st.write(random.randint(0,10000000000000000))
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
