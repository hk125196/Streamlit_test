import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image


st.title("Streamlit 超入門")

"プログレスバー"
"Start!"
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration:{i+1}")
    bar.progress(i+1)
    time.sleep(0.01)
"Finish!"


st.write("DataFrame")

df = pd.DataFrame({
    "1列目":[1,2,3,4],
    "2列目":[10,20,30,40]
})

st.dataframe(df.style.highlight_max(axis=0))

st.write("Table")
st.table(df)

"""

# 章
## 節
### 項

```python

import streamlit

```

"""

df2 = pd.DataFrame(
    np.random.rand(20,3),
    columns=["a","b","c"]
)

st.line_chart(df2)
st.area_chart(df2)
st.bar_chart(df2)

df3 = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=["lat","lon"]
)
st.map(df3)


st.write("Display Image")

if st.checkbox("Show Dog"):
    img = Image.open("dog.jpg")
    st.image(img,caption="Dog", use_container_width=True)

option = st.selectbox(
    "好きな数字は？",
    list(range(1,11))
)

"あなたの好きな数字は",option,"です"

"インタラクティブなウィジェット"

left_column,right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

expander = st.expander("問い合わせ")
expander.write("問い合わせへの回答")

"←Sidebar"
option2 = st.sidebar.text_input("趣味は？")
"あなたの好きなことは",option2,"です"
"←Sidebar"
conditon = st.sidebar.slider("今の調子",0,100,50)
"condition:",conditon

