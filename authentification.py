from database import Database


class Authentification:
    def __init__(self):
        self.dtb = Database()

    def set_new_user(self, last_name: str, name: str, email: str, passwd_hash: str):
        '''create new row in database
        Arguments:
            last_name -- str
            name -- str
            email -- str
            passwd_hash -- str  
        '''
        req = "INSERT INTO users(nom,prenom,email,password_hash) VALUES (%s,%s,%s,%s) "
        values = (last_name, name, email, passwd_hash)
        self.dtb.query(req, values)

    def read(self, email: str):
        '''read user row in tables users
        Returns:
            With email get all information user 
        '''
        req = "SELECT * FROM users where email = %s"
        value = (email,)
        return self.dtb.query(req, value)

    def update(self, colonne: str, new_name: str, user_id: int):
        '''update table users
        Arguments:
            colonne -- str name_column
            new_name -- str new information
            user_id -- INT id

        '''
        match(colonne):
            case 'nom':
                req = "UPDATE users SET nom = %s WHERE user_id = %s"
            case 'prenom':
                req = "UPDATE users SET prenom = %s WHERE user_id = %s"
            case 'email':
                req = "UPDATE users SET email = %s WHERE user_id = %s"
            case 'password_hash':
                req = "UPDATE users SET password_hash = %s WHERE user_id = %s"
            case _:
                print("Column name no found")
        values = (new_name, user_id)
        self.dtb.query(req, values, modif=True)
        print("users updated successfully")

    def delete(self, email: str):
        '''delete row in table users  

        Arguments:
            email -- email-inscription 
        '''
        req = "DELETE FROM users WHERE email = %s"

        value = (email,)
        self.dtb.query(req, value)
        print("users deleted successfully")

    def delete_all_users(self):
        req = "DELETE FROM users "
        self.dtb.query(req, None)
        print("All users deleted successfully")

    def get_Id_user(self, email: str):
        '''get user_id how send the message 

        Arguments:
            email -- user email

        Returns:
            User_id
        '''
        req = "SELECT user_id FROM users where email = %s"
        value = (email,)
        result = self.dtb.query(req, value)[0][0]
        return result


if __name__ == "__main__":

    gestion = Authentification()
    gestion.delete_all_users()
    # gestion.create("admin","admin","admin@admin2.com","admin")
    # gestion.update()
    # gestion.delete("magomed.agaev@gmail.com")
    # print(gestion.read('abdel.ben-ahmed@hotmail.fr'))
    # gestion.close_all()
    # print(gestion.get_Id_user('admin@admin.com'))
