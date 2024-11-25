from datetime import datetime  #Modulo nativo de python

def get_current_date():
    return datetime.now().strftime("%d-%m-%Y")


def date_difference(date1, date2):
    formato = "%d/%m/%y"
    d1 = datetime.strptime(date1, formato)
    d2 = datetime.strptime(date2, formato)
    diferencia = abs((d2 - d1).days)
    
    return diferencia