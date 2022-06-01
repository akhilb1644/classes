package kingPackage;

public class main {
	public static void main(String[] args) {
		King gustav = new King("Gustav I","Vasa","Sweden");
		King cOld = new King("Christian II","Oldenberg","Denmark","Norway");
		
		cOld.printGeneralInfo();
		gustav.doDiplomacy("Muscovy");
		cOld.printPlacesRuled();
	}
}
