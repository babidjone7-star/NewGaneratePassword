import streamlit as st
import requests

res = 0
Password = ""
data = 0
url = "http://127.0.0.1:8000/generator"
class generate():
  def __init__(self):
    global data
    global res
    st.title("Рандом генератор паролей...")
    st.write("Нажмите на кнопку и сгенерируйте пароль")
    if st.button("Получить данные"):
      res = requests.get(url)
      data = res.json
      st.write(data())
      st.json(data)
gener = generate()
st.divider()
      