
import java.awt.*;
import java.awt.event.*;

import py4j.GatewayServer;
/*import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertTrue;*/

/**
 * An instance of App will generate a window on which 4 choices are available depending on whether disturbance, fault, outage or interruption is to be recorded.
 * @author Leconte
 *
 */

public class App extends Frame implements ActionListener {
	private Choice table;
	private Button ok;
	public FlowLayout f;
	private Label msg;
	public Disturbance dist;
	
	/**
	 * Constructor App creates a new instance of App, generating a window on which 4 choices are available depending on whether disturbance, fault, outage or interruption is to be recorded.
	 */
	public App () {
		table = new Choice ();
		table.add("------");
		table.add("Disturbance");
		table.add("Fault");
		table.add("Outage");
		table.add("Interruption");
		
		ok = new Button("OK");
		
		f=new FlowLayout();
		
		msg = new Label();
		msg.setText("Please select a table for a new entry");
		
		setLayout(f);   
		add(table);
		add(ok);
		add(msg);
		
		addWindowListener(new EcouteurPourFermetureFenetre()); 
		ok.addActionListener(this);
	}
	/**
	 * Creates a new instance of App and waits for a python script to interact with it threw the py4j module. Please see the cote_python.py documentation for further informations.
	 * @param args
	 * 			Should not be completed
	 */
	public static void main(String[] args) {
		 App appli = new App();
		 appli.setLocation(100, 100);
		 appli.setSize(600, 450);
		 appli.setVisible(false);
		GatewayServer server = new GatewayServer(appli);
	    server.start();
	}
	/**
	 * Closes the App window and opens a Disturbance/Outage/Fault/Interruption window according to which table is selected on the App window when the "OK" button is clicked. If no table is selected, "Please select a valid table is displayed".
	 * 
	 * @param evt
	 * 			An ActionEvent, it does have consequences only when the "OK" button is clicked.
	 * @see Disturbance
	 * @see Outage
	 * @see Fault
	 * @see Interruption
	 */
	public void actionPerformed(ActionEvent evt) {
		if (evt.getSource()==ok) {
			String item = table.getSelectedItem();
			switch (item) {
			case "Disturbance":
				
				this.setVisible(false);
				dist = new Disturbance ();
				dist.setVisible(true);
				dist.setSize(600, 450);
				break;
			case "Fault":
				this.setVisible(false);
				Fault ft = new Fault ();
				ft.setVisible(true);
				ft.setSize(1200,200);
				break;
			case "Outage":
				this.setVisible(false);
				Outage otg = new Outage ();
				otg.setVisible(true);
				otg.setSize(600,450);
				break;
			case "Interruption":
				this.setVisible(false);
				Interruption inter = new Interruption ();
				inter.setVisible(true);
				inter.setSize(600,450);
				break;
			default:
				msg.setText("Please select a valid table");
				break;
			}
		}
	}
}
