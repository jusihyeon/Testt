import streamlit as st

st.title("디지털 논리 회로 시뮬레이터")

st.markdown("### 입력값 선택")
a = st.checkbox("입력 A", value=False)
b = st.checkbox("입력 B", value=False)

# 논리 회로 함수 정의
def AND(x, y):
    return x and y

def OR(x, y):
    return x or y

def NAND(x, y):
    return not (x and y)

def NOR(x, y):
    return not (x or y)

def NOT(x):
    return not x

def XOR(x, y):
    return x != y

# 결과 출력
st.markdown("---")
st.markdown("### 회로 출력 결과")

col1, col2 = st.columns(2)

with col1:
    st.write("🔹 AND 회로:", AND(a, b))
    st.write("🔹 OR 회로:", OR(a, b))
    st.write("🔹 NAND 회로:", NAND(a, b))

with col2:
    st.write("🔹 NOR 회로:", NOR(a, b))
    st.write("🔹 NOT 회로 (A 기준):", NOT(a))
    st.write("🔹 XOR 회로:", XOR(a, b))
