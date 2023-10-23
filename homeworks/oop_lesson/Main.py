from DataBase import DataBase
from Record import Record

if __name__ == "__main__":
    #DataBase.Record = Record
    # db = DataBase.DataBase("user1", "12345", 80)
    # db2 = DataBase.DataBase("user2", "23445", 80)
    # print(db, db2, sep="\n")
    # print(db.user, db.password, db.port, sep="\n")
    db = DataBase("user1", "12345", 80)
    rec_1 = Record("Katya", 23, "Female")
   
    db.records = ["Katya", "Alisher", 80]
    print(db.records)
    

    