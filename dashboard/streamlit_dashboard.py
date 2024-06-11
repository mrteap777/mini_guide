import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import time
from datetime import datetime


# Функция для установки состояния сессии
def update_session_state():
    if 'counter' not in st.session_state:
        st.session_state.counter = 0

    if st.button('Увеличить счетчик'):
        st.session_state.counter += 1


# Заголовок приложения
st.title('Мой Расширенный Дашборд на Streamlit')


# Текстовые элементы
st.header('Этот дашборд демонстрирует все основные элементы Streamlit')
st.subheader('Текстовые элементы')
st.text('Здесь отображается обычный текст.')
st.markdown('**Здесь отображается маркированный текст.**')
st.caption('Это подпись к изображению или тексту.')
st.code('print("Hello, World!")', language='python')
st.latex(r''' e^{i\pi} + 1 = 0 ''')


# Элементы ввода
user_input = st.text_input("Введите что-нибудь:")
number_input = st.number_input("Введите число:")
text_area_input = st.text_area("Введите много текста:")
date_input = st.date_input("Выберите дату:")
time_input = st.time_input("Выберите время:")
slider_input = st.slider("Выберите значение на слайдере", 0, 100, 50)
select_slider_input = st.select_slider("Выберите значение на слайдере", options=['A', 'B', 'C'])
option = st.selectbox('Выберите опцию:', ['Опция 1', 'Опция 2', 'Опция 3'])
multi_select = st.multiselect('Выберите несколько опций:', ['Опция 1', 'Опция 2', 'Опция 3'])
checkbox_input = st.checkbox('Отметьте этот чекбокс')
radio_input = st.radio("Выберите вариант:", ('Вариант A', 'Вариант B', 'Вариант C'))
uploaded_file = st.file_uploader("Загрузите файл")
color_picker = st.color_picker('Выберите цвет:', '#00f900')


# Боковая панель
st.sidebar.header('Боковая панель')

# Элементы на боковой панели
sidebar_user_input = st.sidebar.text_input("Введите что-нибудь на боковой панели:")
sidebar_number_input = st.sidebar.number_input("Введите число на боковой панели:")
sidebar_text_area_input = st.sidebar.text_area("Введите много текста на боковой панели:")
sidebar_date_input = st.sidebar.date_input("Выберите дату на боковой панели:")
sidebar_time_input = st.sidebar.time_input("Выберите время на боковой панели:")
sidebar_slider_input = st.sidebar.slider("Выберите значение на слайдере на боковой панели", 0, 100, 50)
sidebar_select_slider_input = st.sidebar.select_slider("Выберите значение на слайдере на боковой панели", options=['A', 'B', 'C'])
sidebar_option = st.sidebar.selectbox('Выберите опцию на боковой панели:', ['Опция 1', 'Опция 2', 'Опция 3'])
sidebar_multi_select = st.sidebar.multiselect('Выберите несколько опций на боковой панели:', ['Опция 1', 'Опция 2', 'Опция 3'])
sidebar_checkbox_input = st.sidebar.checkbox('Отметьте этот чекбокс на боковой панели')
sidebar_radio_input = st.sidebar.radio("Выберите вариант на боковой панели:", ('Вариант A', 'Вариант B', 'Вариант C'))
sidebar_uploaded_file = st.sidebar.file_uploader("Загрузите файл на боковой панели")
sidebar_color_picker = st.sidebar.color_picker('Выберите цвет на боковой панели:', '#00f900')


# Прогресс-бар
progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress_bar.progress(i + 1)


# Спиннер
with st.spinner('Подождите...'):
    time.sleep(2)
st.success('Готово!')


# Элемент отображения данных: Таблица
data = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)
st.table(data)


# Элемент отображения данных: Диаграмма (используем Altair)
chart_data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)
chart = alt.Chart(chart_data).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)
st.altair_chart(chart, use_container_width=True)


# Элемент отображения данных: Карта
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_data)


# Элемент отображения данных: Картинка
st.image("https://static.streamlit.io/examples/dog.jpg", caption='Пример изображения')


# Элемент отображения данных: Видео
st.video("https://www.youtube.com/watch?v=Jj6yXxVc21Y")


# Элемент отображения данных: Аудио
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")


# Элемент ввода: Скачивание файла
csv = data.to_csv().encode('utf-8')
st.download_button(
    label="Скачать данные в CSV",
    data=csv,
    file_name='data.csv',
    mime='text/csv',
)


# Текстовые элементы: Сообщения
st.success('Дашборд успешно создан!')
st.error('Это пример ошибки.')
st.warning('Это предупреждение.')
st.info('Это информационное сообщение.')


# Исключение
try:
    1 / 0
except ZeroDivisionError as e:
    st.exception(e)


# Элемент отображения данных: Метрика
st.metric(label="Температура", value="70 °F", delta="1.2 °F")


# Элемент отображения данных: JSON
st.json({
    'foo': 'bar',
    'baz': 'qux'
})


# Состояние сессии
update_session_state()
st.write("Счётчик состояния сессии: ", st.session_state.counter)


# Временные ряды
date_range = pd.date_range(start='1/1/2020', periods=100)
time_series_data = pd.DataFrame(np.random.randn(100, 1), index=date_range, columns=['value'])
st.line_chart(time_series_data)


# Анимация
st.write('Анимация')
for i in range(5):
    st.write(f'Итерация {i}')
    time.sleep(0.1)


# Контакты
st.write('Контакты: [Email](mailto:example@example.com)')


# Модули в расширенных библиотеках (Plotly)
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')
st.plotly_chart(fig)


# Аннотированный текст
st.write('Аннотированный текст:')
st.markdown("""
### Markdown заголовок
- список 1
- список 2
""")
