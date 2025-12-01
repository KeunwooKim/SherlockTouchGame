import streamlit as st
from assets import IMAGES, SOUNDS
from ui_components import (
    show_narration, 
    show_dialogue, 
    set_background, 
    get_base64_of_bin_file, 
    show_center_message,
    update_state
)

# --- 콜백 함수들 ---

def update_hat_clicks():
    """모자 클릭 횟수를 증가시킵니다."""
    st.session_state.hat_clicks += 1

def handle_question_click(q_id):
    """질문 클릭을 처리하고 상태를 업데이트합니다."""
    st.session_state.questions_asked.add(q_id)
    st.session_state.display_answer = q_id

def reset_and_start_over():
    """게임을 초기화하고 처음으로 돌아갑니다."""
    st.session_state.clear()

# --- 씬(Scene) 렌더링 함수 ---

def render_boot_scene():
    """오디오 재생을 위한 사용자 상호작용을 유도하는 시작 씬"""
    set_background(None, color="black")
    st.title("셜록 홈즈: 푸른 카벙클의 모험")
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    _, col2, _ = st.columns([1, 1, 1])
    with col2:
        st.button(
            "START", 
            key="start_game", 
            use_container_width=True,
            on_click=update_state,
            kwargs={'scene': 'intro_1'}
        )

def render_intro():
    """게임 시작 전 인트로 씬들을 관리합니다."""
    scene = st.session_state.scene
    set_background(None, color="black")

    if scene == 'intro_1':
        show_narration("해당 게임은 아서 코난 도일 원작의 셜록홈즈 시리즈 중 ‘푸른 카벙클의 모험’을 기반으로 사건의 토대를 가져와 재구성한 비영리 목적의 과제용 게임입니다.", is_meta=True)
        st.markdown('<div class="next-button">', unsafe_allow_html=True)
        st.button("계속하기", key="intro1_next", on_click=update_state, kwargs={'scene': 'intro_2'})
        st.markdown('</div>', unsafe_allow_html=True)
    elif scene == 'intro_2':
        show_narration("스크립터의 부족한 역량과 분량상의 문제로 각색하거나 삭제한 내용이 다수 존재합니다. 해당 게임은 추리 과정을 직접 플레이하는데 의의를 두고 있다는 점 양해 바랍니다.", is_meta=True)
        st.markdown('<div class="next-button">', unsafe_allow_html=True)
        st.button("계속하기", key="intro2_next", on_click=update_state, kwargs={'scene': 'intro_3'})
        st.markdown('</div>', unsafe_allow_html=True)
    elif scene == 'intro_3':
        show_narration("그럼, 시작합니다.", is_meta=True)
        st.button("시작하기", key="intro3_start", on_click=update_state, kwargs={'scene': 'scene_1_narration_1'}, use_container_width=True)

