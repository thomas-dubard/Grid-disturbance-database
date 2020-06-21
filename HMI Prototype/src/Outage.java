import java.awt.*;
import java.awt.event.*;
import java.io.*;
/**
 * Class conceived to create a window for Outage inputs
 *
 */
public class Outage extends Frame implements ActionListener {

	private Button save;
	
	private Label sysuLabel;
	private TextField sysu;
	private Label ftLabel;
	private TextField ft;
	private Label tsysuLabel;
	private Choice tsysu;
	private Label ensLabel;
	private TextField ens;
	private Label interruptionLabel;
	private TextField interruption;
	private Label characLabel;
	private Choice charac;
	private Label reclosingLabel;
	private Choice reclosing;
	private Label outageLabel;
	private TextField outage;

	/**
	 * Creates a new instance of Outage, displaying a window to save a new outage
	 */
	public Outage () {
		sysuLabel = new Label("System unit");
		sysu = new TextField(40);
		
		ftLabel = new Label("Fault causing the outage");
		ft = new TextField(40);
		
		tsysuLabel = new Label ("Type of system unit");
		tsysu = new Choice ();
		tsysu.add("Power transformer");
		tsysu.add("Overhead line");
		tsysu.add("Cable");
		tsysu.add("Reactor");
		tsysu.add("Bushbar");
		tsysu.add("Series capacitor");
		tsysu.add("Shunt capacitor");
		tsysu.add("SVC");
		
		ensLabel = new Label ("Energy not supplied");
		ens = new TextField (40);
		
		interruptionLabel = new Label ("Duration of interruption");
		interruption = new TextField (40);
		
		characLabel = new Label ("Characterisation of the disconnection");
		charac = new Choice ();
		charac.add("Automatically");
		charac.add("Automatically with unsuccessful automatic reclosing");
		charac.add("Manually");
		
		reclosingLabel = new Label ("Characterisation of reclosing");
		reclosing = new Choice ();
		reclosing.add("Automatically after less than 2 seconds");
		reclosing.add("Automatically after more than 2 seconds");
		reclosing.add("Manually after restructuring of operation");
		reclosing.add("Manually after inspection");
		reclosing.add("Manually after repair");
		reclosing.add("Manually without either inspection,"
				+ " repair or restructuring the operation");
		reclosing.add("Unknown");
		reclosing.add("Others");
		
		outageLabel = new Label("Duration of outage");
		outage = new TextField(40);
		
		save= new Button("Save");
		setLayout(new GridLayout (5,4));
		
		add(sysuLabel);
		add(sysu);
		add(ftLabel);
		add(ft);
		add(tsysuLabel);
		add(tsysu);
		add(ensLabel);
		add(ens);
		add(interruptionLabel);
		add(interruption);
		add(characLabel);
		add(charac);
		add(reclosingLabel);
		add(reclosing);
		add(outageLabel);
		add(outage);
		
		add(save);
		save.addActionListener(this);
		addWindowListener(new EcouteurPourFermetureFenetre());
	}
	/**
	 * When the "Save" Button is clicked, all the data inserted is converted to String,
	 * the different components being separated by the "%" symbol. This String is written in ToSave.txt file. 
	 */
	public void actionPerformed (ActionEvent e) {
		if (e.getSource()==save) {
			try {
				PrintWriter out = new PrintWriter (new FileWriter("ToSave.txt",true));
				out.println("Outage%"+sysu.getText()+"%"+ft.getText()+"%"+tsysu.getSelectedItem()
				+"%"+ens.getText()+"%"+interruption.getText()+"%"+charac.getSelectedItem()+"%"
				+reclosing.getSelectedItem()+"%"+outage.getText());
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
