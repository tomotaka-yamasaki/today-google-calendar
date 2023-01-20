import datetime
import os.path
from datetime import timedelta

import click
import pyperclip
from config.config import Config
from lib.google.calendar import GoogleCalendar


def get_calendar(calendar_id):
    cred_dir = os.path.join(os.path.dirname(__file__), Config.SA_KEY_PATH)
    return GoogleCalendar(calendar_id, cred_dir)


@click.command()
@click.option("--calendar-id", "-i", type=str, default=Config.CALENDAR_ID, help="取得したいGoogleカレンダーID")
@click.option(
    "--date",
    "-d",
    type=click.DateTime(["%Y-%m-%d", "%Y/%m/%d"]),
    default=datetime.datetime.today().strftime("%Y-%m-%d"),
    help="予定の取得日 (yyyy-mm-dd or yyyy/mm/dd) default:Today",
)
def output_oneday_calendar(calendar_id, date):
    calendar = get_calendar(calendar_id)
    schedules = calendar.get_schedules(date - timedelta(days=1), date)

    schedule_texts = [schedule.output() for schedule in schedules]
    output_texts = ["## 【スケジュール】本日の予定"]
    output_texts.extend(schedule_texts)
    output_text = "\n".join(output_texts)

    print(output_text)
    pyperclip.copy(output_text)


def main():
    output_oneday_calendar()


if __name__ == "__main__":
    main()
