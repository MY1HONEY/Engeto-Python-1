databaze = {'id123': {},'id124': {},'id125': {}}

slovnik1 = {'jmeno': 'Thomas', 'vek': 45, 'zeme': 'Czechia', 'mesto': 'Brno'}
slovnik2 = {'jmeno': 'Daniel', 'vek': 34, 'zeme': 'Czechia', 'mesto': 'Prague'}
slovnik3 = {'jmeno': 'Eva', 'vek': 43, 'zeme': 'Czechia', 'mesto': 'Olomouc'}

databaze.update(id123 = slovnik1)
databaze.update(id124 = slovnik2)
databaze.update(id125 = slovnik3)

print(databaze)
