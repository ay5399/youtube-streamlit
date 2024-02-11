import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done!!'

# left_column, right_column = st.beta_columns(2)
# button = left_column.button('右からカラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')

# expander1 = st.beta_expander('問合せ１')
# expander1.write('問合せ１の内容を書く')

text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味は、', text, 'です。'

condition = st.slider('あなたの今の調子は？',0,100,50)
'あなたのコンディションは、', condition, 'です。'


# if st.checkbox('Show Image'):
#     img = Image.open('1.gif')
#     st.image(img, caption='test',use_column_width=True)
