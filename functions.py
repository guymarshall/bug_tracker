class Functions:
    def number_to_day(number):
        day = ''
        match number:
            case 1: day = 'Monday'
            case 2: day = 'Tuesday'
            case 3: day = 'Wednesday'
            case 4: day = 'Thursday'
            case 5: day = 'Friday'
            case 6: day = 'Saturday'
            case 7: day = 'Sunday'
            case _: day = 'Invalid'
        return day


    def number_to_month(number):
        month = ''
        match number:
            case 1: month = 'January'
            case 2: month = 'February'
            case 3: month = 'March'
            case 4: month = 'April'
            case 5: month = 'May'
            case 6: month = 'June'
            case 7: month = 'July'
            case 8: month = 'August'
            case 9: month = 'September'
            case 10: month = 'October'
            case 11: month = 'November'
            case 12: month = 'December'
            case _: month = 'Invalid'        
        return month


    def is_leap_year(year):
        result = False
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            result = True
        return result


    def month_to_days(month, year, self):
        days = 0
        match month:
            case 'January': days = 31
            case 'February':
                if self.is_leap_year(year):
                    days = 29
                else:
                    days = 28
            case 'March': days = 31
            case 'April': days = 30
            case 'May': days = 31
            case 'June': days = 30
            case 'July': days = 31
            case 'August': days = 31
            case 'September': days = 30
            case 'October': days = 31
            case 'November': days = 30
            case 'December': days = 31
        return days

#     def filter_input(string input) {
#         input_is_dangerous = true

#         while (input_is_dangerous) {
#             if (str_contains(input, '(')) {
#                 input = str_replace('(', '', input)
#             } else if (str_contains(input, ')')) {
#                 input = str_replace(')', '', input)
#             } else if (str_contains(input, '')) {
#                 input = str_replace('', '', input)
#             } else if (str_contains(input, '{')) {
#                 input = str_replace('{', '', input)
#             } else if (str_contains(input, '}')) {
#                 input = str_replace('}', '', input)
#             } else if (str_contains(input, '[')) {
#                 input = str_replace('[', '', input)
#             } else if (str_contains(input, ']')) {
#                 input = str_replace(']', '', input)
#             } else if (str_contains(input, 'SELECT')) {
#                 input = str_replace('SELECT', '', input)
#             } else if (str_contains(input, '\'')) {
#                 input = str_replace('\'', '', input)
#             } else if (str_contains(input, '"')) {
#                 input = str_replace('"', '', input)
#             } else {
#                 input_is_dangerous = false
#             }
#         }

#         return input
#     }
# }
