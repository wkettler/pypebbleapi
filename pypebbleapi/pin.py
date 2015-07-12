from six import iteritems


class _DictionableObject(object):
    def __iter__(self):
        for k, v in iteritems(self.__dict__):
            if k.startswith('_'):
                continue
            yield k, v

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]


class Pin(_DictionableObject):
    icon = {
        'NOTIFICATION_GENERIC': 'system://images/NOTIFICATION_GENERIC',
        'NOTIFICATION_REMINDER': 'system://images/NOTIFICATION_REMINDER',
        'NOTIFICATION_FLAG': 'system://images/NOTIFICATION_FLAG',
        'NOTIFICATION_FACEBOOK_MESSENGER': 'system://images/NOTIFICATION_FACEBOOK_MESSENGER',
        'NOTIFICATION_WHATSAPP': 'system://images/NOTIFICATION_WHATSAPP',
        'NOTIFICATION_GMAIL': 'system://images/NOTIFICATION_GMAIL',
        'NOTIFICATION_FACEBOOK': 'system://images/NOTIFICATION_FACEBOOK',
        'NOTIFICATION_GOOGLE_HANGOUTS': 'system://images/NOTIFICATION_GOOGLE_HANGOUTS',
        'NOTIFICATION_TELEGRAM': 'system://images/NOTIFICATION_TELEGRAM',
        'NOTIFICATION_TWITTER': 'system://images/NOTIFICATION_TWITTER',
        'NOTIFICATION_GOOGLE_INBOX': 'system://images/NOTIFICATION_GOOGLE_INBOX',
        'NOTIFICATION_MAILBOX': 'system://images/NOTIFICATION_MAILBOX',
        'NOTIFICATION_OUTLOOK': 'system://images/NOTIFICATION_OUTLOOK',
        'NOTIFICATION_INSTAGRAM': 'system://images/NOTIFICATION_INSTAGRAM',
        'NOTIFICATION_BLACKBERRY_MESSENGER': 'system://images/NOTIFICATION_BLACKBERRY_MESSENGER',
        'NOTIFICATION_LINE': 'system://images/NOTIFICATION_LINE',
        'NOTIFICATION_SNAPCHAT': 'system://images/NOTIFICATION_SNAPCHAT',
        'NOTIFICATION_WECHAT': 'system://images/NOTIFICATION_WECHAT',
        'NOTIFICATION_VIBER': 'system://images/NOTIFICATION_VIBER',
        'NOTIFICATION_SKYPE': 'system://images/NOTIFICATION_SKYPE',
        'NOTIFICATION_YAHOO_MAIL': 'system://images/NOTIFICATION_YAHOO_MAIL',
        'GENERIC_EMAIL': 'system://images/GENERIC_EMAIL',
        'GENERIC_SMS': 'system://images/GENERIC_SMS',
        'GENERIC_WARNING': 'system://images/GENERIC_WARNING',
        'GENERIC_CONFIRMATION': 'system://images/GENERIC_CONFIRMATION',
        'GENERIC_GENERIC_QUESTION': 'system://images/',
        'PARTLY_CLOUDY': 'system://images/PARTLY_CLOUDY',
        'CLOUDY_DAY': 'system://images/CLOUDY_DAY',
        'LIGHT_SNOW': 'system://images/LIGHT_SNOW',
        'LIGHT_RAIN': 'system://images/LIGHT_RAIN',
        'HEAVY_RAIN': 'system://images/HEAVY_RAIN',
        'HEAVY_SNOW': 'system://images/HEAVY_SNOW',
        'TIMELINE_WEATHER': 'system://images/TIMELINE_WEATHER',
        'TIMELINE_SUN': 'system://images/TIMELINE_SUN',
        'RAINING_AND_SNOWING': 'system://images/RAINING_AND_SNOWING',
        'TIMELINE_MISSED_CALL': 'system://images/TIMELINE_MISSED_CALL',
        'TIMELINE_CALENDAR': 'system://images/TIMELINE_CALENDAR',
        'TIMELINE_SPORTS': 'system://images/TIMELINE_SPORTS',
        'TIMELINE_BASEBALL': 'system://images/TIMELINE_BASEBALL',
        'AMERICAN_FOOTBALL': 'system://images/AMERICAN_FOOTBALL',
        'BASKETBALL': 'system://images/BASKETBALL',
        'CRICKET_GAME': 'system://images/CRICKET_GAME',
        'SOCCER_GAME': 'system://images/SOCCER_GAME',
        'HOCKEY_GAME': 'system://images/HOCKEY_GAME',
        'RESULT_DISMISSED': 'system://images/RESULT_DISMISSED',
        'RESULTS_DELETED': 'system://images/RESULTS_DELETED',
        'RESULT_MUTE': 'system://images/RESULT_MUTE',
        'RESULTS_SENT': 'system://images/RESULTS_SENT',
        'RESULTS_FAILED': 'system://images/RESULTS_FAILED',
        'STOCKS_EVENT': 'system://images/STOCKS_EVENT',
        'MUSIC_EVENT': 'system://images/MUSIC_EVENT',
        'BIRTHDAY_EVENT': 'system://images/BIRTHDAY_EVENT',
        'PAY_BILL': 'system://images/PAY_BILL',
        'HOTEL_RESERVATION': 'system://images/HOTEL_RESERVATION',
        'TIDE_IS_HIGH': 'system://images/TIDE_IS_HIGH',
        'NEWS_EVENT': 'system://images/NEWS_EVENT',
        'SCHEDULED_EVENT': 'system://images/SCHEDULED_EVENT',
        'DURING_PHONE_CALL': 'system://images/DURING_PHONE_CALL',
        'CHECK_INTERNET_CONNECTION': 'system://images/CHECK_INTERNET_CONNECTION',
        'MOVIE_EVENT': 'system://images/MOVIE_EVENT',
        'GLUCOSE_MONITOR': 'system://images/GLUCOSE_MONITOR',
        'ALARM_CLOCK': 'system://images/ALARM_CLOCK',
        'CAR_RENTAL': 'system://images/CAR_RENTAL',
        'DINNER_RESERVATION': 'system://images/DINNER_RESERVATION',
        'RADIO_SHOW': 'system://images/RADIO_SHOW',
        'AUDIO_CASSETTE': 'system://images/AUDIO_CASSETTE',
        'SCHEDULED_FLIGHT': 'system://images/SCHEDULED_FLIGHT',
        'NO_EVENTS': 'system://images/NO_EVENTS',
        'REACHED_FITNESS_GOAL': 'system://images/REACHED_FITNESS_GOAL',
        'DAY_SEPARATOR': 'system://images/DAY_SEPARATOR',
        'WATCH_DISCONNECTED': 'system://images/WATCH_DISCONNECTED',
        'TV_SHOW': 'system://images/TV_SHOW',
    }

    layout_type = {
        'GENERIC_PIN': 'genericPin',
        'CALENDAR_PIN': 'calendarPin',
        'GENERIC_REMINDER': 'genericReminder',
        'GENERIC_NOTIFICATION': 'genericNotification',
        'WEATHER_PIN': 'weatherPin',
        'SPORTS_PIN': 'sportsPin'
    }

    action_type = {
        'OPEN_WATCH_APP': 'openWatchApp',
    }

    color = {
        'RED': '#FF0000',
        'ORANGE': '#FFA500',
        'YELLOW': '#FFFF00',
        'GREEN': '#00FF00',
        'BLUE': '#0000FF',
        'PURPLE': '#551A8B'
    }

    def __init__(self,
            id,
            time,
            duration=None,
            createNotification=None,
            updateNotification=None,
            layout=None,
            reminders=None,
            actions=None,
            ):
            self.id = id
            self.time = time

            if duration is not None:
                self.duration = duration

            if createNotification is not None:
                self.createNotification = createNotification

            if updateNotification is not None:
                self.updateNotification = updateNotification

            if layout is not None:
                self.layout = layout

            if reminders is not None:
                self.reminders = reminders

            if actions is not None:
                self.actions = actions

    def __iter__(self):
        for k, v in iteritems(self.__dict__):
            if k.startswith('_'):
                continue
            yield k, v

    def __getitem__(self, key):
        return self.__dict__[key]
