import java.awt.*;
import java.awt.event.*;
import java.io.*;

public class Interruption extends Frame implements ActionListener {
	
	private Button save;
	
	private Label delPointLabel;
	private TextField delPoint;
	private Label durationLabel;
	private TextField duration;
	private Label disturbanceLabel;
	private TextField disturbance;
	
	public Interruption () {
		delPointLabel= new Label ("Name of delivery point");
		delPoint = new TextField(40);
		
		durationLabel = new Label("Duration of interruption");
		duration = new TextField(40);
		
		disturbanceLabel = new Label ("Reference to grid disturbance");
		disturbance = new TextField (40);
		
		save= new Button("Save");
		setLayout(new GridLayout (2,4));
		
		add(delPointLabel);
		add(delPoint);
		add(durationLabel);
		add(duration);
		add(disturbanceLabel);
		add(disturbance);
		add(save);
		
		add(save);
		save.addActionListener(this);
		addWindowListener(new EcouteurPourFermetureFenetre()); 
	}
	public void actionPerformed (ActionEvent e) {
		if (e.getSource()==save) {
			try {
				PrintWriter out = new PrintWriter (new FileWriter("ToSave.txt",true));
				out.println("Interruption%"+delPoint.getText()+"%"+duration.getText()
				+"%"+disturbance.getText());
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
