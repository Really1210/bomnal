import streamlit as st
import requests

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


# Instagram oEmbed API를 사용하여 게시물 정보 가져오기
def get_instagram_post(embed_url):
    # oEmbed API에 대한 요청 URL 구성
    api_url = f"https://graph.facebook.com/v12.0/instagram_oembed?url={embed_url}&omitscript=true"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            st.error("Instagram API 요청 실패")
            return None
    except requests.exceptions.RequestException as e:
        st.error(f"API 요청 중 오류가 발생했습니다: {e}")
        return None

# 스트림릿 앱 설정
st.title("타 사용자의 Instagram 게시물 보기")

# 표시할 Instagram 게시물의 URL
embed_url = st.text_input("Instagram 게시물 URL을 입력하세요:", "https://www.instagram.com/p/EXAMPLE")

if embed_url:
    post_data = get_instagram_post(embed_url)

    if post_data:
        st.subheader("게시물 미리보기")
        st.write(f"Caption: {post_data.get('title')}")
        st.image(post_data.get('thumbnail_url'), use_column_width=True)
        st.write(f"[Instagram에서 보기]({post_data.get('author_url')})")
    else:
        st.write("게시물을 가져올 수 없습니다.")
