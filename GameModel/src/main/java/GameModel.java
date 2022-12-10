//package GameModel.src.main.java;

import org.chocosolver.solver.Model;
import org.chocosolver.solver.Solution;
import org.chocosolver.solver.variables.BoolVar;
import org.chocosolver.solver.variables.IntVar;
import org.chocosolver.solver.variables.RealVar;
import org.chocosolver.solver.variables.SetVar;
import java.util.Random;

public class GameModel {

  public static void print_board(IntVar[][] board){
    for(int y = 0; y < 2;  y++){
      for(int x = 0; x < 2;  x++){
        System.out.print(board[x][y].getValue());
        System.out.print("|");
      }
      System.out.print("\n");
    }
  }

  public static void main(String[] args){
    // random number generator
    Random rand = new Random(694201337);
    
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
    BoolVar[][] isAvailable = model.boolVarMatrix("isAvailable", 2, 2); // variable pour savoir si une tile peut être merged

    // Liste de moves
    IntVar[] moves = new IntVar[1000]; // maximum de 1000 moves mettons
    for(int q = 0; q < 1000; q++){
      moves[q] = model.intVar("moves_"+q, 1, 4); // Générer les variables de moves
    }

    IntVar[][] grid = model.intVarMatrix("grid", 2, 2, -1, 16);
    
    // on commence avec 2 tiles sur la grille
    int spawn_x = rand.nextInt(1)+1;
    int spawn_y = rand.nextInt(1)+1;
    double v_prob = rand.nextDouble();
    int new_value = 0;
    if(v_prob < 0.9){
      new_value = 2;
    }
    else {
      new_value = 4;
    }

    while(grid[spawn_x][spawn_y].getValue() != -1){
      spawn_x = rand.nextInt(2);
      spawn_y = rand.nextInt(2);
      v_prob = rand.nextDouble();
      new_value = 0;
      if(v_prob < 0.9){
        new_value = 2;
      }
      else {
        new_value = 4;
      }
    }

    grid[spawn_x][spawn_y] = model.intVar(new_value);

    spawn_x = rand.nextInt(1)+1;
    spawn_y = rand.nextInt(1)+1;
    v_prob = rand.nextDouble();
    new_value = 0;
    if(v_prob < 0.9){
      new_value = 2;
    }
    else {
      new_value = 4;
    }

    while(grid[spawn_x][spawn_y].getValue() != -1){
      spawn_x = rand.nextInt(2);
      spawn_y = rand.nextInt(2);
      v_prob = rand.nextDouble();
      new_value = 0;
      if(v_prob < 0.9){
        new_value = 2;
      }
      else {
        new_value = 4;
      }
    }

    grid[spawn_x][spawn_y] = model.intVar(new_value);

    print_board(grid);

    // iteration sur chaque move
    for(int i = 1; i <= 1000; i++){
      // iteration sur chaque élément de la grille
      int current_move = moves[i].getValue();
          
      if(current_move == 1){ // UP
        for(int x = 0; x < 2;  x++){
          for(int y = 1; y > 0;  y--){
            // logique de tiles
            if(grid[x][y].getValue() == grid[x][y-1].getValue() & grid[x][y].getValue() != -1){
              grid[x][y-1] = model.intOffsetView(grid[x][y-1], grid[x][y].getValue());
              grid[x][y] = model.intVar(-1);
            }
            else if(grid[x][y-1].getValue() == -1 & grid[x][y].getValue() != -1){
              grid[x][y-1] = grid[x][y];
              grid[x][y] = model.intVar(-1);
            }
          }
        }
      }
      else if(current_move == 2){ // DOWN

      }
      else if(current_move == 3){ // LEFT

      }
      else{ // RIGHT

      }
      
      System.out.println(current_move);

      spawn_x = rand.nextInt(1)+1;
      spawn_y = rand.nextInt(1)+1;
      v_prob = rand.nextDouble();
      new_value = 0;
      if(v_prob < 0.9){
        new_value = 2;
      }
      else {
        new_value = 4;
      }

      while(grid[spawn_x][spawn_y].getValue() != -1){
        spawn_x = rand.nextInt(2);
        spawn_y = rand.nextInt(2);
        v_prob = rand.nextDouble();
        new_value = 0;
        if(v_prob < 0.9){
          new_value = 2;
        }
        else {
          new_value = 4;
        }
      }

      grid[spawn_x][spawn_y] = model.intVar(new_value);

      print_board(grid);
      System.out.print("\n");
    }

    Solution solution = model.getSolver().findSolution();

    if(solution != null){
      System.out.println(solution.toString());
    }
  }

}
