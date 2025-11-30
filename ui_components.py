import streamlit as st
import base64
import os

@st.cache_data
def get_base64_of_bin_file(bin_file):
    """바이너리 파일을 base64로 인코딩된 문자열로 변환합니다."""
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    st.error(f"파일을 찾을 수 없습니다: {bin_file}")
    return None

def load_css(file_name):
    """지정된 CSS 파일을 읽어 <style> 태그 안에 삽입합니다."""
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def set_background(image_path, color=""):
    """화면에 배경 이미지를 설정하거나 배경색을 지정합니다."""
    if image_path:
        image_base64 = get_base64_of_bin_file(image_path)
        if image_base64:
            st.markdown(
                f'''
                <style>
                body, .stApp {{
                    background-image: url("data:image/jpeg;base64,{image_base64}");
                }}
                </style>
                ''',
                unsafe_allow_html=True
            )
    elif color:
        st.markdown(
            f'''
            <style>
            body, .stApp {{
                background-color: {color};
            }}
            </style>
            ''',
            unsafe_allow_html=True
        )

def show_narration(text, is_meta=False):
    """나레이션 텍스트 상자를 화면에 표시합니다."""
    box_class = "narration-box-meta" if is_meta else "narration-box-ingame"
    st.markdown(
        f'<div class="narration-box {box_class}">{text}</div>',
        unsafe_allow_html=True
    )

def show_dialogue(char_img, char_name, dialogue, alignment='left'):
    """캐릭터 이미지와 함께 대화창을 표시합니다."""
    char_base64 = get_base64_of_bin_file(char_img)
    align_class = "align-right" if alignment == 'right' else "align-left"

    st.markdown(
        f'''
        <div class="dialogue-box {align_class}">
            <div class="char-name">{char_name}</div>
            <img class="dialogue-character-image" src="data:image/png;base64,{char_base64}">
            <p class="dialogue-text">"{dialogue}"</p>
        </div>
        ''',
        unsafe_allow_html=True
    )

def play_sound(sound_file):
    """오디오 파일을 한 번 재생합니다. BGM과 충돌하지 않도록 JS를 사용합니다."""
    sound_base64 = get_base64_of_bin_file(sound_file)
    if sound_base64:
        js_code = f"""
            <script>
                var audio = document.getElementById("sfx_player");
                audio.src = "data:audio/mp3;base64,{sound_base64}";
                audio.play();
            </script>
        """
        st.markdown(js_code, unsafe_allow_html=True)


def show_center_message(message, duration=3):
    """화면 중앙에 메시지를 띄우고 몇 초 후 사라지게 합니다."""
    # 메시지 내용으로 고유 ID 생성 (간단한 해시)
    message_hash = f"msg-{hash(message)}"
    
    message_html = f"""
        <div id="{message_hash}" class="center-message">
            {message}
        </div>
        <script>
            setTimeout(function() {{
                var element = document.getElementById("{message_hash}");
                if (element) {{
                    element.style.display = 'none';
                }}
            }}, {duration * 1000});
        </script>
    """
    st.markdown(message_html, unsafe_allow_html=True)

