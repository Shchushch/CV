import streamlit as st
from PIL import Image
from assets.imagenet import img_class
import requests
from io import BytesIO
st.set_page_config(
    page_title="Распознаватель изображений",
    page_icon="🖼️",
    layout="wide",
)
st.title('Распознаватель изображений')

with st.expander("Пояснения"):
    """
    #### Нейросеть опознаёт, что изображено на картинке

    Немного технической информации:
    
    Используется нейросеть **inception_v3** с точностью **78.1%** на датасете [imagenet](https://www.image-net.org/). Никаких изменений не внесено, просто добавлен пользовательский интерфейс.
    """

upload_method = st.radio("Выбери метод загрузки", ["Файл", "URL"],key='method')
  
if st.session_state['method'] == "Файл":
    uploaded_file=st.file_uploader('# Загрузи сюда любую картинку',type=["jpg", "jpeg", "png","svg"],key='uploader')
    if uploaded_file is not None:
        st.image(uploaded_file)
        image = Image.open(uploaded_file)

elif st.session_state['method'] == "URL":
    
    pic_url=st.text_input('Или вставь сюда ссылку на картинку',key='urls')
    if pic_url != '':
        try:
            image = Image.open(requests.get(pic_url, stream=True).raw)
            st.image(image, caption="Изображение по URL")
        except:
            st.error('Не удалось загрузить картинку')
# try:        
if st.button('Определить'):
    #st.write(image)
    # st.image(image, caption='Uploaded Image', use_column_width=True)
    st.success(img_class(image))
# except:
#     st.error('Не удалось обработать картинку')