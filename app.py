import streamlit as st
from PIL import Image
import time
import os

# ───────────────────────────────────────────────────
# 논리 회로 계산 및 포뮬러 생성 함수
# ───────────────────────────────────────────────────
def AND_gate(a, b):
    res = a & b
    return res, f"A({a}) · B({b}) = X({res})"

def OR_gate(a, b):
    res = a | b
    return res, f"A({a}) + B({b}) = X({res})"

def NOT_gate(a, _b=None):
    res = 1 - a
    return res, f"¬A({a}) = X({res})"

def NOR_gate(a, b):
    or_res = a | b
    res = 1 - or_res
    return res, f"¬(A({a}) + B({b})) = X({res})"

def XOR_gate(a, b):
    res = a ^ b
    return res, f"A({a}) ⊕ B({b}) = X({res})"

# ───────────────────────────────────────────────────
# 메인 스트림릿 앱
# ───────────────────────────────────────────────────
def main():
    st.set_page_config(page_title="Digital Logic Simulator", layout="centered")
    st.title("🖥️ Digital Logic Gate Simulator")

    # 사용자 입력
    col1, col2 = st.columns(2)
    a = col1.radio("A 입력", [0, 1], index=0, horizontal=True)
    b = col2.radio("B 입력", [0, 1], index=0, horizontal=True)

    gate = st.selectbox("게이트 선택", ["AND", "OR", "NOT", "NOR", "XOR"])

    # 실행 버튼
    if st.button("실행"):
        # 결과 계산
        if gate == "AND":
            res, formula = AND_gate(a, b)
            img_path = "images/and_gate.png"
        elif gate == "OR":
            res, formula = OR_gate(a, b)
            img_path = "images/or_gate.png"
        elif gate == "NOT":
            res, formula = NOT_gate(a)
            img_path = "images/not_gate.png"
        elif gate == "NOR":
            res, formula = NOR_gate(a, b)
            img_path = "images/nor_gate.png"
        elif gate == "XOR":
            res, formula = XOR_gate(a, b)
            img_path = "images/xor_gate.png"
        else:
            st.error("알 수 없는 게이트입니다.")
            return

        # 이미지 로드
        if os.path.exists(img_path):
            img = Image.open(img_path)
            st.image(img, caption=f"{gate} 게이트", use_column_width=False)
        else:
            st.warning(f"이미지 파일을 찾을 수 없습니다: {img_path}")

        # 논리식 & 결과 표시
        st.markdown(f"**논리식:** `{formula}`")
        st.markdown(f"**결과:** {res}")

        # 간단 애니메이션 흐름
        flow = st.empty()
        flow.text(f"A → {a}    B → {b}")
        time.sleep(0.3)
        flow.text(f"A → {a}    B → {b}    ▶ X → {res}")

    # 사이드바에 종료 안내
    st.sidebar.markdown("---")
    st.sidebar.write("🔴 종료하려면 터미널에서 `Ctrl+C` 또는 창을 닫으세요.")

if __name__ == "__main__":
    main()