def render_scene_1():
    """첫 번째 씬: 홈즈의 집, 피터슨의 방문"""
    scene = st.session_state.scene
    
    if scene in ['scene_1_narration_1', 'scene_1_narration_2']:
        set_background(IMAGES["street"])
    else:
        set_background(IMAGES["lobby"])


    if scene == 'scene_1_narration_1':
        show_narration("크리스마스 무렵의 런던. 경찰관과 피터슨이 길거리에서 싸움을 목격한다. 피터슨은 이를 제지하려 한다.")
        st.markdown('<div class="next-button">', unsafe_allow_html=True)
        st.button("계속하기", key="s1_n1_next", on_click=update_state, kwargs={'scene': 'scene_1_narration_2'})
        st.markdown('</div>', unsafe_allow_html=True)
    elif scene == 'scene_1_narration_2':
        show_narration("이때 한 남자가 모자와 거위를 잃고 도망쳤고, 피터슨은 모자와 거위를 어떻게 처리할까 고민하다 끝내 홈즈에게로 향한다.")
        st.markdown('<div class="next-button">', unsafe_allow_html=True)
        st.button("계속하기", key="s1_n2_next", on_click=update_state, kwargs={'scene': 'scene_1_dialogue_1'})
        st.markdown('</div>', unsafe_allow_html=True)
    elif scene == 'scene_1_dialogue_1':
        show_dialogue(IMAGES["watson"], "왓슨", "나 왔네, 홈즈.", alignment='right')
        st.markdown('<div class="next-button">', unsafe_allow_html=True)
        st.button("계속하기", key="s1_d1_next", on_click=update_state, kwargs={'scene': 'scene_1_dialogue_2'})
        st.markdown('</div>', unsafe_allow_html=True)
    elif scene == 'scene_1_dialogue_2':
        show_dialogue(IMAGES["holmes"], "홈즈", "어서오게.")
        st.markdown('<div class="next-button">', unsafe_allow_html=True)
        st.button("계속하기", key="s1_d2_next", on_click=update_state, kwargs={'scene': 'scene_1_dialogue_3'})
        st.markdown('</div>', unsafe_allow_html=True)
    elif scene == 'scene_1_dialogue_3':
        show_dialogue(IMAGES["watson"], "왓슨", "......뭘 보고 있는 건가?", alignment='right')
        st.markdown('<div class="next-button">', unsafe_allow_html=True)
        st.button("계속하기", key="s1_d3_next", on_click=update_state, kwargs={'scene': 'scene_1_dialogue_4'})
        st.markdown('</div>', unsafe_allow_html=True)
    elif scene == 'scene_1_dialogue_4':
        peterson_img = get_base64_of_bin_file(IMAGES["peterson"])
        st.markdown(f'<div class="center-container"><img src="data:image/png;base64,{peterson_img}"></div>', unsafe_allow_html=True)
        show_dialogue(IMAGES["holmes"], "홈즈", "보다시피 모자와 거위라네. 이쪽의 피터슨 수위께서 내게 가져오셨지.")
        st.button("조사하기", key="s1_d4_investigate", on_click=update_state, kwargs={'scene': 'scene_2_investigation'}, use_container_width=True)

def render_scene_2_investigation():
    """두 번째 씬: 모자와 거위 조사"""
    set_background(IMAGES["lobby"])
    show_narration("홈즈가 조사를 시작했다. 거위와 모자를 자세히 살펴보자.")
    
    col1, col2 = st.columns(2)

    with col1:
        st.image(IMAGES["goose"], width=300)
        if st.button("거위 조사하기", key="inv_goose", use_container_width=True):
            show_center_message("For Mrs. Henry Baker 라고 적혀 있는 꼬리표가 있다.")
            show_center_message("평범한 거위다. 토실토실한게 맛있어 보인다.")

    with col2:
        st.image(IMAGES["hat"], width=300)
        if st.button("모자 조사하기", key="inv_hat", use_container_width=True):
            st.session_state.hat_clicks += 1
        
        if st.session_state.hat_clicks > 0:
            if st.session_state.hat_clicks == 1:
                show_center_message("낡은 모자다. 꽤 오래 착용해 온 듯 연식이 느껴지는 것으로 보아 주인은 중년 남성일 가능성이 높다.")
            elif st.session_state.hat_clicks == 2:
                show_center_message("관리되지 않은 것으로 보아 부인이 주인을 돌보지 않는 듯 하다. 또한, 새 것을 사지 않는 것은 생활고와 연관이 있어 보인다.")
            else:
                show_center_message("모자에서 술과 담배 냄새가 나는 것으로 보아 주인은 펍에 자주 드나드는 듯 하다.")
    
    st.button("조사 완료", key="inv_finish", on_click=update_state, kwargs={'scene': 'scene_3_dialogue_1'}, use_container_width=True)

