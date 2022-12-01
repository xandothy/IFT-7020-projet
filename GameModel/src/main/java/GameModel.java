import org.chocosolver.solver.Model;
import org.chocosolver.solver.variables.IntVar;
import org.chocosolver.solver.variables.RealVar;
import org.chocosolver.solver.variables.SetVar;

public class GameModel {


  public static void main(String[] args){
    Model model = new Model("2048Game");
    //we are going to start with a 2x2 model
    IntVar maxValue = model.intVar("maxValue", 2048);
    RealVar newTile2chance = model.realVar("newTile2chance", 0.9);
    SetVar possibleValues = model.setVar("possibleValues", new int[]{}, new int[]{0,2,4,8,16, 32, 64, 128, 256,
        512, 1024, 2048});

  }

}
