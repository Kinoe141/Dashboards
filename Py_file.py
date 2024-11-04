import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Создание экземпляра Dash
app = dash.Dash(__name__)

# Загрузка данных из CSV файла с Google Drive
url = "https://drive.google.com/uc?id=1IkfyKEo_U-Ii-_lllmwEmO6fQsHlZIX4"
df = pd.read_csv(url, encoding='utf-8')  # Чтение файла с русскими символами

# Удаление лишних пробелов из названий столбцов
df.columns = df.columns.str.strip()

# Преобразование столбца Дата в datetime
df['Дата'] = pd.to_datetime(df['Дата'])

# Создание графиков для отображения на дашборде
activity_fig = px.histogram(df, x='Дата', color='Действие', title='Активность пользователей по дням')
page_actions_fig = px.histogram(df, x='Страница', color='Действие', title='Количество действий по страницам')

# Определение макета дашборда
app.layout = html.Div(children=[
    html.H1(children='Дашборд анализа клиентской активности'),

    # Выпадающий список для выбора никнеймов (множественный выбор)
    dcc.Dropdown(
        id='nickname-dropdown',
        options=[{'label': nickname, 'value': nickname} for nickname in df['Никнейм'].unique()],
        value=['ivan123'],  # Установить значение по умолчанию как список
        multi=True,  # Разрешить множественный выбор
        placeholder="Выберите никнеймы"
    ),

    # Выбор диапазона дат
    dcc.DatePickerRange(
        id='date-picker-range',
        start_date=df['Дата'].min(),
        end_date=df['Дата'].max(),
        display_format='YYYY-MM-DD'
    ),

    # Радио-кнопки для выбора действия
    dcc.RadioItems(
        id='action-radio',
        options=[
            {'label': 'Все действия', 'value': 'Все'},
            {'label': 'Просмотр', 'value': 'Просмотр'},
            {'label': 'Редактирование', 'value': 'Редактирование'},
            {'label': 'Скачивание', 'value': 'Скачивание'},
            {'label': 'Комментарий', 'value': 'Комментарий'},
            {'label': 'Авторизация', 'value': 'Авторизация'},
            {'label': 'Диавторизация', 'value': 'Диавторизация'}
        ],
        value='Все',
        labelStyle={'display': 'inline-block'}
    ),

    # Ползунок для выбора диапазона времени
    dcc.Slider(
        id='time-slider',
        min=0,
        max=24,
        step=1,
        value=12,
        marks={i: f'{i}:00' for i in range(0, 25)},
        tooltip={"placement": "bottom", "always_visible": True}
    ),

    # Графики для отображения данных
    dcc.Graph(
        id='activity-over-time',
        figure=activity_fig
    ),

    dcc.Graph(
        id='page-actions',
        figure=page_actions_fig
    )
])


# Обновление графиков на основе выбранных фильтров
@app.callback(
    [Output('activity-over-time', 'figure'),
     Output('page-actions', 'figure')],
    [Input('nickname-dropdown', 'value'),
     Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date'),
     Input('action-radio', 'value'),
     Input('time-slider', 'value')]
)
def update_graph(selected_nicknames, start_date, end_date, selected_action, selected_time):
    filtered_df = df[
        (df['Никнейм'].isin(selected_nicknames)) &  # Фильтрация по множеству никнеймов
        (df['Дата'] >= start_date) &
        (df['Дата'] <= end_date)
        ]

    if selected_action != 'Все':
        filtered_df = filtered_df[filtered_df['Действие'] == selected_action]

    # Фильтрация по времени (если необходимо)

    filtered_df['Час'] = filtered_df['Время'].apply(lambda x: int(x.split(':')[0]))

    filtered_df = filtered_df[filtered_df['Час'] <= selected_time]

    activity_fig = px.histogram(filtered_df, x='Дата', color='Действие',
                                title='Активность пользователей по дням')

    page_actions_fig = px.histogram(filtered_df, x='Страница', color='Действие',
                                    title='Количество действий по страницам')

    return activity_fig, page_actions_fig


# Запуск приложения
if __name__ == '__main__':
    app.run_server(debug=True)