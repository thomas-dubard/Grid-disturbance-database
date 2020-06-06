import java.awt.*;
import java.awt.event.*;
import java.io.*;

public class Disturbance extends Frame implements ActionListener {
	private Label idlabel;
	private TextField id;
	private Label datelabel;
	private TextField date;
	private Label timelabel;
	private TextField time;
	private Button save;
	private Label msg;
	
	public Disturbance () {
		id = new TextField(40);
		idlabel = new Label("ID");
		date = new TextField(40);
		datelabel = new Label("Date");
		time = new TextField(40);
		timelabel = new Label("Time");
		save = new Button("Save");
		msg = new Label();
		
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

	public void actionPerformed(ActionEvent e) {
		if (e.getSource()==save) {
			// do the saving
			try {
				PrintWriter out = new PrintWriter (new FileWriter("ToSave.txt",true));
				out.println("Disturbance%"+id.getText()+"%"+date.getText()+"%"+time.getText()+"\n");
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
