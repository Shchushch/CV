import streamlit as st
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch


DEVICE = 'cpu'


st.set_page_config(
    page_title="Генератор анекдотов",
    page_icon="🤡",
    layout="wide",
)
st.title('Генератор анекдотов')

@st.cache_resource
def load_model():
    model = GPT2LMHeadModel.from_pretrained(
        'sberbank-ai/rugpt3small_based_on_gpt2',
        output_attentions = False,
        output_hidden_states = False,
    )

    # Вешаем сохраненнки весов на нашу модель
    model.load_state_dict(torch.load('assets/aneks_model.pt',map_location=DEVICE))
    return model.to(DEVICE)
model = load_model()
with st.expander("Пояснения"):
    """
    #### Это генератор анекдотов

    Немного технической информации:
    Здесь используется нейросеть модель **rugp3small_based_on_gpt2** обученная Сбером. Я дообучил её на датасете из 2220 категории Б.
    Кроме тех параметров, которые можно регулировать в интерфейсе заданы do_sample=True, early_stopping=True, остальное оставил дефолтным, т.к. это привело меня к лучшему результату
    """

# Вешаем сохраненные веса на нашу модель
#model.load_state_dict(torch.load('resources/model.pt',map_location=DEVICE))
model_name='sberbank-ai/rugpt3small_based_on_gpt2'
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
tokenizer.pad_token_id = tokenizer.eos_token_id

input=st.text_area('Введи промт для генерации анека',value="Заходит бесконечное число математиков в бар", key='input')
num_aneks= st.number_input('Количество анеков',min_value=1,max_value=5,value=3)

token_nums= st.number_input('Максимум токенов вывода',min_value=1,max_value=500,value=200)
with st.expander("А что такое токен?"):
    """
    Токен в контексте обработки естественного языка (Natural Language Processing, NLP) - это кусочек текста, который является частью большего текста. Токены могут быть очень короткими, например, отдельным символом, или более длинными, представляя собой целое слово или даже несколько слов.

    Давайте рассмотрим несколько примеров:

    1. В слове "кошка" есть 6 символов, и каждый символ может считаться токеном (к, о, ш, к, а).

    2. В предложении "Я люблю кошек" токенами могут быть каждое слово: "Я", "люблю", "кошек".

    3. В случае работы с буквами, каждая буква может считаться токеном. Например, в слове "HELLO" будут пять токенов: "H", "E", "L", "L", "O".

    Когда мы говорим о токенах в машинном обучении, особенно в нейронных сетях для обработки текста, мы часто имеем в виду минимальные единицы, с которыми модель работает. В тексте каждое слово или символ обычно преобразуется в числовое представление, называемое токеном, чтобы модель могла эффективно обрабатывать текстовую информацию.

    Конкретно в этом случае токеном считается слово или знак препинания, заканчивающий предложение
    """

length=st.number_input('Наказание за длину',min_value=0.0,max_value=10.0,value=0.2)
with st.expander("А как это?"):
    """
    Коэффициент штрафа за длину, который управляет предпочтением более коротких или более длинных ответов. Значение length_penalty < 1.0 предпочитает более короткие ответы, а значение > 1.0 предпочитает более длинные ответы.
    Общие значения для length_penalty могут варьироваться от 0.0 до положительного бесконечности. Различные значения могут оказывать разное влияние на результат:
    - length_penalty = 1.0: Нейтральный эффект на выбор длины ответа.
    - length_penalty < 1.0: Модель будет предпочитать генерировать более короткие ответы.
    - length_penalty > 1.0: Модель будет предпочитать генерировать более длинные ответы.
    """

temp_num=st.number_input('Ввод температуры',min_value=0.1,max_value=5.0,value=0.5)
with st.expander("А это что такое?"):
    """
    Когда мы говорим о "температуре" в контексте генерации текста с использованием нейронных сетей, таких как GPT, это относится к параметру, который влияет на случайность и разнообразие ответов модели.

    Простыми словами, температура контролирует, насколько "сумасшедшие" или "предсказуемые" будут ответы. Вы можете представить это как настройку, которая регулирует, насколько вероятность различия между предсказаниями модели.

    - **Высокая температура (например, 1.5):**
    - Большая случайность в ответах.
    - Модель может генерировать неожиданные и креативные тексты.
    - Ответы могут быть менее связанными с контекстом.

    - **Низкая температура (например, 0.5):**
    - Меньшая случайность, более предсказуемые ответы.
    - Модель склонна использовать более типичные и "осмысленные" фразы.
    - Ответы более связаны с контекстом.

    Итак, регулировка температуры помогает вам контролировать баланс между творчеством и структурой в генерируемых текстах."""

def generator(prompt, max_new_tokens=token_nums, temperature=temp_num, num_aneks=num_aneks,length_penalty=length):
    # Предполагается, что у вас уже есть определения model, tokenizer и DEVICE

    prompt = tokenizer.encode(prompt, return_tensors='pt', truncation=True).to(DEVICE)

    aneks = model.generate(
        input_ids=prompt,
        do_sample=True,
        temperature=temperature,

        num_return_sequences=num_aneks,
        max_length=max_new_tokens,
        length_penalty=length_penalty,
        early_stopping=True
    ).cpu().numpy()

    # Используем строковый токенизатор для декодирования
    out_list = [tokenizer.decode(seq, skip_special_tokens=True).split("\n")[0] for seq in aneks]

    return out_list

if "generated_text" not in st.session_state:
    st.session_state.generated_text = ""
if "disabled" not in st.session_state:
    st.session_state.disabled = False

def show_anekdot_generator():
    rad= st.empty()
    butt= st.empty()
    
    age_confirmation = rad.radio("Вам есть 18 лет?", ("Да", "Нет"))
    
    submit =butt.button("Подтвердить")
    
    if submit:
        if age_confirmation == "Да":
            # Если пользователь подтвердил, что ему 18
            st.session_state.disabled = True
            

        elif age_confirmation == "Нет":
            # Если пользователь ответил "Нет"
            
            st.write("Вы не достигли 18 лет. Вас переадресовывают...")
            st.markdown('<meta http-equiv="refresh" content="0;URL=\'https://www.youtube.com/watch?v=V8Er1uk4fcw\'" />', unsafe_allow_html=True)
        rad.empty() 
        butt.empty()
        
if not st.session_state.disabled:
    show_anekdot_generator()
if st.session_state.disabled:
    generate_anek_button = st.button("Генерировать анек",key='gen')


    if st.session_state.gen:
        st.session_state.generated_text = ""
        out= generator(input)
        for out_ in out:
            st.session_state.generated_text += out_+'\n\n'

        st.session_state.generated_text


