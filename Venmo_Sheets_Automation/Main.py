from __future__ import print_function
from venmo_api import Client
import os
import gspread
import time
from dotenv import load_dotenv


# load access token and service account environment variables

load_dotenv('variable.env')

    
def main():

    

    # venmo access token
    access_token = os.getenv('access_token')
    print(access_token) # makes sure the token loads properly mainly for debugging
    
    client = Client(access_token)  # create venmo client

    sa = gspread.service_account('example.json')  # create google client


    # open google sheet 'Your_sheet_here' and access sheet 'Venmo'
    sheet = sa.open('your google sheet')
    wks = sheet.worksheet('your worksheet') # opens the specific worksheet

    me = client.user.get_my_profile()  # get venmo userid
    my_id = me.id
    
    # the api i am using the limit is 50 so you cant go above that learn it the hard way
    transactions = client.user.get_user_transactions(
        user_id=my_id)  # get last 50 venmo transactions 
    
    sheet_updates = 0 #counter for how many updates where made to the sheet
    payment_ids = wks.col_values(5) # the ID's are stored in the 5th column
    
    
    # Iterate through each transaction in reverse order (most recent first)
    for t in reversed(transactions):
        # data from each venmo transaction
        sender = t.actor.first_name + ' ' + t.actor.last_name
        receiver = t.target.first_name + ' ' + t.target.last_name
        amt = t.amount
        note = t.note
        id = t.payment_id
        #date = t.date_created

       
        id_check = id # temp variable to check transaction ID
        
    # Check if the payment_id has already been processed
        

        # Check if the transaction ID has not already been processed
        if not (id_check in payment_ids): 
            time.sleep(3)  # Pause for 3 seconds to avoid rate limits or rapid requests
            
            row_num=2 # the only row that should get updated becuase row 1 is the header row
            if(sender == 'Your venmo name'): # Check if the sender is 'your venmo name'
                
                amt = amt*-1 # if  outgoing i want the transaction to be nagative
                outgoing = [sender, receiver, amt, note, id]
                #print(outgoing)
                
                wks.insert_row(outgoing,2) # inserts the outgoing to row 2
                
                sheet_updates += 1 
                # Format the newly added row with a different background color
                row_range = f'A{row_num}:E{row_num}'
                wks.format(row_range, {'backgroundColor': {
                  "red": 100,
                  "green": 200,
                  "blue": 200
                  
                }})
                
                
                
            elif(sender != 'your venmo name'): # Check if the sender is not 'your venmo name'
                insertion = [sender, receiver, amt, note, id]
               
                
                wks.insert_row(insertion,2) # inserts the data at row 2
                
                
                sheet_updates += 1
                 # Format the newly added row with a different background color
                row_range = f'A{row_num}:E{row_num}'
                wks.format(row_range, {'backgroundColor': {
                    "red": 194,
                    "green": 100,
                    "blue": 154
                    }})
            
            
        
            
    

    
        

    # notify whether updates have been made to the spreadsheet
    if sheet_updates > 0:
        print(str(sheet_updates) +
              ' new venmo transaction(s) have been added to the sheet.')
    elif sheet_updates == 0:
        print('No new venmo transactions.')

if __name__ == '__main__':
    main()

