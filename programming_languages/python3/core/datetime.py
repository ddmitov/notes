#!/usr/bin/env python3

# Today as a string:
from datetime import datetime
import pytz

utc = pytz.utc
date_time_now = datetime.now(utc)
date_time_string = (date_time_now.strftime('%Y-%m-%d %H:%M:%S %Z').strip())

# Date in the past:
from datetime import date
from dateutil.relativedelta import relativedelta

past_date = (date.today() - relativedelta(months=1))
