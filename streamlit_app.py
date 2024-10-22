import streamlit as st
import requests

# 스트림릿 타이틀
st.title("🎈 봄날의꽃 BOMNAL Flower")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# 이미지 URL을 변수로 저장
image_url = 'https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240613_190%2F1718262533822XFxk4_JPEG%2FKakaoTalk_20240613_160008244.jpg'
image_url_1 = 'https://search.pstatic.net/common/?src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20231103_194%2F1699008075917YRUge_JPEG%2FIMG_7909.jpeg'

# st.image()에 이미지 URL 전달 및 캡션 추가
st.image(image_url, caption='봄날의꽃', use_column_width=True)
st.image(image_url_1, caption='봄날의꽃', use_column_width=True)

# Instagram oEmbed API를 사용하여 게시물 정보 가져오기
def get_instagram_post(embed_url, access_token):
    # oEmbed API에 대한 요청 URL 구성
    api_url = f"https://graph.facebook.com/v12.0/instagram_oembed?url={embed_url}&access_token={access_token}&omitscript=true"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # 상태 코드가 200이 아니면 예외를 발생시킴
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP 오류 발생: {http_err}")
        return None
    except requests.exceptions.RequestException as e:
        st.error(f"요청 중 오류가 발생했습니다: {e}")
        return None

# 스트림릿 앱 설정
st.title("Instagram 게시물 보기")

# Instagram Access Token과 User ID
access_token = "638bbd582151fbd4386ff7e66c2bc688"  # Instagram에서 발급받은 Access Token
embed_url = "https://www.instagram.com/bomnal.flower/"  # 고정된 Instagram 게시물 URL

# 게시물 가져오기
post_data = get_instagram_post(embed_url, access_token)

if post_data:
    st.subheader("게시물 미리보기")
    st.write(f"Caption: {post_data.get('title')}")
    st.image(post_data.get('thumbnail_url'), use_column_width=True)
    st.write(f"[Instagram에서 보기]({post_data.get('author_url')})")
else:
    st.write("게시물을 가져올 수 없습니다.")
