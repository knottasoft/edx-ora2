"""Default data initializations for the XBlock, with formatting preserved."""
# pylint: disable=line-too-long

DEFAULT_PROMPT = """
    Цензура в библиотеках

    'Каждый из нас может вспомнить книгу, которую, как мы надеемся, никто из наших детей или других детей не взял с полки. Но если я имею право убрать с полки эту книгу - то есть то произведение, которое мне отвратительно, - то и вы имеете точно такое же право, и все остальные тоже. И тогда на полке не останется книг ни для кого из нас'. --Кэтрин Патерсон, автор

    Напишите убедительное эссе для газеты, отражающее ваши взгляды на цензуру в библиотеках. Считаете ли вы, что определенные материалы, такие как книги, музыка, фильмы, журналы и т.д., должны убираться с полок, если они признаны оскорбительными? Подкрепите свою позицию убедительными аргументами из собственного опыта, наблюдений и/или прочитанного.

    Читайте для краткости, ясности мысли и формы.
"""  # nopep8

DEFAULT_RUBRIC_CRITERIA = [
    {
        'name': "Идеи",
        'label': "Идеи",
        'prompt': "Определите, есть ли объединяющая тема или главная идея.",
        'order_num': 0,
        'feedback': 'optional',
        'options': [
            {
                'order_num': 0, 'points': 0, 'name': 'Плохо', 'label': 'Плохо',
                'explanation': """Читателю трудно выделить главную идею.  Слишком краткое или слишком повторяющееся изложение, чтобы установить или удержать внимание."""  # nopep8
            },
            {
                'order_num': 1, 'points': 3, 'name': 'Неплохо', 'label': 'Неплохо',
                'explanation': """Представляет объединяющую тему или главную идею, но может включать незначительные отступления.  В некоторой степени концентрируется на теме и задаче."""  # nopep8
            },
            {
                'order_num': 2, 'points': 5, 'name': 'Хорошо', 'label': 'Хорошо',
                'explanation': """Представляет объединяющую тему или главную идею, не уклоняясь в сторону.  Остается полностью сосредоточенным на теме и задаче."""  # nopep8
            },
        ],
    },
    {
        'name': "Содержание",
        'label': "Содержание",
        'prompt': "Оцените содержание представленного материала",
        'order_num': 1,
        'options': [
            {
                'order_num': 0, 'points': 0, 'name': 'Плохо', 'label': 'Плохо',
                'explanation': """Содержит мало информации с небольшим количеством деталей или вообще без них или с несвязанными деталями.  Неудачные попытки исследовать какие-либо аспекты темы."""  # nopep8
            },
            {
                'order_num': 1, 'points': 1, 'name': 'Неплохо', 'label': 'Неплохо',
                'explanation': """Содержит мало информации и мало или совсем нет деталей.  Исследует только один или два аспекта темы."""  # nopep8
            },
            {
                'order_num': 2, 'points': 3, 'name': 'Хорошо', 'label': 'Хорошо',
                'explanation': """Включает достаточное количество информации и вспомогательных деталей. (Детали могут быть не полностью проработаны; идеи могут быть перечислены). Исследует некоторые аспекты темы."""  # nopep8
            },
            {
                'order_num': 3, 'points': 5, 'name': 'Отлично', 'label': 'Отлично',
                'explanation': """Включает глубокую информацию и исключительные вспомогательные детали, которые полностью проработаны.  Исследует все аспекты темы."""  # nopep8
            },
        ],
    },
]

# The rubric's feedback prompt is a set of instructions letting the student
# know they can provide additional free form feedback in their assessment.
DEFAULT_RUBRIC_FEEDBACK_PROMPT = """
(Необязательно) Какие аспекты этого ответа привлекли ваше внимание? Что в нем было сделано хорошо? Как его можно улучшить?
"""

# The rubric's feedback text is the default text displayed and used as
# the student's response to the feedback prompt
DEFAULT_RUBRIC_FEEDBACK_TEXT = """
Я думаю, что этот ответ...
"""

