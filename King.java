package kingPackage;

public class King {

	protected String name;
	protected String dynasty;
	protected String[] location;
	
	public King(String kingName,String kingDynasty, String... kingLocation) { // That constructer that is required for classes
		name = kingName;
		dynasty = kingDynasty;
		location = kingLocation;
	}
	
	public String getName() { // Returns monarch name.
		return name;
	}
	
	public void printGeneralInfo() { // Get some general information of the monarch stored in the variable(in main class)
		System.out.println(name + " of the " + dynasty + " Dynasty ruled:");
		for (int j = 0; j < location.length; j++) {
			int n = j + 1;
			System.out.println(n + ". " + location[j]);
		}
	}
	
	public void doDiplomacy(String Location) { // Conduct diplomacy with said nation
		System.out.println("Diplomacy with " + Location + " successful!");
	}
	
	public void changeTaxes(float Tax) { // Hike the taxes, lower them, your choice.
		System.out.println("Tax rate changed to " + Tax + " percent.");
	}
	
	public void printTitle() { // Print your title
		System.out.println(name + ", King of " + location);
	}
	
	public void printPlacesRuled() { // Print all the places you rule(some kings rule more than one place)
		System.out.println(name + " rules: ");
		for (int i = 0; i < location.length ; i++) {
			int j = i + 1;
			System.out.println(j + ". " + location[i]);
		}
		}
}
