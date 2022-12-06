package GameModel.src.main.java;

import org.chocosolver.solver.Model;
import org.chocosolver.solver.variables.BoolVar;
import org.chocosolver.solver.variables.IntVar;
import org.chocosolver.solver.variables.RealVar;
import org.chocosolver.solver.variables.SetVar;

public class GameModel {


  public static void main(String[] args){
    Model model = new Model("2048Game");
    //we are going to start with a 2x2 model
    IntVar maxValue = model.intVar("maxValue", 16);
    RealVar newTile2chance = model.realVar("newTile2chance", 0.9);
    IntVar newTileValue = model.intVar("newTileValue", new int[]{2, 4});
    IntVar value = model.intVar("value", new int[]{-1, 2, 4, 8, 16});
    //-1 is empty
    SetVar possibleMoves = model.setVar("possibleMoves", new int[]{}, new int[]{1, 2, 3, 4});
    //1 = UP 2 = DOWN 3 = LEFT 4 = RIGHT
    SetVar oppositeMoves = model.setVar("oppositeMoves", new int[]{}, new int[]{2, 1, 4, 3});
    SetVar columns = model.setVar("columns", new int[]{}, new int[]{1, 2});
    SetVar rows = model.setVar("rows", new int[]{}, new int[]{1, 2});
    BoolVar isAvailable = model.boolVar("isAvailable");

    IntVar[][] grid = model.intVarMatrix("grid", 2, 2, -1, 16);




  }

}