DEFAULT_EXAMPLE_ANSWER = (
    "Замените этот текст своим собственным образцом ответа для этого задания. "
    "Затем в разделе Оценка ответа справа выберите вариант для каждого критерия. "
    "Обучающиеся практикуются в выполнении взаимных оценок, оценивая этот ответ и сравнивая его "
    "варианты, которые они выбирают в рубрике, с вариантами, которые вы указали."
)

DEFAULT_EXAMPLE_ANSWER_2 = (
    "Замените этот текст другим образцом ответа, "
    "а затем укажите варианты, которые вы выбрали бы для этого ответа."
)

DEFAULT_STUDENT_TRAINING = {
    "name": "student-training",
    "start": None,
    "due": None,
    "examples": [
        {
            "answer": DEFAULT_EXAMPLE_ANSWER,
            "options_selected": [
                {
                    "criterion": "Идеи",
                    "option": "Неплохо"
                },
                {
                    "criterion": "Содержание",
                    "option": "Хорошо"
                }
            ]
        },
        {
            "answer": DEFAULT_EXAMPLE_ANSWER_2,
            "options_selected": [
                {
                    "criterion": "Идеи",
                    "option": "Плохо"
                },
                {
                    "criterion": "Содержание",
                    "option": "Хорошо"
                }
            ]
        }
    ]
}

DEFAULT_START = "2001-01-01T00:00"
DEFAULT_DUE = "2029-01-01T00:00"

# The Default Peer Assessment is created as an example of how this XBlock can be
# configured. If no configuration is specified, this is the default assessment
# module(s) associated with the XBlock.
DEFAULT_PEER_ASSESSMENT = {
    "name": "peer-assessment",
    "start": DEFAULT_START,
    "due": DEFAULT_DUE,
    "must_grade": 5,
    "must_be_graded_by": 3,
    "enable_flexible_grading": False,
    "flexible_grading_days": 7,
    "flexible_grading_graded_by_percentage": 30
}

DEFAULT_SELF_ASSESSMENT = {
    "name": "self-assessment",
    "start": DEFAULT_START,
    "due": DEFAULT_DUE,
}

DEFAULT_STAFF_ASSESSMENT = {
    "name": "staff-assessment",
    "start": DEFAULT_START,
    "due": DEFAULT_DUE,
    "required": False,
}

ACTIVE_STAFF_ASSESSMENT = {
    "name": "staff-assessment",
    "start": DEFAULT_START,
    "due": DEFAULT_DUE,
    "required": True,
}

DEFAULT_ASSESSMENT_MODULES = [
    DEFAULT_STUDENT_TRAINING,
    DEFAULT_PEER_ASSESSMENT,
    DEFAULT_SELF_ASSESSMENT,
    DEFAULT_STAFF_ASSESSMENT,
]

DEFAULT_EDITOR_ASSESSMENTS_ORDER = [
    "student-training",
    "peer-assessment",
    "self-assessment",
    "staff-assessment",
]

BLANK_ASSESSMENT_MODULES = []

SELF_ASSESSMENT_MODULES = [
    DEFAULT_SELF_ASSESSMENT,
]

PEER_ASSESSMENT_MODULES = [
    DEFAULT_STUDENT_TRAINING,
    DEFAULT_PEER_ASSESSMENT,
]

STAFF_ASSESSMENT_MODULES = [
    ACTIVE_STAFF_ASSESSMENT,
]

SELF_TO_PEER_ASSESSMENT_MODULES = [
    DEFAULT_STUDENT_TRAINING,
    DEFAULT_SELF_ASSESSMENT,
    DEFAULT_PEER_ASSESSMENT,
]

SELF_TO_STAFF_ASSESSMENT_MODULES = [
    DEFAULT_SELF_ASSESSMENT,
    ACTIVE_STAFF_ASSESSMENT,
]
