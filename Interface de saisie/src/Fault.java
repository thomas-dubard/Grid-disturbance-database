import java.awt.*;
import java.awt.event.*;
import java.io.*;

public class Fault extends Frame implements ActionListener{
	private Label serialLabel;
	private TextField serial;
	private Label distLabel;
	private TextField dist;
	private Label compLabel;
	private Choice comp;
	private Label voltLabel;
	private Choice volt;
	private Label sysgrLabel;
	private Choice sysgr;
	private Label nwkLabel;
	private Choice nwk;
	private Label cfsdLabel;
	private Choice cfsd;
	private Label fttLabel;
	private Choice ftt;
	private Label repairLabel;
	private TextField repair;
	
	private Button save;
	
	public Fault () {
		serialLabel= new Label("Serial Number");
		serial = new TextField(40);
		
		distLabel = new Label ("Reference to grid disturbance");
		dist = new TextField(40);
		
		compLabel = new Label("Component type");
		comp = new Choice();
		comp.add("None");
		comp.add("Unknown");
		comp.add("Surge arresters and spark gaps");
		comp.add("Circuit breakers");
		comp.add("Disconnectors and earth connectors");
		comp.add("Foundations Isolator(s)");
		comp.add("Common ancillary equipment");
		comp.add("Control equipment");
		comp.add("Power cables");
		comp.add("Power transformers");
		comp.add("Overhead lines");
		comp.add("Instrument transformers");
		comp.add("Reactors inclusive of neutral point reactors");
		comp.add("Synchronous compensators");
		comp.add("Bushbars");
		comp.add("Series capacitors");
		comp.add("Shunt capacitors batteries and filters");
		comp.add("SVC and statcom");
		comp.add("Other high-voltage component in stations");
		
		voltLabel = new Label ("Voltage level");
		volt = new Choice();
		volt.add("100-150kV");
		volt.add("220-330kV");
		volt.add("380-420kV");
		
		sysgrLabel = new Label ("System grounding");
		sysgr = new Choice ();
		sysgr.add("Directly earthed");
		sysgr.add("Compensated");
		
		nwkLabel = new Label("Statistical area");
		nwk = new Choice ();
		nwk.add("Own network");
		nwk.add("Other network");
		
		cfsdLabel = new Label ("Component fault or system disturbance");
		cfsd = new Choice ();
		cfsd.add("Component fault");
		cfsd.add("System disturbance");
		
		fttLabel= new Label("Fault type");
		ftt = new Choice ();
		ftt.add("Single-phase earth fault");
		ftt.add("Two or three-phase with or without earth fault");
		ftt.add("Function failing to occur");
		ftt.add("Undesidered function");
		ftt.add("Oscillation");
		ftt.add("Overload");
		ftt.add("Broken conductor without earth contact");
		ftt.add("Others");
		
		repairLabel = new Label ("Repair time");
		repair = new TextField (40);
		
		
		save= new Button("Save");
		setLayout(new GridLayout (5,4));
		
		add(serialLabel);
		add(serial);
		add(distLabel);
		add(dist);
		add(compLabel);
		add(comp);
		add(voltLabel);
		add(volt);
		add(sysgrLabel);
		add(sysgr);
		add(nwkLabel);
		add(nwk);
		add(cfsdLabel);
		add(cfsd);
		add(fttLabel);
		add(ftt);
		add(repairLabel);
		add(repair);
		
		
		add(save);
		save.addActionListener(this);
		addWindowListener(new EcouteurPourFermetureFenetre()); 
		
	}
	
	public void actionPerformed (ActionEvent e) {
		if (e.getSource()==save) {
			try {
				PrintWriter out = new PrintWriter (new FileWriter("ToSave.txt",true));
				out.println("Fault%"+serial.getText()+"%"+dist.getText()+"%"
				+comp.getSelectedItem()+"%"+volt.getSelectedItem()+"%"
				+sysgr.getSelectedItem()+"%"+nwk.getSelectedItem()+"%"
				+cfsd.getSelectedItem()+"%"+ftt.getSelectedItem()+"%"
				+repair.getText());
				out.close();
			}
			catch (FileNotFoundException e1) {
				System.err.println("Text file can't be read");
			}
			catch (IOException e2) {
				System.err.println("Input-Output error");				
			}
		}
	}
}
