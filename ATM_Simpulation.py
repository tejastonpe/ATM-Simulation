import logging

logger=logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(message)s',filename="ATM_Transitions.log",level=logging.INFO)

atm_amount_distribution={500:500,100:500,50:500,20:500,10:500}

def display_atm_amount():
    print("\nAvailable notes in ATM")
    for rupee,numbers in atm_amount_distribution.items():
        print(f"{rupee} Rs available notes:{numbers} Total amount:{rupee*numbers} Rs")

def display_total_amount():
    total_amount = 0
    for rupee,numbers in atm_amount_distribution.items():
        total_amount += rupee*numbers
    print(f"\nTotal amount in ATM: {total_amount}")

def draw_cash(amount_withdraw):
    try:
        if amount_withdraw>10000 or amount_withdraw <100 or amount_withdraw % 10 != 0:
            raise ValueError("Enter withdraw amount in range of 100 to 10000 rs & amount is multiplies of 10")
        else:
            remaining_amount = amount_withdraw
            total_notes={}

            for rupee,numbers in atm_amount_distribution.items():
                notes_to_add =  remaining_amount // rupee
                if notes_to_add > 0:
                    total_notes[rupee]=notes_to_add
                    remaining_amount -= (notes_to_add*rupee)
                    atm_amount_distribution[rupee] -= notes_to_add

        if sum(total_notes.values()) > 40:
            raise ValueError("Maximum number of notes, ATM can't withdraw")
        
        for rupee,numbers in total_notes.items():
            print(f"for {amount_withdraw} Rs,{rupee} Rs {numbers} notes")

    except ValueError as v:
        logger.error(f"Error in draw cash function:{v}")

def main():
    try:
        display_atm_amount()
        display_total_amount()
        amount_withdraw = int(input("\nEnter amount you want to withdraw form ATM: "))
        draw_cash(amount_withdraw)
        display_atm_amount()
        display_total_amount()
    except Exception as e:
        logger.error("Error in main: %s",e)
        main()


if __name__=="__main__":
    main()