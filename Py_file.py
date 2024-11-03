import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
# Создание экземпляра Dash
app = dash.Dash(__name__)

# Данные о клиентской активности
data = {
    "Дата": [
        "2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05",
        "2023-01-06", "2023-01-07", "2023-01-08", "2023-01-09", "2023-01-10",
        "2023-01-11", "2023-01-12", "2023-01-13", "2023-01-14", "2023-01-15",
        "2023-01-16", "2023-01-17", "2023-01-18", "2023-01-19", "2023-01-20",
        "2023-01-21", "2023-01-22", "2023-01-23", "2023-01-24", "2023-01-25",
        "2023-01-26", "2023-01-27", "2023-01-28", "2023-01-29", "2023-01-30", "2023-01-31",
        "2023-02-01", "2023-02-02", "2023-02-03", "2023-02-04", "2023-02-05",
        "2023-02-06", "2023-02-07", "2023-02-08", "2023-02-09", "2023-02-10",
        "2023-02-11", "2023-02-12", "2023-02-13", "2023-02-14", "2023-02-15",
        "2023-02-16", "2023-02-17", "2023-02-18", "2023-02-19", "2023-02-20",
        "2023-02-21", "2023-02-22", "2023-02-23", "2023-02-24", "2023-02-25",
        "2023-02-26", "2023-02-27", "2023-02-28",
        "2023-03-01", "2023-03-02", "2023-03-03", "2023-03-04", "2023-03-05",
        "2023-03-06", "2023-03-07", "2023-03-08", "2023-03-09", "2023-03-10"
    ],
    "Авторизация": [
        "Да","Да",  "Нет", "Да", "Да",
        "Да", "Да", "Да", "Да", "Да",
        "Нет", "Да", "Да", "Да", "Да",
        "Да", "Да", "Да", "Нет", "Да",
        "Да", "Да", "Да", "Да", "Да",
        "Да", "Да", "Да", "Да", "Нет", "Да",

        "Да", "Да", "Да", "Да", "Да",
        "Да", "Да", "Нет", "Да", "Да",
        "Да", "Да", "Да", "Да", "Да",
        "Да", "Да", "Да", "Нет", "Да",
        "Да", "Да", "Да", "Да", "Да",
        "Да", "Да", "Нет",

        "Да", "Да", "Да", "Да", "Да",
        "Да", "Да", "Да", "Да", "Да"

    ],
    "Никнейм": [
        "ivan123", "maria456", "-", "pavel789", "ekaterina234",
        "ivan123", "maria456", "ekaterina234", "pavel789", "ivan123",
        "-", "maria456", "pavel789", "ekaterina234", "ivan123",
        "maria456", "pavel789", "ekaterina234", "-", "ivan123",
        "maria456", "pavel789", "ekaterina234",  "ivan123", "maria456",
        "pavel789", "ekaterina234",  "ivan123", "maria456", "-", "pavel789",

        "ivan123", "ekaterina234", "maria456", "pavel789", "ekaterina234",
        "ivan123", "maria456", "-", "pavel789", "ekaterina234",
        "ivan123", "maria456", "pavel789", "ekaterina234", "ivan123",
        "maria456", "pavel789", "ekaterina234", "-", "ivan123",
        "maria456", "pavel789", "ekaterina234",  "ivan123", "maria456",
        "pavel789",  "ekaterina234", "-",

        "ivan123", "maria456", "pavel789", "ekaterina234", "ivan123",
        "maria456", "pavel789", "ekaterina234",  "ivan123", "maria456"
    ],
    "Страница": [
        "Главная", "О нас", "Главная", "Контакты", "Главная",
        "Продукты", "Главная", "О нас", "Главная", "Контакты",
        "Главная", "Продукты", "Главная", "О нас", "Главная",
        "Продукты", "Главная", "Контакты", "Главная", "О нас",
        "Главная", "Контакты", "Главная", "Продукты", "Главная",
        "О нас", "Главная", "Контакты", "Главная", "Главная", "Главная",

        "О нас", "Главная", "Контакты", "Главная", "Продукты",
        "Главная", "О нас", "Контакты", "Главная", "Главная",
        "Контакты", "Главная", "Контакты", "Главная", "Продукты",
        "Главная", "Контакты", "Главная", "Контакты", "Продукты",
        "Главная", "Контакты", "Главная", "Продукты", "Главная",
        "Контакты", "Главная", "Контакты",

        "Продукты", "Главная", "Контакты", "Главная", "Продукты",
        "Главная", "Контакты", "Главная", "Продукты", "Главная"
    ],
    "Действие": [
        "Просмотр", "Просмотр", "Просмотр", "Просмотр", "Просмотр",
        "Просмотр", "Редактирование", "Скачивание", "Комментарий", "Просмотр",
        "Авторизация", "Редактирование", "Просмотр", "Комментарий", "Диавторизация",
        "Скачивание", "Редактирование", "Авторизация", "Смена пароля", "Просмотр",
        "Редактирование", "Комментарий", "Просмотр", "Скачивание", "Просмотр",
        "Редактирование", "Просмотр", "Комментарий","Авторизация", "Диавторизация", "Смена пароля",

        "Просмотр", "Просмотр", "Редактирование", "Просмотр", "Просмотр",
        "Редактирование", "Просмотр", "Комментарий", "Скачивание", "Просмотр",
        "Скачивание", "Редактирование", "Комментарий", "Просмотр", "Смена пароля",
        "Авторизация", "Редактирование", "Скачивание", "Комментарий", "Просмотр",
        "Редактирование", "Авторизация", "Просмотр", "Редактирование", "Просмотр",
        "Скачивание", "Редактирование", "Комментарий",

        "Просмотр", "Авторизация", "Редактирование", "Скачивание", "Комментарий",
        "Просмотр", "Редактирование", "Просмотр", "Скачивание", "Комментарий"
    ],
    'Время': [
        '10:05', '11:15', '09:30', '14:20', '16:45',
        '13:10', '10:35', '12:25', '15:30', '09:55',
        '08:40', '14:55', '11:10', '10:15', '09:20',
        '12:45', '14:55', '16:10', '10:30', '11:20',
        '09:40', '15:25', '12:15', '13:30', '14:45',
        '16:05', '09:50', '10:20', '08:55', '15:10', '11:30',

        '12:40', '10:25', '13:15', '14:20', '15:30',
        '16:40', '09:45', '11:55', '12:10', '10:05',
        '09:20', '10:30', '12:45', '14:55', '09:10',
        '10:25', '11:35', '13:45', '15:55', '09:15',
        '10:20', '11:30', '12:40', '13:50', '15:00',
        '16:10', '09:30', '10:45',

        '12:55', '14:05', '15:15', '09:05', '10:15',
        '11:25', '12:35', '13:45', '14:55', '16:05'
    ]
}

# Преобразование данных в DataFrame
df = pd.DataFrame(data)

# Преобразование столбца Дата в datetime
df['Дата'] = pd.to_datetime(df['Дата'])

# Создание графика активности пользователей по дням
activity_fig = px.histogram(df, x='Дата', color='Действие', title='Активность пользователей по дням')

# Создание графика количества действий по страницам
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

    #Радио - кнопки для выбора действия
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
