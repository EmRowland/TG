from datetime import datetime, timedelta
from django.utils import timezone
from .models import Events, SubscribeToEvent


def cronjob():

    events = Events.objects.all()
    one_hour = timedelta(hours=1)
    real = timezone.make_aware(datetime.now())

    if events:
        for event in events:
            real_e = event.time_when
            dick = real - real_e
            print("...................................dick....................")
            print(dick)
            print("...................................dick....................")
            print(real)
            print(".................................... datetime on top")
            print(real_e)
            if event.event_status_to_come == 'True':

                if event.time_when >= datetime().now:
                    # setting the Event status to false if the event time has passed
                    event.status = True
                elif event.time_when - time.now <= '1:00:00':
                    # checking if the event is in hour time
                    # send email function
                    # set event status to false
                    event.status = True
                    datetime.time

                    print('worked')
                else:
                    print('fucked .........')



