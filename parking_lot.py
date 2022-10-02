# Your parking gargage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# - leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)
# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary
<<<<<<< HEAD
=======

class ParkingGarage:
    def __init__(self, ticket, space, currentTicket):
        self.ticket = ticket
        self.space = space
        # self.leave = leave
        self.currentTicket = currentTicket

    def takeTicket(self):
        # self.ticket = ticket
        self.currentTicket = {}
        if len(self.ticket) == 0:
            print('There are no more tickets available.')
            
        else:
            open_realestate = self.ticket.pop(0)
            print(f"Park in space {open_realestate}")
            self.currentTicket[open_realestate] = "You haven't paid"
            # takeTicket -= 1
            
            self.space.append(open_realestate)
            
    def payForParking(self):
        
        open_realestate = input("Which space where you in?: ")

        if self.currentTicket[open_realestate] == "You haven't paid":
            pay = input("Please type 'pay' to pay. ")
            if pay.lower() == 'pay':
                self.currentTicket[open_realestate] = "paid"
                print("You're all set, have a great day.")
                
            else:
                print("Please type a valid response. pay for your shit")
        # elif self.currentTicket[open_realestate] == "paid"



        # while True:
        #     if paid > ticket:
        #         break
        #     else:
        #         return "Thank you, have a nice day!"
        # for payForParking in payForParking == 0:
        #     print("There are no available spots.")
        # parking += 1
        # pass

    def leaveGarage(self):
        
        leaving = ("Enter your parking space to leave garage: ")

        if self.currentTicket[leaving] == "paid":
            self.space.remove(leaving)
            self.ticket.append(leaving)
            self.ticket.sort()
            del self.currentTicket[leaving]
        else:
            return self.payForParking()
        # elif leaving == 'n':
        
        # else:
        #     print("Please type a valid response you twat.")

    # def currentTicket(self):
    #     pass
parking = ['p1','p2','p3','p4','p5','p6','p7','p8','p9']
e_t_parking = ParkingGarage(parking,[],{})
# paid = 10

def runnit():
    
>>>>>>> 43ef758c0dc38b6e305ab7fe09f3f1b62592a957
