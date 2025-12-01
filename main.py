import streamlit as st
from ui_components import load_css, get_base64_of_bin_file
from assets import SOUNDS
from scenes import (
    render_boot_scene,
    render_intro,
    render_scene_1,
    render_scene_2_investigation,
    render_scene_3_and_4,
    render_final_scenes
)

# --- 메인 실행 로직 ---
def main():
    """게임의 메인 로직을 실행하고 씬을 전환합니다."""

    # 0. CSS 로드
    load_css('style.css')
    
    # 1. 세션 상태 초기화
    if 'scene' not in st.session_state:
        st.session_state.scene = 'boot'
    if 'hat_clicks' not in st.session_state:
        st.session_state.hat_clicks = 0
    if 'questions_asked' not in st.session_state:
        st.session_state.questions_asked = set()
    if 'fear_level' not in st.session_state:
        st.session_state.fear_level = 1
    if 'display_answer' not in st.session_state:
        st.session_state.display_answer = None
    if 'current_bgm' not in st.session_state:
        st.session_state.current_bgm = None
    if 'bgm_src' not in st.session_state:
        st.session_state.bgm_src = ""

    # 2. BGM 로직
    current_scene = st.session_state.scene
    bgm_to_play = None

    if current_scene == 'boot':
        bgm_to_play = None
    elif current_scene.startswith('intro') or current_scene.startswith('scene_1') or current_scene.startswith('scene_3') or current_scene.startswith('scene_4'):
        bgm_to_play = SOUNDS["main_theme"]
    elif current_scene.startswith('scene_2') or current_scene.startswith('scene_5'):
        bgm_to_play = SOUNDS["investigation_theme"]
    elif current_scene.startswith('scene_6'):
        bgm_to_play = SOUNDS["confrontation_theme"]
    elif current_scene.startswith('scene_7_ending') or current_scene == 'the_end':
        bgm_to_play = SOUNDS["emotional_theme"]

    # 이전에 재생하던 BGM과 다를 경우에만 src 업데이트
    if st.session_state.get('current_bgm') != bgm_to_play:
        if bgm_to_play:
            sound_base64 = get_base64_of_bin_file(bgm_to_play)
            st.session_state.bgm_src = f"data:audio/mp3;base64,{sound_base64}" if sound_base64 else ""
            st.toast(f"🎵 BGM 시작: {bgm_to_play.split('/')[-1]}")
        else:
            st.session_state.bgm_src = ""
            if st.session_state.current_bgm is not None: # 이미 음악이 없던게 아니라면 중지 토스트
                 st.toast("🎵 BGM 중지")
        st.session_state.current_bgm = bgm_to_play
    
    # 3. 오디오 플레이어 렌더링
    st.markdown(f'<audio src="{st.session_state.bgm_src}" loop autoplay></audio>', unsafe_allow_html=True)
    
    # 4. 현재 씬에 맞는 함수 호출
    current_scene = st.session_state.scene
    if current_scene == 'boot':
        render_boot_scene()
    elif current_scene.startswith('intro'):
        render_intro()
    elif current_scene.startswith('scene_1'):
        render_scene_1()
    elif current_scene.startswith('scene_2'):
        render_scene_2_investigation()
    elif current_scene.startswith('scene_3') or current_scene.startswith('scene_4'):
        render_scene_3_and_4()
    elif current_scene.startswith('scene_5') or current_scene.startswith('scene_6') or current_scene.startswith('scene_7') or current_scene == 'the_end':
        render_final_scenes()
    else:
        st.error("오류: 알 수 없는 씬입니다.")
        if st.button("처음으로 돌아가기"):
            st.session_state.clear()

if __name__ == "__main__":
    main()
