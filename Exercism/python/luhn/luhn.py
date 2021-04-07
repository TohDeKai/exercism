import re

class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        self.card_num = "".join(self.card_num.split())
        # strings less than or equal to 1 not valid
        if len(self.card_num) <= 1:
            return False
        elif self.card_num.isdigit() == False:
            return False
        else:
            #convert string to list
            card_num_list = []
            for i in self.card_num:
                card_num_list.append(i)
            #doubing every 2nd digit from the right
            reversed_every_2_digits = card_num_list[-2::-2]
            remaining_digits = card_num_list[::-2]
            for i in range(len(reversed_every_2_digits)):
                reversed_every_2_digits[i] = int(reversed_every_2_digits[i])
                reversed_every_2_digits[i] = reversed_every_2_digits[i]*2
                if reversed_every_2_digits[i] >= 10:
                    reversed_every_2_digits[i] -= 9
            #summing up the digits
            sum = 0
            for i in reversed_every_2_digits:
                sum += i
            #checking if sum is even
            for i in remaining_digits:
                sum += int(i)
            if sum % 10 == 0:
                return True
            else: 
                return False

print (Luhn('59').valid())


            