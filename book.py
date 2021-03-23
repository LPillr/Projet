###########################################################################
################################## CLASS ##################################
###########################################################################
class Book(str):
    
    #Global variable
    global id
    id=0
    global order_list 
    order_list = []

    def __init__(self, book_name):
        self.bookName = book_name 
        
    def insert_buy(self, qtty, price):
        global id 
        id+=1
        order_list.append(Order(qtty,price,0,id))
        print("---"+" Insert BUY "+str(qtty)+"@"+str(price)+" id="+str(id)+ " on "+ self.bookName)
        Book.orderpassing(self,Order(qtty,price,0,id)) #I pass order if it's possible
        Book.show_book(self)
        
    def insert_sell(self,qtty,price):
        global id 
        id+=1
        order_list.append(Order(qtty,price,1,id))
        print("---"+" Insert SELL "+str(qtty)+"@"+str(price)+" id="+str(id)+ " on "+ self.bookName)
        Book.orderpassing(self,Order(qtty,price,1,id)) #I pass order if it's possible
        Book.show_book(self)
        
    def show_book(self): #display
        orderbytype()
        orderbyprice()
        orderbyquantity()
        print("Book on " + self.bookName)
        for order in order_list:
            print("     "+sellorbuy(order.types)+" "+str(order.qtty)+"@"+str(order.price)+" id="+str(order.uniqid))
        print("---------------------")
    
    
    def orderpassing(self,s):
        if s.types==1:
            for b in order_list:
                if b.types==0: #b is a buy
                    if s.qtty!=0:
                        if s.price <= b.price :
                            
                            if s.qtty < b.qtty:
                                del(order_list[len(order_list)-1]) #s.qtty=0, we delete it 
                                b.qtty=b.qtty-s.qtty
                                print ("Execute "+ str(s.qtty)+ " at "+str(b.price)+" on "+self.bookName)
                                s.qtty=0
                                return
                                
                            
                            if s.qtty > b.qtty:
                                s.qtty=s.qtty-b.qtty
                                del(order_list[order_list.index(b)]) #b.qtty=0, we delete it 
                                print("Execute "+ str(b.qtty)+ " at "+str(b.price)+" on "+self.bookName)
                                Book.orderpassing(self,s)
                                
                            else :
                                s.qtty=0
                                del(order_list[order_list.index(b)]) #both qtty are null
                                del(order_list[len(order_list)-1]) #we delete them
                                print ("Execute "+ str(b.qtty)+ " at "+str(b.price)+" on "+self.bookName)
                                return
        else :
            for o in order_list:
                if o.types==1: #i need to verirify that I don't have a seller for my buyer
                    Book.orderpassing(self, o)
                

