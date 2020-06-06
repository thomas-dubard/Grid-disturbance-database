import java.awt.event.*;

/** Classe conçue pour écouter les événements "fermeture fenêtre" afin
    d'arrêter proprement l'application lorsqu'on ferme la fenêtre. */
public class EcouteurPourFermetureFenetre extends WindowAdapter {
  // Remarque : faire hériter cette classe de WindowAdapter permet d'implanter
  //            l'interface WindowListener sans avoir à redéfinir TOUTES 
  //            les méthodes de l'interface.
    
  public void windowClosing(WindowEvent w) {
    w.getWindow().dispose() ;  // Libération des ressources associées à la Frame
    System.exit(0);  // Sortie du programme  avec code d'erreur 0 (pas d'erreur)
  }
  
}