def render_scene_3_and_4():
    """세 번째 씬: 추리 결과 / 네 번째 씬: 헨리 베이커"""
    set_background(IMAGES["lobby"])
    scene = st.session_state.scene

    if scene.startswith('scene_3'):
        if scene == 'scene_3_dialogue_1':
            show_dialogue(IMAGES["holmes"], "홈즈", "지금 알 수 있는 정보는 대략 이 정도겠군. 이 거위의 주인은 헨리 베이커라는 이름을 가진 생활고에 시달리는 중년 남성일 가능성이 높네.")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s3_d1_next", on_click=update_state, kwargs={'scene': 'scene_3_dialogue_2'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_3_dialogue_2':
            show_dialogue(IMAGES["watson"], "왓슨", "모자와 거위만 가지고 이만큼이나 알아내다니, 역시 자네로군.", alignment='right')
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s3_d2_next", on_click=update_state, kwargs={'scene': 'scene_3_dialogue_3'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_3_dialogue_3':
            show_dialogue(IMAGES["holmes"], "홈즈", "자넨 매번 칭찬이 똑같군 그래. 다음엔 조금 더 창의적인 칭찬을 기대하겠네.")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s3_d3_next", on_click=update_state, kwargs={'scene': 'scene_3_narration_1'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_3_narration_1':
            show_narration("홈즈는 거위를 피터슨에게 포상으로 주고, 피터슨은 감사히 받아간다.")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s3_n1_next", on_click=update_state, kwargs={'scene': 'scene_3_narration_2'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_3_narration_2':
            show_narration("이후 피터슨의 아내가 거위를 요리 하려다가, 그 안에서 귀중한 보석 ‘푸른 카벙클’을 발견한다.")
            jewel_base64 = get_base64_of_bin_file(IMAGES["jewel"])
            st.markdown(f'<div style="position:fixed; top:40%; left:50%; transform: translate(-50%, -50%);"><img src="data:image/png;base64,{jewel_base64}" width=150></div>', unsafe_allow_html=True)
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s3_n2_next", on_click=update_state, kwargs={'scene': 'scene_3_narration_3'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_3_narration_3':
            show_narration("홈즈는 범인이 거위의 뱃속에 보석을 숨긴 이유를 추적하기 시작한다.")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s3_n3_next", on_click=update_state, kwargs={'scene': 'scene_4_narration_1'})
            st.markdown('</div>', unsafe_allow_html=True)

    elif scene.startswith('scene_4'):
        questions = {"q1": "거위의 배에서 보석이 나온 사실을 아는가?", "q2": "거위를 어디에서 누구에게 받았는가?", "q3": "거위를 어디에서 산 것인가?"}
        answers = {"q1": "전혀 몰랐습니다. 저는 애초에 거위만 찾으려고 온 걸요.", "q2": "제가 산 것입니다.", "q3": "저는 사실 ‘알파인 거위 클럽’ 의 회원으로, 클럽이 마련한 가게에서 거위를 산 것 뿐입니다. 브렉스톤 이라는 사람이 주인인 가게였었죠."}

        if st.session_state.get('display_answer'):
            answer_id = st.session_state.display_answer
            show_dialogue(IMAGES["baker"], "헨리", answers[answer_id])
            st.button("다른 질문을 한다", key="ask_another", on_click=update_state, kwargs={'display_answer': None}, use_container_width=True)
        elif scene == 'scene_4_narration_1':
            show_narration("광고를 내고 얼마 후, 헨리 베이커가 홈즈를 찾아온다.")
            st.button("대화하기", key="s4_n1_next", on_click=update_state, kwargs={'scene': 'scene_4_dialogue_1'}, use_container_width=True)
        elif scene == 'scene_4_dialogue_1':
            show_dialogue(IMAGES["holmes"], "홈즈", "당신이 헨리 베이커 로군요.")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s4_d1_next", on_click=update_state, kwargs={'scene': 'scene_4_dialogue_2'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_4_dialogue_2':
            show_dialogue(IMAGES["baker"], "헨리", "맞습니다. 제 거위는 어디 있지요?")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s4_d2_next", on_click=update_state, kwargs={'scene': 'scene_4_dialogue_3'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_4_dialogue_3':
            show_dialogue(IMAGES["holmes"], "홈즈", "아쉽게도 분실한 거위를 습득한 수위에게 줘 버렸습니다. 제가 새 거위를 한 마리 사 드릴 테니 염려 마시고, 몇 가지 질문에 대답을 해 주셨으면 합니다.")
            st.button("질문하기", key="s4_d3_next", on_click=update_state, kwargs={'scene': 'scene_4_questions', 'questions_asked': set()}, use_container_width=True)
        elif scene == 'scene_4_questions':
            show_dialogue(IMAGES["baker"], "헨리", "제가 아는 선에서는 최대한 답해 드리겠습니다.")
            for q_id, q_text in questions.items():
                if q_id not in st.session_state.questions_asked:
                    st.button(q_text, key=q_id, on_click=handle_question_click, args=(q_id,), use_container_width=True)
            if len(st.session_state.questions_asked) == len(questions):
                st.markdown('<div class="next-button">', unsafe_allow_html=True)
                st.button("계속하기", key="q_finish", on_click=update_state, kwargs={'scene': 'scene_4_narration_2'})
                st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_4_narration_2':
            show_narration("홈즈는 헨리가 대답할 때의 호흡과 동공의 움직임, 몸의 경직도 등으로 미루어 보아 그가 진실만을 말했음을 깨닫는다.")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s4_n2_next", on_click=update_state, kwargs={'scene': 'scene_4_narration_3'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_4_narration_3':
            show_narration("홈즈는 생각한다. ‘진범은 거위를 공급한 경로에 있다.’ 이에 거위의 유통 경로를 조사하기로 한다.")
            st.button("계속하기", key="s4_n3_next", on_click=update_state, kwargs={'scene': 'scene_5_dialogue_1'}, use_container_width=True)

