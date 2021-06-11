import sqlite3

class StudyDataDB(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):         # Foo 클래스 객체에 _instance 속성이 없다면
            print("__new__ is called\n")
            cls._instance = super().__new__(cls)  # Foo 클래스의 객체를 생성하고 Foo._instance로 바인딩
        return cls._instance                      # Foo._instance를 리턴

    def __init__(self):
        cls = type(self)
        if not hasattr(cls, "_init"):             # Foo 클래스 객체에 _init 속성이 없다면
            print("__init__ is called\n")
            
            cls._init = True
                        
            self.DB_NAME = "keep_studying.db" 

    def select(self):
        
        conn = sqlite3.connect(self.DB_NAME)
        cursor = conn.cursor()
        
        #오늘 날짜에 해당하는 애들 추가
        cursor.execute("select * from today_studying_number where DATE = date('now', 'localtime');")

        study_record = []
        for i in cursor.fetchall():
            study_record.append(list(i))
        
        conn.close()

        return study_record

    def delete(self):
        conn = sqlite3.connect(self.DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute(f"delete from today_studying_number where DATE < date('now','-2 day')")

        conn.commit()
        conn.close()
    
    def insert(self,complete):           

        conn = sqlite3.connect(self.DB_NAME)
        cursor = conn.cursor()
        
        cursor.execute(f"insert into today_studying_number(complete) values({complete})")

        conn.commit()
        conn.close()


    
    