package school;

public class Student {
	String fName;
	String lName;
	byte grade;
	String[] classes;
	
	public Student(String firstName,String lastName,byte studentGrade,String[] studentClasses) {
		Student.this.fName = firstName;
		Student.this.lName = lastName;
		Student.this.grade = studentGrade;
		Student.this.classes = studentClasses;
	}
	
	protected void attendClass(String course) { // This is where access modifiers are used
		// These modifiers prevent people from attending one class
		System.out.println(Student.this.fName + " attended " + course + " class.");
	}
	
	public void attendSchool() {
		for (byte i = 0;i < Student.this.classes.length;i++) { // Students must attend all classes
			// At least in this simulation they do
			attendClass(Student.this.classes[i]);
		}
	}
	
	public void graduate() {
		Student.this.grade = (byte) (Student.this.grade + 1);
		System.out.println(fName + " you have just graduated to grade: ");
		System.out.println(Student.this.grade);
	}
}