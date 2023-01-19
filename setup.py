from setuptools import setup

setup(
    name='today-google-calendar',
    description="GoogleCalendarから一日の予定を取得し、整形して表示する",
    version='1.1.0',
    install_requires=['httplib2', 'google-api-python-client', 'oauth2client', 'click', 'pyperclip'],
    packages=['src', 'src.google', 'src.config', 'src.credentials'],
    entry_points={
        'console_scripts': [
            'today-google-calendar=src.today_google_calendar:main',
        ],
    }
)
