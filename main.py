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
    
    # 0. CSS 로드 및 오디오 플레이어 준비
    load_css('style.css')
    # st.markdown('<audio id="sfx_player"></audio>', unsafe_allow_html=True)
    # st.markdown('<audio id="bgm_player" loop autoplay></audio>', unsafe_allow_html=True)
    
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
    # if 'current_bgm' not in st.session_state:
    #     st.session_state.current_bgm = None

    # # 2. BGM 로직
    # current_scene = st.session_state.scene
    # bgm_to_play = None

    # if current_scene == 'boot':
    #     bgm_to_play = None
    # elif current_scene == 'the_end':
    #     bgm_to_play = None
    # elif current_scene.startswith('intro') or current_scene.startswith('scene_1') or current_scene.startswith('scene_3') or current_scene.startswith('scene_4'):
    #     bgm_to_play = SOUNDS["main_theme"]
    # elif current_scene.startswith('scene_2') or current_scene.startswith('scene_5'):
    #     bgm_to_play = SOUNDS["investigation_theme"]
    # elif current_scene.startswith('scene_6'):
    #     bgm_to_play = SOUNDS["confrontation_theme"]
    # elif current_scene.startswith('scene_7'):
    #     bgm_to_play = SOUNDS["emotional_theme"]

    # if st.session_state.current_bgm != bgm_to_play:
    #     if bgm_to_play:
    #         sound_base64 = get_base64_of_bin_file(bgm_to_play)
    #         if sound_base64:
    #             js_code = f"""
    #                 <script>
    #                     var bgmPlayer = document.getElementById("bgm_player");
    #                     if (bgmPlayer) {{
    #                         bgmPlayer.src = "data:audio/mp3;base64,{sound_base64}";
    #                         bgmPlayer.play();
    #                     }}
    #                 </script>
    #             """
    #             st.markdown(js_code, unsafe_allow_html=True)
    #     else: # bgm_to_play is None
    #         js_code = """
    #             <script>
    #                 var bgmPlayer = document.getElementById("bgm_player");
    #                 if (bgmPlayer) {
    #                     bgmPlayer.pause();
    #                     bgmPlayer.src = "";
    #                 }
    #             </script>
    #         """
    #         st.markdown(js_code, unsafe_allow_html=True)
        
    #     st.session_state.current_bgm = bgm_to_play

    # 3. 현재 씬에 맞는 함수 호출
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
            st.rerun()