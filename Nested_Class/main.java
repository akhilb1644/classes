package Nested_Class;

public class main {
	public static void main(String... args) {
		Byz byz= new Byz();
		Byz.lekapenos roma = byz.new lekapenos("Romanos I"); // Only emperor of Lekapenos dynasty
		roma.print_emp();
		Byz.lekapenos fake = byz.new lekapenos("Romanos II");
		fake.print_emp(); // This Byzantine emperor was not of the Lekapenos dynasty, this is just for getting false condition.
	}
}
