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

# Instagram API 설정
access_token = '638bbd582151fbd4386ff7e66c2bc688'
user_id = '1505713830311872'

# Instagram 사용자 미디어 가져오기
def get_instagram_media(user_id, access_token):
    url = f'https://graph.instagram.com/{user_id}/media?fields=id,caption,media_type,media_url,permalink&access_token={access_token}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get('data')
    else:
        st.error('Instagram API 요청 실패')
        return []

# 스트림릿 앱
st.title("Instagram 피드 및 릴스 보기")

media_data = get_instagram_media(user_id, access_token)

if media_data:
    for media in media_data:
        st.write(f"Caption: {media.get('caption')}")
        if media['media_type'] == 'IMAGE':
            st.image(media['media_url'], use_column_width=True)
        elif media['media_type'] == 'VIDEO':
            st.video(media['media_url'])
        st.write(f"[View on Instagram]({media.get('permalink')})")
else:
    st.write("Instagram에서 가져올 미디어가 없습니다.")

