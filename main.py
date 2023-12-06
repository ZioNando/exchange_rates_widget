import rumps
import requests


class CoursesApp(rumps.App):

    API_KEY = 'YOUR_API'
    UPDATE_INTERVAL = 1200

    def __init__(self):
        super(CoursesApp, self).__init__(name="Courses Widget", title='Loading...')

    def exchange_rates(self):
        url = f'https://openexchangerates.org/api/latest.json?app_id={self.API_KEY}'
        resource = requests.get(url)
        return resource.json()['rates']

    def usd_rub(self):
        rates = self.exchange_rates()
        return round(rates['RUB'], 2)

    @rumps.timer(UPDATE_INTERVAL)
    def update_course(self, _):
        self.title = f' {self.usd_rub()}₽'

    @rumps.clicked("Refresh data")
    def refresh_data(self, _):
        self.update_course()


if __name__ == "__main__":
    app = CoursesApp()
    app.run()
