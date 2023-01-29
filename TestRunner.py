import pytest
from datetime import datetime

configurations = {
    'headless': 'No',
    'browser': 'chromium',  # ['chromium', 'firefox', 'webkit']
    'tracing': 'Yes',
    'allure': 'Yes'
}

arguments = []

now = datetime.now()

if configurations['headless'] == "No":
    arguments.append('--headed')
arguments.extend(['--browser', configurations['browser']])
if configurations['tracing'] == "Yes":
    arguments.extend(['--tracing', 'on'])
if configurations['allure'] == 'Yes':
    arguments.append('--alluredir=./Reports/Allure/{:02d}{:02d}{:04d}/{:02d}{:02d}/allure-results'.format(
        now.day, now.month, now.year, now.hour, now.minute))

pytest.main(arguments)
