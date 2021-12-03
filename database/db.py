import os.path
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
db_path = os.path.join(BASE_DIR, "students.db")

class DataBase:
    def __init__(self):
        self.conn = sqlite3.connect(db_path, check_same_thread=False) 
        self.cursor = self.conn.cursor()
        
    def create(self):
        self.cursor.execute("CREATE TABLE questions (que_id INTEGER, que TEXT, opt1 TEXT, opt2 TEXT, opt3 TEXT, opt4 TEXT, ans INTEGER)")
        print('done')

    def write(self):
        test = [
            (2, 'In the Hofmann bromamide degradation reaction, the number of moles of NaOH and Br2 used per mole of amine produced are', 'Four moles of NaOH and two moles of Br2', 'Two moles of NaOH and two moles of Br2', 'Four moles of NaOH and one mole of Br2', 'One mole of NaOH and one mole of Br2', 3),
            (3, 'The surface considered for Gauss’s law is called', 'Closed surface', 'Spherical surface', 'Gaussian surface', 'Plane surface', 3),
            (4, 'Which of the following statements is not true about Gauss’s law?', ' Gauss’s law is true for any closed surface', 'The term q on the right side side of Gauss’s law includes the sum of all charges enclosed by the surface', 'Gauss’s law is not much useful in calculating electrostatic field when the system has some symmetry', 'Gauss’s law is based on the inverse square dependence on distance contained in the coulomb’s law',3),
            (5, 'The force per unit charge is known as', 'electric flux', 'electric field', 'electric potential' , 'electric current', 2),
            (6, 'A charged particle is moving in a cyclotron, what effect on the radius of path of this charged particle will occur when the frequency of the ratio frequency field is doubled?',  'It will also be doubled.', 'It will be halved.', 'It will be increased by four times.', 'it will remain unchanded', 4),
            (7, 'The nature of parallel and anti-parallel currents are', 'parallel currents repel and antiparallel currents attract.', 'parallel currents attract and antiparallel cur-rents repel', 'both currents attract', 'both currents repel', 2),
            (8, 'The magnetic moment of a current I carrying circular coil of radius r and number of turns N varies as ', ' 1r² ', '1r ', 'r', ' r²', 4),
            (9, 'A short bar magnet has a magnetic moment of 0. 65 J T-1, then the magnitude and direction of the magnetic field produced by the magnet at a distance 8 cm from the centre of magnet on the axis is', '2.5 × 10-4 T, along NS direction', '2.5 × 10-4 T along SN direction', '4.5 × 10-4 T, along NS direction', '4.5 × 10-4 T, along SN direction', 2),
            (10,'A current carrying loop is placed in a uniform magnetic field. The torqe acting on it does not depend upon', 'area of loop', 'value of current', 'magnetic field', 'None of these',4)
        ]
        for data in test:
            self.cursor.execute(f"INSERT INTO questions VALUES ({data[0]}, '{data[1]}', '{data[2]}', '{data[3]}', '{data[4]}', '{data[5]}', {data[6]})")
            self.conn.commit()
        print('done') 

    def fetch(self, email):
        data = self.cursor.execute(f"SELECT * FROM students WHERE email='{email}'").fetchone()
        return data
    
    def fetch_que(self, que_id):
        if que_id == 0:
            data = self.cursor.execute(f"SELECT * FROM questions").fetchall()
            return data
        else:
            data = self.cursor.execute(f"SELECT * FROM questions WHERE que_id={que_id}").fetchone()
            response = {
                'que_id': data[0],
                'que': data[1],
                'opts': {
                    'A': data[2], 
                    'B': data[3], 
                    'C': data[4], 
                    'D': data[5]
                },
                'ans': data[6]
            }
            return response