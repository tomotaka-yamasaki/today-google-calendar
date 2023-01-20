import datetime
import os.path
import pickle

from dateutil import parser
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client.service_account import ServiceAccountCredentials


class Event:
    def __init__(self, title, start, end):
        self.title = title
        self.start = start
        self.end = end

    def output(self):
        return f"- {self.start.strftime('%H:%M')} ~ {self.end.strftime('%H:%M')} : {self.title}"


class GoogleCalendar:
    def __init__(self, calendar_id, cred_dir):
        self.service = self.authorize_service(cred_dir)
        self.calendar_id = calendar_id

    def authorize_service(self, cred_dir):
        scopes = ["https://www.googleapis.com/auth/calendar.readonly"]

        creds = None
        pickle_path = os.path.join(cred_dir, "token.pickle")
        if os.path.exists(pickle_path):
            with open(pickle_path, "rb") as token:
                creds = pickle.load(token)
        if not creds:
            # credentials.json was created by GCP service account
            cred_path = os.path.join(cred_dir, "credentials.json")
            creds = ServiceAccountCredentials.from_json_keyfile_name(cred_path, scopes=scopes)
            with open(pickle_path, "wb") as token:
                pickle.dump(creds, token)

        http_auth = creds.authorize(Http())
        service = build("calendar", "v3", http=http_auth)
        return service

    def get_schedules(self, start, end):
        time_min = datetime.datetime(start.year, start.month, start.day, 15, 0, 0).isoformat() + "Z"
        time_max = datetime.datetime(end.year, end.month, end.day, 14, 59, 59).isoformat() + "Z"

        events_result = (
            self.service.events()
            .list(
                calendarId=self.calendar_id, timeMin=time_min, timeMax=time_max, singleEvents=True, orderBy="startTime"
            )
            .execute()
        )
        events = events_result.get("items", [])

        jst = datetime.timezone(datetime.timedelta(hours=+9), "JST")
        schedules = []
        for event in events:
            iso_start = event["start"].get("dateTime")
            if iso_start is None:
                continue
            start = parser.parse(iso_start).astimezone(jst)
            iso_end = event["end"].get("dateTime")
            end = parser.parse(iso_end).astimezone(jst)

            schedules.append(Event(event["summary"], start, end))

        return schedules
