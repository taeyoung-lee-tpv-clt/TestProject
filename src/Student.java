public class Student{
        //Constructor OverLoading
        public int studentId;
        public String studentName;
        public String address;
    
        public Student(int id, String name){
            studentId = id;
            studentName = name;
        }
    
        public Student(String name){
            this.studentName = name;
        }
    
    }
