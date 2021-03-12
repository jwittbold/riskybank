
from sqlalchemy import Column, String, Integer, Float, Sequence, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import MetaData
from member import Member
from base import Base


class Account(Base):
    """Account class is used for instantiating new accounts for existing members. 
    
    Parameters:
    acc_name (str): Account type name (checking, savings, etc.)
    balance (float): Account balance

    """

    __tablename__ = 'accounts'

    id = Column(Integer, Sequence('account_id_seq'), primary_key=True)
    acc_name = Column(String(50), nullable=False)
    balance = Column(Float)
    member_id = Column(Integer, ForeignKey('members.id')) # values in accounts.member_id column should be constrained to values in members.id column (primary key)
    member = relationship('Member', back_populates='accounts', cascade='all, delete-orphan', single_parent=True)

    def __init__(self, acc_name, balance):
        self.acc_name = acc_name
        self.balance = balance



    # for viewing values of Account class object when printed to console
    def __repr__(self):
        return "<Account(acc_name='%s', balance='%s', member_id='%s')>" % (self.acc_name, self.balance, self.member_id)




    def create_account(Account):
        """Creates new Account derived from Account(Base), can choose 'Member Checking' or 'Member Savings'. 
        Differ in name only. Balance initialized to =0

        """

        print('\nWhat kind of account would you like to open?\n')
        acc_choice = input('Checking (c) or Savings (s): ').lower()
        if acc_choice == 'c':
            checking_account = Account(acc_name='Member Checking', balance=0)
            print('You have successfully opened a Member Checking Account')
            return checking_account 
        elif acc_choice == 's':
            savings_account = Account(acc_name='Member Savings', balance=0)
            print('You have successfully opened a Member Savings Account')
            return savings_account
        else:
            raise ValueError('Invalid Choice.')


        # for viewing values of Account class object when printed to console
        def __repr__(self):
            return "<Account(acc_name='%s', balance='%s', member_id='%s')>" % (self.acc_name, self.balance, self.member_id)



    # Functions available to Account Class
    
    def deposit(Account):
        """Deposit into account"""
        amount = float(input('Enter amount to be deposited: '))
        Account.balance =+ amount 
        print('\nAmount Deposited:', amount, 'into your', Account.acc_name)
        return Account.balance

    
    def withdraw(Account):
        """withdraw from Account"""
        amount = float(input('Enter amount to be withdrawn: '))
        if Account.balance < amount:
            raise ValueError('Insufficient funds to complete transaction. Please check your account balance.')
        else:
            Account.balance =- amount
            print('\nYou have withdrawn', amount, 'from your', Account.acc_name)
            return Account.balance

        
    def balance_inquiry(Account):
        """Prints account balance"""
        print('Your', Account.acc_name, 'balance is:', Account.balance)


# tells the ORM that the Account class should be linked to the Member class, using the attribute Account.member.relationship()
Member.accounts = relationship('Account', order_by='Account.id', back_populates='member', cascade='all, delete-orphan', single_parent=True)  
Account.members = relationship('Member', order_by='Member.id', back_populates='account', cascade='all, delete-orphan', single_parent=True)













    # def deposit(self, amount):
    #     """make a deposit"""
    #     self.balance += amount

    
    # def withdraw(self, amount):
    #     """make a withdrawal"""
    #     if amount > self.balance:
    #         raise ValueError('Insufficient funds to complete transaction')
    #     self.balance -= amount


    # @property
    # def balance(self):
    #     """check balance"""
    #     return self.balance

    # # def __repr__(self):
    # #     return '{0.__class__.__acc_name__}(acc_name={0.acc_name}, balance={0.balance})'.format(self)

    # def __str__(self):
    #     return 'Account of {}, current balance: {}'.format(self.acc_name, self.balance)
# uselist=False allows object to be manipulated but not appeneded to, so if uselist=False, no list exists to append new_account to, in not used, member_id does not show in account member_id column, accounts seemingly not linked



