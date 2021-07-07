def make_questions():
    dictionary = {}
    dictionary['France'] = 'Paris'
    dictionary['Spain'] = 'Madrid'
    dictionary['UK'] = 'London'
    dictionary['Ireland'] = 'Dublin'
    dictionary['Italy'] = 'Rome'
    dictionary['Greece'] = 'Athens'
    dictionary['Russia'] = 'Moscow'
    dictionary['Algeria'] = 'Algeirs'
    dictionary['Turkey'] = 'Ankara'
    dictionary['Lebanon'] = 'Beirut'
    dictionary['Australia'] = 'Canberra'
    dictionary['Cuba'] = 'Havana'
    dictionary['Peru'] = 'Lima'
    dictionary['Portugal'] = 'Lisbon'
    dictionary['Norway'] = 'Oslo'
    dictionary['Canada'] = 'Ottawa'
    dictionary['Latvia'] = 'Riga'
    dictionary['Czech Republic'] = 'Prague'
    dictionary['Sweden'] = 'Stockholm'
    dictionary['Japan'] = 'Tokyo'
    return dictionary
	
def pick_question(dictionary): 
    count = 0
    for i in range(20):
        key, value = dictionary.popitem()
        print('Enter a capital for the country :', key)
        capital = input('Enter the capital: ')
        if capital == value:
            count += 1
            print('Right!')
    print('The number of correct answers is', count)
    print('The nubmer of incorrect answers is', 20 - count)
	
def main():
    dictionary = make_questions()
    pick_question(dictionary)
main()