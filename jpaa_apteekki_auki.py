# -*- coding: utf-8 -*
#py3

import datetime

#aika_nyt = datetime.now().isocalendar()[1]
# Debug:
#                             yyyy, mm, dd
maaratty_aika = datetime.date(2020, 10, 3)
aika_nyt = maaratty_aika.isocalendar()[1]

if aika_nyt % 2 == 0:
    print("Mannilantien apteekki")

if aika_nyt % 2 == 1:
    print("Helsingintien apteekki")



