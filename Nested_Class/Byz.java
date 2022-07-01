package Nested_Class;

public class Byz { // This is the outer class
	String name;
	String dynasty;

	class lekapenos { // This is the nested class, or the inner class
		public lekapenos(String name) {
			Byz.this.name = name;
			Byz.this.dynasty = "Lekapenos";
		}
		
		void print_emp() {
			if (Byz.this.name == "Romanos I") {
				System.out.println(name+": Looks like you want to tax the rich.\n");
			}
			else {
				System.out.println(name+": I have never heard of them!\n");
			}
		}
	}
}
