from app import mysql

class Student:
    @staticmethod
    def get_all(search=None, sort_by='id', sort_order='asc'):
        cursor = mysql.get_db().cursor()
        valid_sort_columns = {'id', 'firstname', 'lastname', 'program_name', 'year', 'gender'}
        if sort_by not in valid_sort_columns:
            sort_by = 'id'
        if sort_order not in ['asc', 'desc']:
            sort_order = 'asc'
            
        # Map program_name to p.name for sorting
        sort_column = 'p.name' if sort_by == 'program_name' else f's.{sort_by}'
        order_clause = f"ORDER BY {sort_column} {sort_order.upper()}"
        
        if search:
            query = f"""
                SELECT s.*, p.name as program_name 
                FROM student s 
                LEFT JOIN program p ON s.course_code = p.code 
                WHERE s.id LIKE %s OR s.firstname LIKE %s 
                OR s.lastname LIKE %s OR s.course_code LIKE %s
                {order_clause}
            """
            search_term = f"%{search}%"
            cursor.execute(query, (search_term, search_term, search_term, search_term))
        else:
            cursor.execute(f"""
                SELECT s.*, p.name as program_name 
                FROM student s 
                LEFT JOIN program p ON s.course_code = p.code
                {order_clause}
            """)
        return cursor.fetchall()
    
    @staticmethod
    def get_by_id(student_id):
        cursor = mysql.get_db().cursor()
        cursor.execute("""
            SELECT s.*, p.name as program_name 
            FROM student s 
            LEFT JOIN program p ON s.course_code = p.code 
            WHERE s.id = %s
        """, (student_id,))
        return cursor.fetchone()
    
    @staticmethod
    def create(data):
        cursor = mysql.get_db().cursor()
        cursor.execute("""
            INSERT INTO student (id, firstname, lastname, course_code, year, gender, photo_url) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (data['id'], data['firstname'], data['lastname'], 
              data['course_code'], data['year'], data['gender'], data.get('photo_url')))
        mysql.get_db().commit()
    
    @staticmethod
    def update(student_id, data):
        cursor = mysql.get_db().cursor()
        cursor.execute("""
            UPDATE student 
            SET firstname=%s, lastname=%s, course_code=%s, year=%s, gender=%s, photo_url=%s 
            WHERE id=%s
        """, (data['firstname'], data['lastname'], data['course_code'], 
              data['year'], data['gender'], data.get('photo_url'), student_id))
        mysql.get_db().commit()
    
    @staticmethod
    def delete(student_id):
        cursor = mysql.get_db().cursor()
        cursor.execute("DELETE FROM student WHERE id=%s", (student_id,))
        mysql.get_db().commit()


class Program:
    @staticmethod
    def get_all(search=None, sort_by='code', sort_order='asc'):
        cursor = mysql.get_db().cursor()
        valid_sort_columns = {'code', 'name', 'college_name'}
        if sort_by not in valid_sort_columns:
            sort_by = 'code'
        if sort_order not in ['asc', 'desc']:
            sort_order = 'asc'
            
        # Map college_name to c.name for sorting
        sort_column = 'c.name' if sort_by == 'college_name' else f'p.{sort_by}'
        order_clause = f"ORDER BY {sort_column} {sort_order.upper()}"
        
        if search:
            query = f"""
                SELECT p.*, c.name as college_name 
                FROM program p 
                LEFT JOIN college c ON p.college_code = c.code 
                WHERE p.code LIKE %s OR p.name LIKE %s
                {order_clause}
            """
            search_term = f"%{search}%"
            cursor.execute(query, (search_term, search_term))
        else:
            cursor.execute(f"""
                SELECT p.*, c.name as college_name 
                FROM program p 
                LEFT JOIN college c ON p.college_code = c.code
                {order_clause}
            """)
        return cursor.fetchall()
    
    @staticmethod
    def get_by_code(code):
        cursor = mysql.get_db().cursor()
        cursor.execute("""
            SELECT p.*, c.name as college_name 
            FROM program p 
            LEFT JOIN college c ON p.college_code = c.code 
            WHERE p.code = %s
        """, (code,))
        return cursor.fetchone()
    
    @staticmethod
    def create(data):
        cursor = mysql.get_db().cursor()
        cursor.execute("""
            INSERT INTO program (code, name, college_code) 
            VALUES (%s, %s, %s)
        """, (data['code'], data['name'], data['college_code']))
        mysql.get_db().commit()
    
    @staticmethod
    def update(code, data):
        cursor = mysql.get_db().cursor()
        cursor.execute("""
            UPDATE program 
            SET name=%s, college_code=%s 
            WHERE code=%s
        """, (data['name'], data['college_code'], code))
        mysql.get_db().commit()
    
    @staticmethod
    def delete(code):
        cursor = mysql.get_db().cursor()
        cursor.execute("DELETE FROM program WHERE code=%s", (code,))
        mysql.get_db().commit()


class College:
    @staticmethod
    def get_all(search=None, sort_by='code', sort_order='asc'):
        cursor = mysql.get_db().cursor()
        valid_sort_columns = {'code', 'name'}
        if sort_by not in valid_sort_columns:
            sort_by = 'code'
        if sort_order not in ['asc', 'desc']:
            sort_order = 'asc'
            
        order_clause = f"ORDER BY {sort_by} {sort_order.upper()}"
        
        if search:
            query = f"SELECT * FROM college WHERE code LIKE %s OR name LIKE %s {order_clause}"
            search_term = f"%{search}%"
            cursor.execute(query, (search_term, search_term))
        else:
            cursor.execute(f"SELECT * FROM college {order_clause}")
        return cursor.fetchall()
    
    @staticmethod
    def get_by_code(code):
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT * FROM college WHERE code = %s", (code,))
        return cursor.fetchone()
    
    @staticmethod
    def create(data):
        cursor = mysql.get_db().cursor()
        cursor.execute("""
            INSERT INTO college (code, name) 
            VALUES (%s, %s)
        """, (data['code'], data['name']))
        mysql.get_db().commit()
    
    @staticmethod
    def update(code, data):
        cursor = mysql.get_db().cursor()
        cursor.execute("""
            UPDATE college 
            SET name=%s 
            WHERE code=%s
        """, (data['name'], code))
        mysql.get_db().commit()
    
    @staticmethod
    def delete(code):
        cursor = mysql.get_db().cursor()
        cursor.execute("DELETE FROM college WHERE code=%s", (code,))
        mysql.get_db().commit()