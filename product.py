from sqlalchemy import Column, String, Integer, Float, Sequence, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import MetaData
from account import Account
from base import Base


class Product(Base):
    """Product class is used for instantiating custom products such as home loans, business loans, personal loans, etc. 
    
    Parameters:
    prod_name (Str): Name of product to be created
    amount (Int): Dollar amount related to product
    rate (float): Rate of interest 
    term (Int): Duration of product in years  
    """

    __tablename__ = 'products'

    id = Column(Integer, Sequence('product_seq_id'), primary_key=True)
    prod_name = Column(String(50))
    amount = Column(Integer)
    rate = Column(Float)
    term = Column(Float)
    account_id = Column(Integer, ForeignKey('accounts.id'))  # values in products.account_id column should be constrained to values in account.id column (primary key)
    # builds relationship with Account class 
    account = relationship('Account', back_populates='products', cascade='all, delete-orphan', single_parent=True)

    def __init__(self, prod_name, amount, rate, term):
        self.prod_name = prod_name
        self.amount = amount
        self.rate = rate
        self.term = term



    # for viewing values of Product class object when printed to console
    def __repr__(self):
        return "Product(prod_name='%s', rate='%s')>" % (self.prod_name, self.rate)




    def create_product(Product):
        """Create Product function allows member to apply for a loan or credit card, specifying desired loan amount and term in years, or desired credit limit for credit card."""


        print('\nWhat kind of product would you like to add?\n')
        prod_choice = input('Loan (l) or Credit Card (cc): ').lower()
        if prod_choice == 'l':
            loan = Product(prod_name='Loan', amount=int(input('Please enter desired loan amount: ')), rate=12, term=int(input('Please enter the desired term of loan in full year value: ')))
            print(f'\nYou have successfully applied for a', f'{loan.prod_name}', 'in the amount of', f'{loan.amount}', 'with a ' f'{loan.rate}% annual rate and ' f'{loan.term} year term.\n'
                    'Our Financial Department will notify you of their decision shortly.')
            return loan

        elif prod_choice == 'cc':
            credit_card = Product(prod_name='Credit Card', amount=int(input('Please enter desired credit limit: ')), rate=17, term=None)
            print(f'\nYou have successfully applied for a', f'{credit_card.prod_name}', 'with a maximum limit of', f'{credit_card.amount}', 'and a fixed APR of', f'{credit_card.rate}%\n'
                    'Our Financial Department will notify you of their decision shortly.')
            return credit_card
        else:
            raise ValueError('Invalid Choice.')




# tells the ORM that the Product class itself should be linked to the Account class, useing the attribute Product.account.relationship()
Account.products = relationship('Product', order_by='Product.id', back_populates='account', cascade='all, delete-orphan', single_parent=True)


