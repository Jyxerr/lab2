import csv

is_in_top = True
# Creating the list of preferences
preferences = []

with open('output', 'w', encoding='utf-8') as output_file, \
     open('steam (1).csv', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:

            # Are we at the top of the table?
            if is_in_top:
                is_in_top = False

                # Asking the user about their preferences in all categories.
                for category in row:
                    current_wish = input('Write favourite ' + category + '.\n')

                    # Changing the text for convenience
                    current_wish = current_wish.lower()
                    current_wish = current_wish.replace(' ', '')

                    # Filling out the preferences list
                    preferences.append(current_wish.split(','))
                    continue

            string_row = (' '.join(row))
            string_row = string_row.lower()

            it_not_fits = False

            # Checking that the game is suitable.
            for current_category in preferences:
                if current_category == ['']:
                    continue

                it_includes = False

                for wishes in current_category:
                    if not string_row.find(wishes) == -1:
                        it_includes = True
                        break

                # If games don't include one of the categories,they don't fit.
                if not it_includes:
                    it_not_fits = True
                    break

            # If it not not fits, it fits.
            if not it_not_fits:
                output_file.write(row[1])
                output_file.write('\n')
