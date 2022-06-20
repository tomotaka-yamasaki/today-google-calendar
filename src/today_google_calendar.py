from src.google import calendar
from src.config import config
import os.path
import datetime
from datetime import timedelta
import argparse

def get_calendar(calendar_id):
    cred_dir = os.path.join(os.path.dirname(__file__), config.SA_KEY_PATH)
    return calendar.GoogleCalendar(calendar_id, cred_dir)

def output_oneday_calendar(calendar_id, dase_date):
    calendar = get_calendar(calendar_id)
    schedules = calendar.get_schedules(dase_date - timedelta(days=1), dase_date)

    print('## 【スケジュール】本日の予定')
    for schedule in schedules:
        print(schedule.output())

def main():
    # カレンダー取得範囲のデフォルト
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    date_type = lambda s: datetime.datetime.strptime(s, '%Y-%m-%d')

    # コマンドライン引数設定
    parser = argparse.ArgumentParser(description='Googleカレンダーから予定を取得する')
    parser.add_argument('-i', '--calendarId', default=config.CALENDAR_ID, help='取得したいGoogleカレンダーID')
    parser.add_argument('-d', '--today', type=date_type, default=today, help='予定の取得日 yyyy-mm-dd default:Today')

    args = parser.parse_args()
    output_oneday_calendar(args.calendarId, args.today)

if __name__ == '__main__':
    main()
