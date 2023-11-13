from google.oauth2 import service_account
from googleapiclient.discovery import build


class GoogleCalendar:
    SCOPES = ["https://www.googleapis.com/auth/calendar"]
    FILE_PATH = "grand-appliance-403520-b06ed9fdb088.json"

    def __init__(self):
        # Определение областей видимости и .json-файла для учетной записи службы google
        credentials = service_account.Credentials.from_service_account_file(
            filename=self.FILE_PATH, scopes=self.SCOPES
        )
        # Авторизация в учетной записи службы google
        self.service = build("calendar", "v3", credentials=credentials)

    # Список календарей
    def get_calendar_list(self):
        return self.service.calendarList().list().execute()

    # Создание календаря
    def add_calendar(self, calendar_id):
        calendar_list_entry = {"id": calendar_id}
        return self.service.calendarList().insert(body=calendar_list_entry).execute()

    # Получение списка событий на выбранную дату
    def get_event_by_date(self, calendar_id, date):
        events_result = (
            self.service.events()
            .list(
                calendarId=calendar_id,
                timeMin=date + "T00:00:00Z",
                timeMax=date + "T23:59:59Z",
            )
            .execute()
        )
        return events_result.get("items", [])

    # Добавление события
    def add_event(
        self,
        calendar_id,
        summary,
        start_date,
        end_date,
    ):
        event = {
            "summary": summary,
            "start": {
                "date": start_date,
                "timeZone": "Europe/Moscow",
            },
            "end": {
                "date": end_date,
                "timeZone": "Europe/Moscow",
            },
        }

        return (
            self.service.events().insert(
                calendarId=calendar_id, body=event).execute()
        )

    # Удаление события
    def delete_evente(self, calendar_id, event_name):
        events_result = self.service.events().list(calendarId=calendar_id).execute()
        events = events_result.get("items", [])

        # Поиск события по названию
        for event in events:
            if event.get("summary") == event_name:
                # Удаление найденного события
                self.service.events().delete(
                    calendarId=calendar_id, eventId=event["id"]
                ).execute()
                return