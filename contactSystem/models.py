from django.db import connection

# Create your models here.


def get_user_id(userName = None, pwd = None):
    user_id = 0;
    cur=connection.cursor()
    if userName is not None:
        cur.execute("SELECT * FROM users")
        details = cur.fetchall()
        for user in details:
            if user[1] == userName and user[2] == pwd:
                user_id = user[0]
                break
        if user_id != 0:
            return user_id
        else:
            return 0
    else:
        return 0
    
def get_contact_list(id_user = 0):
    cur=connection.cursor()
    cur.execute("SELECT * FROM userContactList WHERE userId=%s", (id_user, ))
    contact_list = cur.fetchall()
    return(contact_list)

def get_contact_details(id_user = 0):
    cur=connection.cursor()
    cur.execute("SELECT * FROM userContactList WHERE contactId=%s", (id_user, ))
    contact_details = cur.fetchone()
    return(contact_details)


