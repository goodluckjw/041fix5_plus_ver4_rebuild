
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from utils.xml_parser import parse_law_xml

st.title("부칙 개정 도우미")
st.write("법령 본문 중 검색어를 포함하는 조문을 찾아줍니다.")

# 설명 및 입력창
st.text("예시: A & B , C -D → A와 B가 모두 포함되거나 C 포함, D는 제외")
search_query = st.text_input("🔍 찾을 검색어 (다중 검색 지원)", key="search_term")

# 조/항/선택없음 필터
unit = st.radio("검색 단위", ["조", "항", "선택 없음"], horizontal=True)

# 초기화 버튼
if st.button("초기화"):
    st.experimental_rerun()

# 검색 버튼
if st.button("법률 검색"):
    if not search_query:
        st.warning("검색어를 입력해 주세요.")
    elif not os.path.exists("./data"):
        st.error("⚠ './data' 디렉토리를 찾을 수 없습니다.")
    else:
        st.info(f"‘{search_query}’(을)를 포함하는 조문을 검색 중입니다...")
        for file in os.listdir("./data"):
            if file.endswith(".xml"):
                path = os.path.join("./data", file)
                try:
                    results = parse_law_xml(path, search_query, unit)
                    if results:
                        with st.expander(f"📘 {file}"):
                            for r in results:
                                st.markdown(r, unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"❌ {file} 처리 중 오류 발생: {e}")
