import streamlit as st
from PIL import Image
from assets.skin import get_evil
import requests
st.set_page_config(
    page_title="Это рак?",
    page_icon="♋",
    layout="wide",
    #initial_sidebar_state="expanded"
)
st.title('Это рак?')
with st.expander("Пояснения"):
    """
    #### Эта программа использует нейросеть чтобы определить, является ли кожное образование доброкачественным или злокачественным.

    Немного технической информации:

    Используется нейросеть **VGG_19_BN** дообученная на 660 фотографиях новообразований в течение **4 эпох**. **Точность** предсказания: **0.8327**
    """
"""Данные для обучения я брал [отсюда](https://www.kaggle.com/datasets/fanconic/skin-cancer-malignant-vs-benign), так что можно использовать их же для проверки работы программы, хоть это и не совсем чесно."""

upload_method = st.radio("Выбери метод загрузки", ["Файл", "URL"],key='method')
image = None  
if st.session_state['method'] == "Файл":
    uploaded_file=st.file_uploader('Загрузи сюда картинку новообразования',type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image')
        

elif st.session_state['method'] == "URL":
    pic_url=st.text_input('Или вставь сюда ссылку на картинку',key='urls')
    if pic_url != '':
        try:
            image = Image.open(requests.get(pic_url, stream=True).raw)
            st.image(image)
        except:
            st.error('Не удалось загрузить картинку')

if image is not None and st.button('Это что'):
    st.success(get_evil(image))