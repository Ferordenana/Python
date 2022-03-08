import random
# I really like this program, a lot of times we're just too lazy to think about different passwords for our accounts. 
# With this code, not only you can generate a new random password, but also you can choose how long you want it to be. (range("xx")

def generate_password():
    capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    lowercase = ['a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
    symbols = ['!', '#', '$', '/', '(', ')',' ','&','¡']
    numbers = ['1','2','3','4','5','6','7','8','9','0']

    characters = capital_letters + lowercase + symbols + numbers

    password = []

    for i in range(15):
        random_character = random.choice(characters)
        password.append(random_character)
    password = ''.join(password)
    return password
            

        
def run():
    password = generate_password()
    print('Your new password is: ' + password)

run()
