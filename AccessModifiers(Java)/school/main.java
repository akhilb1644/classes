package school;

public class main {
	public static void main(String[] args) {
		String[] courses = new String[]{"Math II","Health","AP World","Spanish II"};
		Student nabiyev = new Student("Rahmon","Nabiyev",(byte) 10,courses);
		System.out.println(nabiyev.grade);
		nabiyev.graduate();
		nabiyev.attendSchool();
		/* Output of above portion of program should be
		 * 10
		 * Rahmon you have just graduated to grade: 
		 * 11
		 * Rahmon attended Math II class.
		 * Rahmon attended Health class.
		 * Rahmon attended AP World class.
		 * Rahmon attended Spanish II class.*/
		String[] courses2 = new String[]{"AP Calculus AB","English III","AP Environmental Science"};
		Junior rahmon = new Junior("Emomali","Rahmon",courses2);
		rahmon.attendSchool();
		rahmon.completeSat((byte) 3);
		String[] colleges = new String[]{"Duke","Chapel Hill","Harvard","Iowa State"};
		rahmon.visitColleges(colleges);
		/* Output of above should be:
		 * Emomali attended AP Calculus AB class.
		 * Emomali attended English III class.
		 * Emomali attended AP Environmental Science class.
		 * Emomali has a SAT score of: 
		 * 900
		 * You have visited Duke university
		 * You have visited Chapel Hill university
		 * You have visited Harvard university
		 * You have visited Iowa State university */
	}
}
