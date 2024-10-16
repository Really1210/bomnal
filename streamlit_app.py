import streamlit as st

st.title("🎈 봄날의꽃 BOMNANL Flower")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# 이미지 URL을 변수로 저장
image_url = 'https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240613_190%2F1718262533822XFxk4_JPEG%2FKakaoTalk_20240613_160008244.jpg'
image_url_1 = 'https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20231103_194%2F1699008075917YRUge_JPEG%2FIMG_7909.jpeg'
# st.image()에 이미지 URL 전달 및 캡션 추가
st.image(image_url, caption='봄날의꽃', use_column_width=True)
st.image(image_url_1, caption='봄날의꽃', use_column_width=True)

