import java.awt.event.*;

/** Class conceived to listen windowClosing Events to close the application when the window is closed
 * 
 *
 */
public class EcouteurPourFermetureFenetre extends WindowAdapter {
  // Remarque : faire hériter cette classe de WindowAdapter permet d'implanter
  //            l'interface WindowListener sans avoir à redéfinir TOUTES 
  //            les méthodes de l'interface.
    
  public void windowClosing(WindowEvent w) {
    w.getWindow().dispose() ;  // Libération des ressources associées à la Frame
    System.exit(0);  // Sortie du programme  avec code d'erreur 0 (pas d'erreur)
  }
  
}