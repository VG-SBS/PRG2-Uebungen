import sqlite3

class DB:
    #Konstruktor
    def __init__(self):
        print("Konstruktor DB wurde aufgerufen")
        self.__connection = sqlite3.connect('game.db')
        self.__cursor = self.__connection.cursor()

        self.__cursor.execute('''
        CREATE TABLE IF NOT EXISTS scorelist
        (pk INTEGER PRIMARY KEY NOT NULL, pname TEXT, score INTEGER);
        ''')

        #self.__cursor.execute('''
        #Insert into scorelist Values(0,'Dummy',0)
        #''')
        self.__connection.commit()

    def createPlayer(self,pname):
        """
        Erzeugt einen neuen Spieler mit gegebenen Namen
        :param pname: Name des Spielers ...
        :return: gibt den Händler zum Spieler zurück
        """

        self.__cursor.execute('''
        SELECT MAX(pk) FROM scorelist;
        ''')
        ret = self.__cursor.fetchall()
        pk_max = ret[0][0]

        if pk_max == None:
            pk_max = 0
        else:
            pk_max += 1
        self.__cursor.execute('''
        INSERT INTO scorelist (pk, pname)VALUES("{}","{}");
        '''.format(pk_max,pname))
        self.__connection.commit()

        return pk_max

    def getPlayer(self,pk):
        """
        Hier wird der pk mitgegeben
        :param pk: pk ist der PK der Tabelle
        :return: Der Name des gegebenen PK wird zurückgegeben
        """
        self.__cursor.execute('''
        select pname from scorelist 
        where pk = "{}";
        '''.format(pk))
        name = self.__cursor.fetchall()
        return name[0][0]

    def setPlayerScore(self,scr,pk):
        """
        :param scr: der Score der gesetzt werden möchte
        :param pk: pk, wo der Score gesetzt wird
        """

        self.__cursor.execute('''
        update scorelist
        set score = "{}"
        where pk = "{}";'''.format(scr,pk))
        self.__connection.commit()

    def getPlayerScore(self,pk):
        """
        :param pk: PK der Tabelle, wo der Score ausgelesen wird
        :return: ausgelesener Score der gegebenen pk
        """

        self.__cursor.execute('''
        select score from scorelist
        where pk = "{}";
        '''.format(pk))
        score = self.__cursor.fetchall()
        return score[0][0]