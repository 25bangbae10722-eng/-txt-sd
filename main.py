import streamlit as st
import random

# 게임 초기화 함수
def start_game():
    # 1부터 100 사이의 숫자 중 랜덤으로 하나를 선택
    target_number = random.randint(1, 100)
    attempts = 0  # 시도 횟수 초기화
    return target_number, attempts

# 게임 로직
def play_game():
    # 게임 시작 시 타겟 숫자와 시도 횟수 초기화
    if 'target_number' not in st.session_state:
        st.session_state.target_number, st.session_state.attempts = start_game()

    target_number = st.session_state.target_number
    attempts = st.session_state.attempts

    # 사용자 입력 받기
    guess = st.number_input('1부터 100 사이의 숫자를 입력하세요', min_value=1, max_value=100, step=1)

    # 게임 진행
    if st.button('숫자 맞추기'):
        if guess < target_number:
            st.session_state.attempts += 1
            st.write("입력한 숫자가 너무 작아요! 더 큰 숫자를 입력해보세요.")
        elif guess > target_number:
            st.session_state.attempts += 1
            st.write("입력한 숫자가 너무 커요! 더 작은 숫자를 입력해보세요.")
        else:
            st.session_state.attempts += 1
            st.write(f"축하합니다! 숫자 {target_number}를 맞추셨습니다!")
            st.write(f"총 {st.session_state.attempts}번 만에 맞추셨습니다!")
            # 게임을 다시 시작할지 선택할 수 있는 버튼
            if st.button('게임 다시 시작'):
                st.session_state.target_number, st.session_state.attempts = start_game()
                st.write("게임이 다시 시작되었습니다. 새로운 숫자를 맞춰보세요!")

# 게임 실행
st.title('숫자 맞추기 게임')
play_game()
+
+
