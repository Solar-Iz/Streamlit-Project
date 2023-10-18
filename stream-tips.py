import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


st.title('Приложение по визуализации датасета ***tips.csv*** на платформе **Streamlit**')

path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(path, sep=',')

st.subheader('Гистограмма total_bill')

# Используем Plotly Express для создания гистограммы
fig = px.histogram(tips, x='total_bill', labels={'total_bill': 'Сумма счета', 'count': 'Частота'})

# Показать графику в Streamlit
st.plotly_chart(fig)

st.subheader('Связь между суммой счета и чаевыми')

fig = px.scatter(tips, x='total_bill', y='tip')
fig.update_xaxes(title='Сумма счета')
fig.update_yaxes(title='Чаевые')
st.plotly_chart(fig)

st.subheader('Связь между суммой счета, чаевыми и размером группы')
fig = px.scatter(tips, x='total_bill', y='tip', color='size', size='size')
fig.update_xaxes(title='Сумма счета (total_bill)')
fig.update_yaxes(title='Чаевые (tip)')
st.plotly_chart(fig)

st.subheader('Связь между днем недели и чаевыми')
fig = px.box(tips, x='day', y='total_bill', color='day')
fig.update_xaxes(title='День недели')
fig.update_yaxes(title='Сумма счета (total_bill)')
st.plotly_chart(fig)


st.subheader('Scatter plot с днем недели, чаевыми и цветом по полу')

# Определяем соответствие между категориями и цветами
# color_map = {'male': 'blue', 'female': 'pink'}
fig = px.scatter(tips, x='tip', y='day', color='sex', color_discrete_sequence=['pink','blue'])
fig.update_xaxes(title='Чаевые')
fig.update_yaxes(title='День недели')
st.plotly_chart(fig)

st.subheader('Box plot c суммой счетов по дням и времени')
fig = px.box(tips, x='day', y='total_bill', color='time')
fig.update_xaxes(title='День недели')
fig.update_yaxes(title='Сумма счета (total_bill)')
st.plotly_chart(fig)

st.subheader('Гистограммы чаевых на обед и ланч')
fig = px.histogram(tips, x='tip', color='time', facet_col='time', facet_col_wrap=2)
fig.update_xaxes(title='Чаевые, $')
fig.update_yaxes(title='Частота')
st.plotly_chart(fig)

st.subheader('Визуализация связи размера счета и чаевых для мужчин и женщин, дополнительно уточненная по курящим/некурящим.')
# Создание объекта FacetGrid
g = sns.FacetGrid(tips, col='sex', hue='smoker', height=6)

# Определение вида графика (scatterplot)
g.map(sns.scatterplot, 'total_bill', 'tip')

g.set_axis_labels('Размер счета, $', 'Чаевые, $')
g.add_legend(title='Курение')
st.pyplot(g)

st.subheader('''Визуализация ответа на ***свой*** вопрос к датасету.
             Интересно, больше оставляют чаевых курящие или не курящиие женщины,
             и в какой день недели(будни/выходные)?
             ''')
# Добавляем чекбокс для выбора пола
female_filter = st.checkbox("Показать только женщин", value=True)

# Создаем фильтрованный датафрейм на основе выбора чекбокса
if female_filter:
    filtered_tips = tips[(tips['sex'] == 'Female')]
else:
    filtered_tips = tips

# Создание объекта FacetGrid и настройка размера
g = sns.FacetGrid(filtered_tips, col='smoker', hue='day', height=6)

g.map(sns.scatterplot, 'day', 'tip')

g.set_axis_labels('День недели', 'Чаевые, $')
g.add_legend(title='День недели')
st.pyplot(g)
st.write('Курение у женщин никак не отражается на размер оставляемых чаевых, не заметила корреляции этих двух признаков.')
