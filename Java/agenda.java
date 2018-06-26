import java.util.Scanner;
import java.util.Calendar;

class agenda {
	public static void main(String[] args) {
		//initialization
		Calendar calendar = Calendar.getInstance();
		// calendar.set(year, month, day);
		int today = calendar.get(calendar.DAY_OF_WEEK);
		Scanner in = new Scanner(System.in);
		String[] days = {"Monday", "Tuesday" , "Wednesday", "Thursday",
										 "Friday", "Saturday", "Sunday"};
		int[] time = {24, 24, 24, 24, 24, 24, 24};

		//Initial prompt
		System.out.println("Welcome to the agenda! How may I help you?");
		String input = in.nextLine();
		if (input.equals("today"))
			System.out.println("\n"+days[today-2]+"'s Agenda: ");
		else System.out.println("I don't understand.");



		// for (int i = 0; i < time.length; i++) System.out.println(days[i] + " : "+ time[i]);

		System.out.println("\nNothing more for me to do! bye bye!");
	}
}
