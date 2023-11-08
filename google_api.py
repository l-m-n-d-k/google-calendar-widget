from google.oauth2 import service_account
from googleapiclient.discovery import build


class GoogleCalendar:
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    FILE_PATH = 'grand-appliance-403520-b06ed9fdb088.json'

    def __init__(self):
        # Scopes and .json file of the service google account
        credentials = service_account.Credentials.from_service_account_file(
            filename=self.FILE_PATH, scopes=self.SCOPES
        )
        # Authorization in service google account
        self.service = build('calendar', 'v3', credentials=credentials)
    
    # Calendars list
    def get_calendar_list(self):
        return self.service.calendarList().list().execute()
    
    # Creat calendar
    def add_calendar(self, calendar_id):
        calendar_list_entry = {
            'id': calendar_id
        } 
        return self.service.calendarList().insert(
            body=calendar_list_entry
            ).execute()
    
    # Add event
    def add_event(self, calendar_id, event):
        return self.service.events().insert(
            calendarId=calendar_id, 
            body=event).execute()        

    # Delete event
    def delete_evente(self, calendar_id, event_name):
        events_result = self.service.events().list(calendarId=calendar_id).execute()
        events = events_result.get('items', [])

        # Поиск события по названию
        for event in events:
            if event.get('summary') == event_name:
                # Удаление найденного события
                self.service.events().delete(calendarId=calendar_id, eventId=event['id']).execute()
                print(f'Событие "{event_name}" успешно удалено')
                return
            print(f'Событие "{event_name}" не найдено')

# obj = GoogleCalendar()

# calendar_id = 'dima2642007@gmail.com'
# event = {
#   'summary': 'Тестовый пример',
#   'location': 'Москва',
#   'description': 'Тестовое описание',
#   'start': {
#     'date': '2023-11-1',
#   },
#   'end': {
#     'date': '2023-11-4',
#   },
# }

# # Add event
# # obj.add_event(calendar_id=calendar_id, event=event)

# # Delete evente
# # obj.delete_evente(calendar_id=calendar_id, event_name='Тестовый пример')