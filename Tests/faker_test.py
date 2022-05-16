import pytest 

from datetime import date
from faker import Faker

# Author - Robert Chapin
# Date Created - 5/13/2022
# This test fills out a large form page with fake / random data utilizing faker.
# Documentation on faker can be found here:
# https://faker.readthedocs.io/en/master/providers/baseprovider.html
def test_fill_out_form_with_faker(page):
    fake = Faker()
    page.goto("https://www.roboform.com/filling-test-all-fields")
    
    page.fill("input[name='01___title']", fake.prefix())
    page.fill("input[name='02frstname']", fake.first_name())
    page.fill("input[name='03middle_i']", fake.first_name())
    page.fill("input[name='04lastname']", fake.first_name_female())
    page.fill("input[name='04fullname']", fake.name())
    page.fill("input[name='05_company']", fake.company())
    page.fill("input[name='06position']", fake.job())
    page.fill("input[name='10address1']", fake.street_address())
    page.fill("input[name='11address2']", '')  
    page.fill("input[name='13adr_city']", fake.city())
    page.fill("input[name='14adrstate']", fake.state())
    page.fill("input[name='15_country']", fake.country())
    page.fill("input[name='16addr_zip']", fake.postcode())
    page.fill("input[name='20homephon']", fake.phone_number())
    page.fill("input[name='21workphon']", fake.phone_number())
    page.fill("input[name='22faxphone']", fake.phone_number())
    page.fill("input[name='23cellphon']", fake.phone_number())

    #utilizes bothify which is ? for alpha chars # for digits
    page.fill("input[name='24emailadr']", 
        fake.bothify(text='???????????@gmail.com'))   
    page.fill("input[name='25web_site']", 
        fake.bothify(text='www.??????????????????-####????.com'))

    page.fill("input[name='30_user_id']", 
        fake.bothify(text='?#?#?#?#?#?#?#?#?#?#?'))
    page.fill("input[name='31password']", fake.password(length=12))
    page.fill("input[name='41ccnumber']", fake.credit_card_number())
    page.fill("input[name='43cvc']", fake.credit_card_security_code())
    page.fill("input[name='44cc_uname']", fake.name())
    
    #Card issuing bank
    page.fill("input[name='45ccissuer']", fake.company()) 
    #Customer Service Phone Number
    page.fill("input[name='46cccstsvc']", fake.phone_number()) 
    
    #selects a random letter but only from list of M and F
    page.fill("input[name='60pers_sex']", fake.bothify(letters='MF', text='?')) 

    page.fill("input[name='61pers_ssn']", fake.ssn())
    page.fill("input[name='62driv_lic']", 
        fake.bothify(text='#####################'))
    
    #generates a random digit must convert to string
    page.fill("input[name='66pers_age']", 
        str(fake.pydecimal(min_value=5, max_value=100))) 
    page.fill("input[name='67birth_pl']", fake.address())
    page.fill("input[name='68__income']", fake.bothify(text='$###,###'))
    page.fill("input[name='71__custom']", fake.sentence())
    page.fill("input[name='72__commnt']", fake.paragraph())

    #Credit Card type
    cardType = fake.word(ext_word_list=[
        'amex', 
        'diners', 
        'discover', 
        'mastercard', 
        'visa',
        ])
    
    # Would generate a random credit card based upon the types above 
    # but not used here
    #creditCardType = fake.credit_card_provider(card_type=cardType) 
    cardTypeValue = findCardType(cardType)
    page.select_option("select[name='40cc__type']", cardTypeValue)

    #Credit Card Expiration Date
    cardExpireDate = fake.credit_card_expire().split('/')
    
    # removes leading zero if one is present in month as its not present
    # in value of options
    if(cardExpireDate[0][0]=="0"):
        cardExpireDate[0] = cardExpireDate[0][1]

    page.select_option("select[name='42ccexp_mm']", str(cardExpireDate[0]))
    page.select_option("select[name='43ccexp_yy']", f"20{cardExpireDate[1]}")
    
    #Date of Birth
    dateOfBirth = fake.date_of_birth(maximum_age=100)
    page.select_option("select[name='66mm']", str(dateOfBirth.month))
    page.select_option("select[name='67dd']", str(dateOfBirth.day))
    page.select_option("select[name='68yy']", str(dateOfBirth.year))
    
    page.click("input[value='Reset']")


#method to generate specific card type values that match the page
def findCardType(cardType):
    switch={
       'amex': "1",
       'diners': "4",
       'discover': "19",
       'mastercard': "6",
       'visa': "9",
       }
    return switch.get(cardType,"It is not a card type that is accepted")
