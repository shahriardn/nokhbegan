from model.admin import admin as conadmin
from persiantools.jdatetime import JalaliDate

class db:
    def selectuserswaitinglevel():
        return conadmin().select("""
                                      user."melli-code",
                                      user.name,
                                      user.fname,
                                      user.grade,
                                      user.tel,
                                      user.address,
                                      level.mellicode
            """, 'user').joinit('LEFT', 'level', ' level.mellicode = user."melli-code"').where(' level.mellicode IS NULL').fetchall()
    def selectalluser():
        return conadmin().select('*', 'user').fetchall()
    def selectalldoreh():
        return conadmin().select('*', 'doreh').orderby('id', 'DESC').fetchall()

class date:
    def today():
        return JalaliDate.today()
