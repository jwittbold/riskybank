
from member import Member
from account import Account
from product import Product
from base import Session, engine, Base
import pandas as pd
import os



# create all tables
Base.metadata.create_all(engine)

session = Session()

# # drop all tables
# Base.metadata.drop_all(engine)



def main():
    """Entrance into main program"""


    print("        ____________     ______     ____________     _____   _____     _____      _____\n",
          "      /  ______   /    /_  __/    /  ______   /    /    /  /    /    /    /     /    / \n",
         "     /  /     /  /      / /      /  /     /__/    /    / /    /     /    /     /    /\n",
        "    /  /_____/  /      / /      /  /________     /    // ____/     /     \____/    /\n",
       "   /     ______/      / /      /________   /    /        \          \ ________    /\n",
      "  /  /\  \           / /      ___      /  /    /    /\    \                  /   /\n",
     " /  /  \  \       __/ /__    /  /_____/  /    /    /  \    \        _______ /   /\n",
    "/__/    \__\     /______/   /___________/    /____/    \____\      /__________ /\n")


    print('Welcome to Risky Bank!\n')
    member_intake = input('Are you an existing Risky Bank member? Y/N: ').lower()
    if member_intake == 'n':
            

        print('\nTo join Risky Bank please enter your personal details.\n')
        new_member = Member.add_member(Member)
        verify_email = new_member.email
        if session.query(Member).filter(Member.email == verify_email).first():
            raise ValueError('Member email already exists. Please login using your email.')
        else:
            session.add(new_member)


        def open_account():
            """Open Account function adds new members to Database via add member function, creates new accounts via the create account function,
             and also allows for initial deposit into newly opened account."""

            open_acc = input('\nWould you like to open a new account? Y/N: ').lower()
            if open_acc == 'n':
                print('To join Risky Bank you must also open an account. Please start over.')
                session.close()
                os._exit(0)
            
            elif open_acc == 'y':

                new_account = Account.create_account(Account)
                session.add(new_member)

                new_member.accounts.append(new_account)  

                session.add(new_member)
                session.commit()
                print(f'\n{new_member.name}, your new', f'{new_member.accounts[0].acc_name} has a balance of', f'{new_member.accounts[0].balance}')


            elif open_acc != 'y' or 'n':
                raise ValueError('That is not a valid entry! To make a deposit please login again with your email.')


            transact_prompt = input('\nWould you like to make an initial deposit into your new account? Y/N: ').lower()
            if transact_prompt == 'n':
                print('Please login again when you are ready to make an account deposit. Goodbye 👋')
                session.close()
                os._exit(0)

            elif transact_prompt == 'y':         
                transact_credit = new_account.deposit()
                # print(new_member.accounts)
                session.commit()
                print('Thanks for joining! To make further transactions please log in to your account using your email.')
                session.close()
                os._exit(0)
            elif transact_prompt != 'y' or 'n':
                raise ValueError('That is not a valid entry! To make a deposit please login again with your email.')


        open_account()
    

    
    elif member_intake == 'y':

        # queries the database using the current users email address to pull up account
        current_member = session.query(Member).filter(Member.email == input('To login please enter your email adrress: ')).first()

        
        if current_member == None:
            raise ValueError('No account associated with this email. Please try again with a valid email.')

        else:
            current_member_df = pd.read_sql(session.query(Member).filter(Member.email == current_member.email).statement, session.bind)
            
            print('\n =========================================== MEMBER INFO ===========================================\n',
                current_member_df,
                '\n ===================================================================================================\n')
                
  
    elif member_intake != 'y' or 'n':
        raise ValueError('That is not a valid entry! Please start over.')


    def transaction():
        """Transaction function consists of for Deposit, Withdraw, or Balance Inquiry functions. Updates Database accordingly."""

        transact_prompt = input('\nWould you like to make a transaction? Y/N: ').lower()
        if transact_prompt == 'n':
            print('Transaction cancelled. Goodbye 👋')
            session.close()
            os._exit(0)
        
        elif transact_prompt == 'y':
            transact_choice = input('\nWhat kind of transaction would you like to make?\n'
                                    '\nDeposit (d), Withdrawal (w), Balance Inqiry (i), Financial Product (p), or Exit (exit): ').lower()
        
            # Make a deposit
            if transact_choice == 'd':
                transact_credit = current_member.accounts[0].balance + current_member.accounts[0].deposit()
                print('Your new balance is:', transact_credit)
                current_member.accounts[0].balance = transact_credit
                session.commit()
                transaction()


            # Make a withdrawal 
            elif transact_choice == 'w':
                transact_debit = current_member.accounts[0].balance + current_member.accounts[0].withdraw()
                print('Your new balance is:', transact_debit)
                current_member.accounts[0].balance = transact_debit
                session.commit()
                transaction()


            # Balance Inquiry
            elif transact_choice == 'i':
                transact_balace_inquiry = current_member.accounts[0].balance_inquiry()
                transaction()
                
            
            # Apply for financial product
            elif transact_choice == 'p':
                new_product = Product.create_product(Product)
                session.add(new_product)
                current_member.accounts[0].products.append(new_product)
                session.commit()


            # Exit the program
            elif transact_choice == 'exit':
                print('Transaction Canceled. Goodbye 👋')
                session.close()
                os._exit(0)

            elif transact_prompt != 'd' or 'w' or 'i' or 'p' or 'exit':
                raise ValueError('That is not a valid entry! To make a transaction please login again with your email.')
        elif transact_prompt != 'y' or 'n':
            raise ValueError('That is not a valid entry! To make a transaction please login again with your email.')
    
    transaction()

session.close()



if __name__ == '__main__':
    main()




