package school;

public class Junior extends Student {
	static final byte studentGrade = 11;
	short satScore;
	byte grade;
	
	public Junior(String firstName, String lastName, String[] studentClasses) {
		super(firstName, lastName, studentGrade, studentClasses);
		Junior.this.grade = studentGrade;
	}
	
	public void completeSat(byte hoursStudied) {
		Junior.this.satScore = (short) (hoursStudied * hoursStudied * 100);
		if (Junior.this.satScore > 1600) {
			Junior.this.satScore = 1600;
		}
		System.out.println(Junior.this.fName + " has a SAT score of: ");
		System.out.println(Junior.this.satScore);
	}
	
	public void visitColleges (String[] colleges) {
		for (byte c = 0; c < colleges.length; c++) {
			System.out.println("You have visited " +  colleges[c] + " university");
		}
	}
}
