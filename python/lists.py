
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

#exrecise:
#Select first four elements from row_1 using a list slicing syntax shortcut. Assign the output to a variable named first_4_fb.
#Select last three elements from row_1 using a list slicing syntax shortcut. Assign the output to a variable named last_3_fb
#From row_5, select the list slice ['USD', 1126879] using a list slicing syntax shortcut. Assign the output to a variable named pandora_3_4

first_4_fb = row_1[:4]
last_3_fb = row_1[-3:]
pandora_3_4 = row_5[2:4]

#getting average of the rating
app_data_set = [row_1, row_2, row_3, row_4, row_5]
rating_sum = 0
for list in app_data_set:
    rating = list[-1]
    rating_sum+=rating
avg_rating = rating_sum/5
print(avg_rating)