from PIL import Image
import streamlit as st
#st.header(')
profile_pic = "assets/Женя.jpg"
profile_pic = Image.open(profile_pic)

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Щуркин Евгений'"
PAGE_ICON = ":wave:"
NAME = "Щуркин Евгений"
DESCRIPTION = """
Data Scientist со страстью к NLP
"""
EMAIL = "shchurkin.evgeniy@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Telegram": "https://t.me/Shushch",
}
PROJECTS = {

}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.sidebar.success("Выберите проект выше")
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    # st.download_button(
    #     label=" 📄 Download Resume",
    #     data=PDFbyte,
    #     file_name=resume_file.name,
    #     mime="application/octet-stream",
    # )
    st.write("📫", EMAIL)
    st.write("✅", SOCIAL_MEDIA["Telegram"])

st.write('\n')
st.subheader("Навыки")
st.write(
    """
- ✔️ Хорошее индуктивное и логическое мышление
- ✔️ Строю интересные гипотезы и люблю инжинирить фичи
- ✔️ Много знаю про логические ошибки, а соответственно умею их избегать
"""
)# 
# --- SKILLS ---
st.write('\n')
st.subheader("Хард скиллы")
st.write(
    """
- 👩‍💻 Программирование: Python (Scikit-learn, Pandas), SQL, C#, С++
- 📊 Визуализация данных: MS Excel, Seaborn, Matplotlib, Plotly
- 📚 ML и NN модели: Линейные модели, Деревья решений, нейросети
- 📖 NLP: nltk, pymystem3
- 👁️ CV: YOLO, Detectron
"""
#- 🗄️ Базы данных: Postgres, MongoDB, MySQL
) # Добавить про математику
# --- WORK HISTORY ---
st.write('\n')
st.subheader("Опыт работы")
st.write("---")

# --- JOB 1
st.write('\n')
st.write("🚧", "**Data Scientist | Эльбрус Буткемп**")
st.write("05.2023 - 08.2023")
st.write(
    """
- ► Попал в топ 10% по датасету Титаник
- ► Сделал около 10 проектов. Начиная от ручной обработки и анализа табличных данных и заканчивая нейросетями для NLP и CV
- ► 
"""
)
# --- JOB 2
st.write("🚧", "**Старший менеджер по продажам | ВсеИнструменты.ру**")
st.write("10.2022 - 03.2023")
st.write(
    """
- ► Использовал Excel для анализа продаж год к году и продаж по категориям
- ► Организовал брейн-шторм на полсотни участников для генерации идей по увеличению KPI и проанализировал результаты
- ► Провёл опрос по желаемому графику работы магазинов и интерпретировал результаты
"""
) # Написать про аналитику во ВсеИнстументы
# Написать Толе с погони за офферами


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Проекты")
st.write("---")
"""
Слева можно посмотреть некоторые из моих проектов по CV и NLP
"""