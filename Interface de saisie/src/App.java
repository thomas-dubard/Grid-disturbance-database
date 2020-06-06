
import java.awt.*;
import java.awt.event.*;

public class App extends Frame implements ItemListener,ActionListener {
	private Choice table;
	private Button ok;
	public FlowLayout f;
	private Label msg;
	
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
	public static void main(String[] args) {
		 App appli = new App();
		 appli.setLocation(100, 100);
		 appli.setSize(600, 450);
		 appli.setVisible(true);
	}
	public void actionPerformed(ActionEvent evt) {
		if (evt.getSource()==ok) {
			String item = table.getSelectedItem();
			switch (item) {
			case "Disturbance":
				
				this.setVisible(false);
				Disturbance dist = new Disturbance ();
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
	

	@Override
	public void itemStateChanged(ItemEvent e) {
		// TODO Auto-generated method stub
		
	}
}