def render_final_scenes():
    """마지막 씬들: 브렉스톤, 제임스 라이더, 그리고 결말"""
    scene = st.session_state.scene
    
    if scene.startswith('scene_5'):
        set_background(IMAGES["brexton_store"])
        questions = {"q1": "당신네 거위의 품질이 가장 좋다 하여 물어 보았다.", "q2": "그렇게나 뛰어난 거위들을 어디서 들여오는지?"}
        answers = {"q1": "흥! 보는 눈은 있군. 맞소. 난 항상 뛰어난 거위들만을 선별해 가게로 들여오지", "q2": "윈디게이트 부인네 농장에서 들여오고 있소. 거기 거위들의 품질이 매우 뛰어나거든."}

        if st.session_state.get('display_answer') and st.session_state.scene == 'scene_5_questions':
            answer_id = st.session_state.display_answer
            show_dialogue(IMAGES["braxton"], "브렉스톤", answers[answer_id])
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("다음 질문으로", key="ask_another_braxton", on_click=update_state, kwargs={'display_answer': None})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_5_dialogue_1':
            # This scene is just a transition, background is set in the main block
            show_narration("홈즈는 거위의 유통 경로를 역추적하기 시작했다. 첫 번째 목적지는 브렉스톤의 가게다.")
            st.button("가게로 들어가기", key="s5_d1_next", on_click=update_state, kwargs={'scene': 'scene_5_dialogue_2'}, use_container_width=True)
        elif scene == 'scene_5_dialogue_2':
            show_dialogue(IMAGES["braxton"], "브렉스톤", "반갑소 홈즈선생.")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s5_d2_next", on_click=update_state, kwargs={'scene': 'scene_5_dialogue_3'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_5_dialogue_3':
            show_dialogue(IMAGES["holmes"], "홈즈", "반갑습니다, 브렉스톤씨. 당신에게 묻고 싶은게 있습니다.")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s5_d3_next", on_click=update_state, kwargs={'scene': 'scene_5_dialogue_4'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_5_dialogue_4':
            show_dialogue(IMAGES["braxton"], "브렉스톤", "또 그놈의 거위 얘기요? 저번에도 웬 이상한 놈이 찾아와 귀찮게 앵앵 거리더니!")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s5_d4_next", on_click=update_state, kwargs={'scene': 'scene_5_questions', 'questions_asked': set()})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_5_questions':
            show_dialogue(IMAGES["braxton"], "브렉스톤", "흥!")
            show_narration("브렉스톤의 언행을 통해 진범이 브렉스톤에게 접근한 적이 있었다는 점을 눈치챈 홈즈. 그는 브렉스톤을 도발하고 구슬려 거위의 공급처를 알아내기로 한다.")
            for q_id, q_text in questions.items():
                if q_id not in st.session_state.questions_asked:
                    st.button(q_text, key=q_id, on_click=handle_question_click, args=(q_id,), use_container_width=True)
            if len(st.session_state.questions_asked) == len(questions):
                st.button("계속하기", key="s5_q_finish", on_click=update_state, kwargs={'scene': 'scene_6_narration_1'}, use_container_width=True)

    elif scene.startswith('scene_6'):
        set_background(IMAGES["windigate_farm"])
        if scene == 'scene_6_narration_1':
            show_narration("홈즈와 왓슨은 윈디게이트 부인의 농장으로 찾아가, ‘제임스 라이더’라는 남자가 사건의 핵심 인물임을 알아낸다.")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s6_n1_next", on_click=update_state, kwargs={'scene': 'scene_6_narration_2'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_6_narration_2':
            show_narration("추적 끝에, 그들은 마침내 제임스 라이더와 대면한다.")
            st.button("대면하기", key="s6_n2_next", on_click=update_state, kwargs={'scene': 'scene_6_dialogue_1'}, use_container_width=True)
        elif scene == 'scene_6_dialogue_1':
            show_dialogue(IMAGES["ryder_1"], "제임스", "왜, 왜 저를 찾으신 겁니까?")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s6_d1_next", on_click=update_state, kwargs={'scene': 'scene_6_dialogue_2'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_6_dialogue_2':
            show_dialogue(IMAGES["holmes"], "홈즈", "최근 발생한 보석 도난 사건 때문이오. 단서를 추적하다 그대에게 묻고 싶은 것이 있소.")
            st.button("추궁하기", key="s6_d2_next", on_click=update_state, kwargs={'scene': 'scene_6_holmes_q1', 'fear_level': 1}, use_container_width=True)
        
        elif scene == 'scene_6_holmes_q1':
            show_dialogue(IMAGES["holmes"], "홈즈", "보석은 호텔에서 분실했다. 즉, 호텔 관계자가 범인일 확률이 높다. 짐작가는 바가 있는가?")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s6_hq1_next", on_click=update_state, kwargs={'scene': 'scene_6_ryder_a1'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_6_ryder_a1':
            show_dialogue(IMAGES["ryder_2"], "제임스", "저, 정말 모릅니다! 저는 보석을 본 적도 없는걸요!")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s6_ra1_next", on_click=update_state, kwargs={'scene': 'scene_6_holmes_q2', 'fear_level': 2})
            st.markdown('</div>', unsafe_allow_html=True)
        
        elif scene == 'scene_6_holmes_q2':
            show_dialogue(IMAGES["holmes"], "홈즈", "범행은 보석의 주인이 잠들었거나, 청소를 위해 하인들이 방 안에 들어갔을 때 만 가능하다. 이 시간대에 근무한 하인들의 명단 중 당신의 이름도 있다.")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s6_hq2_next", on_click=update_state, kwargs={'scene': 'scene_6_ryder_a2'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_6_ryder_a2':
            show_dialogue(IMAGES["ryder_crouch"], "제임스", "히이익!")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s6_ra2_next", on_click=update_state, kwargs={'scene': 'scene_6_holmes_q3', 'fear_level': 3})
            st.markdown('</div>', unsafe_allow_html=True)

        elif scene == 'scene_6_holmes_q3':
            show_dialogue(IMAGES["holmes"], "홈즈", "이미 용의자 몇 명이 체포되었다. 그들은 강도 높은 심문을 받고 있다. 정말 아무것도 모르는가?")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s6_hq3_next", on_click=update_state, kwargs={'scene': 'scene_6_ryder_a3'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_6_ryder_a3':
            show_dialogue(IMAGES["ryder_crouch"], "제임스", "으, 으으으! 아아아악!")
            st.button("자백을 받아냈다", key="s6_ra3_finish", on_click=update_state, kwargs={'scene': 'scene_7_confession'}, use_container_width=True)

    elif scene.startswith('scene_7') or scene == 'the_end':
        set_background(IMAGES["windigate_farm"])
        if scene == 'scene_7_confession':
            show_dialogue(IMAGES["ryder_crouch"], "제임스", "죄송합니다! 죄송해요! 제가, 제가 훔친게 맞습니다!")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s7_c_next", on_click=update_state, kwargs={'scene': 'scene_7_narration_1'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_7_narration_1':
            show_narration("제임스는 모든 것을 자백했다. 그는 하녀 캐서린 쿠삭과 공모해 보석을 훔쳤고, 도망치던 중 거위의 뱃속에 보석을 숨겼다. 하지만 실수로 그 거위를 팔아버렸고, 거위는 돌고 돌아 헨리의 손에 들어갔던 것이다.")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s7_n1_next", on_click=update_state, kwargs={'scene': 'scene_7_dialogue_1'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_7_dialogue_1': # This is where Watson asks what to do
            show_dialogue(IMAGES["watson"], "왓슨", "그래서, 이 자는 어찌할 건가 홈즈?", alignment='right')
            # NEW: Choices here
            col1, col2 = st.columns(2)
            with col1:
                st.button("용서하기", key="forgive_choice", on_click=update_state, kwargs={'scene': 'scene_7_ending_sequence_start'}, use_container_width=True)
            with col2:
                st.button("용서하지 않기", key="not_forgive_choice", on_click=update_state, kwargs={'scene': 'scene_7_persuasion_1'}, use_container_width=True)

        elif scene == 'scene_7_persuasion_1':
            show_dialogue(IMAGES["holmes"], "홈즈", "그는 아직 젊고, 이번이 처음 저지른 범죄일세. 그리고 보게, 이미 극도의 공포를 느끼고 있지 않나. 이런 청년에겐 체포보다는 자비로운 용서가 더 큰 교훈이 될 수 있다네.")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("계속하기", key="s7_p1_next", on_click=update_state, kwargs={'scene': 'scene_7_persuasion_2'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_7_persuasion_2':
            show_dialogue(IMAGES["holmes"], "홈즈", "크리스마스지 않나. 오늘 만큼은 정의보다는 자비가 더 낫지 않겠나 왓슨?")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("용서하기", key="forgive_persuaded", on_click=update_state, kwargs={'scene': 'scene_7_ending_sequence_start'})
            st.markdown('</div>', unsafe_allow_html=True)

        elif scene == 'scene_7_ending_sequence_start': # This is where the emotional_theme starts
            # The music logic in main.py will pick up emotional_theme for scene_7_ending_sequence_start
            # Automatically transition to the next scene after BGM starts
            st.session_state.scene = 'scene_7_ending_dialogue_1'
            st.rerun()

        elif scene == 'scene_7_ending_dialogue_1': # Renamed from scene_7_dialogue_3
            show_dialogue(IMAGES["watson"], "왓슨", "뭐? 이 자는 엄연히 절도죄를 저지른 범죄자일세. 정말 그를 용서할 건가?", alignment='right')
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("...", key="s7_d3_next", on_click=update_state, kwargs={'scene': 'scene_7_ending_dialogue_2'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_7_ending_dialogue_2': # Renamed from scene_7_dialogue_4
            show_dialogue(IMAGES["holmes"], "홈즈", "그는 아직 젊고, 이번이 처음 저지른 범죄일세. 그리고 보게, 이미 극도의 공포를 느끼고 있지 않나. 이런 청년에겐 체포보다는 자비로운 용서가 더 큰 교훈이 될 수 있다네.")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("...", key="s7_d4_next", on_click=update_state, kwargs={'scene': 'scene_7_ending_dialogue_3'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_7_ending_dialogue_3': # Renamed from scene_7_dialogue_5
            show_dialogue(IMAGES["holmes"], "홈즈", "크리스마스지 않나. 오늘 만큼은 정의보다는 자비가 더 낫지 않겠나 왓슨?")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("...", key="s7_d5_next", on_click=update_state, kwargs={'scene': 'scene_7_ending_1'}) # Original s7_ending_1
            st.markdown('</div>', unsafe_allow_html=True)

        elif scene == 'scene_7_ending_1': # Original scene_7_ending_1, now renamed as the *first* narration of the ending
            set_background(None, color="black")
            show_narration("성야의 종소리가 울려 퍼진다.")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("...", key="s7_e1_next", on_click=update_state, kwargs={'scene': 'scene_7_ending_2'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_7_ending_2':
            set_background(None, color="black")
            show_narration("오늘 밤, 과오를 저지른 한 젊은 청년은 새로 태어났다.")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("...", key="s7_e2_next", on_click=update_state, kwargs={'scene': 'scene_7_ending_3'})
            st.markdown('</div>', unsafe_allow_html=True)
        elif scene == 'scene_7_ending_3':
            set_background(None, color="black")
            show_narration("또한 늘 정의를 좇던 홈즈의 인간성이 새하얀 눈밭 위의 발자국처럼 족적을 남긴 날이기도 하다.")
            st.markdown('<div class="next-button">', unsafe_allow_html=True)
            st.button("게임 끝", key="s7_e3_finish", on_click=update_state, kwargs={'scene': 'the_end'})
            st.markdown('</div>', unsafe_allow_html=True)
        
        elif scene == 'the_end':
            set_background(None, color="black")
            show_narration("The End.", is_meta=True)
            st.button("처음으로 돌아가기", key="restart", on_click=reset_and_start_over, use_container_width=True)
