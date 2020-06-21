import java.awt.*;
import java.awt.event.*;
import java.io.*;

/**
 * Class conceived to create a window for Disturbance inputs
 *
 */
public class Disturbance extends Frame implements ActionListener {
	private Label idlabel;
	private TextField id;
	private Label datelabel;
	private TextField date;
	private Label timelabel;
	private TextField time;
	private Button save;
	private Label msg;
	public String saving;
	public Boolean hasSaved;
	
	
	/**
	 * Creates a new instance of disturbance, displaying a window to save a new disturbance
	 */
	public Disturbance () {
		id = new TextField(40);
		idlabel = new Label("ID");
		date = new TextField(40);
		datelabel = new Label("Date");
		time = new TextField(40);
		timelabel = new Label("Time");
		save = new Button("Save");
		msg = new Label();
		saving = "";
		hasSaved = false;
		
		setLayout(new GridLayout (4,2));
		
		add(idlabel);
		add(id);
		add(datelabel);
		add(date);
		add(timelabel);
		add(time);
		add(save);
		add(msg);
		
		msg.setVisible(false);
		
		
		
		save.addActionListener(this);
		addWindowListener(new EcouteurPourFermetureFenetre()); 

		
	}
	/**
	 * When the "Save" Button is clicked, all the data inserted is converted to String,
	 * the different components being separated by the "%" symbol. This String is written in ToSave.txt file. 
	 */
	public void actionPerformed(ActionEvent e) {
		if (e.getSource()==save) {
			// do the saving
			try {
				PrintWriter out = new PrintWriter (new FileWriter("ToSave.txt",true));
				saving ="Disturbance%"+id.getText()+"%"+date.getText()+"%"+time.getText()+"\n";
				hasSaved = true;
				out.println(saving);
				out.close();
			}
			catch (FileNotFoundException e1) {
				System.err.println("Text file can't be read");
			}
			catch (IOException e2) {
				System.err.println("Input-Output error");
			}
			// saving done
			msg.setText("Disturbance "+id.getText()+" saved");
			msg.setVisible(true);
		}
		repaint();		
	}
}
