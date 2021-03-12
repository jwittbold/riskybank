
from sqlalchemy import Column, String, Integer, Float, Sequence, Date, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy import MetaData
from base import Base
import os




class Member(Base):
    """Member class is used for instantiating new members. 
    
    Parameters:
    name (str): Member full name
    address (str): Member primary address
    phone (str): Member primary phone number
    email (str): Member email address
    pin (int): Member personal pin code

    """
     
    __tablename__ = 'members'

    id = Column(Integer, Sequence('member_id_seq'), primary_key=True)
    name = Column(String(50))
    address = Column(String(100))
    phone = Column(String(50))
    email = Column(String(50))
    pin = Column(Integer)
    account = relationship('Account', back_populates='members', cascade='all, delete-orphan', single_parent=True)

    # constructor 
    def __init__(self, name, address, phone, email, pin):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.pin = pin


    # for viewing values of Member class object when printed to console
    def __repr__(self):
        return "<Member(name='%s', address='%s', phone='%s', email='%s', pin='%s')>" % (self.name, self.address, self.phone, self.email, self.pin)


    # Functions for Member class

    def add_member(Member):
        
        member_info = Member(name=input('Full Name: '),
                            address=input('Current Address: '),
                            phone=input('Primary Phone Number: '),
                            email=input('Email: '),
                            pin=input('Private four digit PIN: ')
                            )
        
        
        print('\n=========================== NEW MEMBER INFO ===========================\n',
              f'\n{member_info.name}', 
              f'\n{member_info.address}', 
              f'\n{member_info.phone}',
              f'\n{member_info.email}',
              f'\n{member_info.pin}\n',
              '\n=========================== NEW MEMBER INFO ===========================\n')
        confirm = input('To proceed, please confirm that the above information is correcet, Y/N: ').lower()
        if confirm != 'y':
            print('Please start over.')
            os._exit(0)
        else:
            return member_info


    

