//package GameModel.src.main.java;

import org.chocosolver.solver.Model;
import org.chocosolver.solver.Solution;
import org.chocosolver.solver.constraints.Constraint;
import org.chocosolver.solver.constraints.IIntConstraintFactory;
import org.chocosolver.solver.variables.BoolVar;
import org.chocosolver.solver.variables.IntVar;
import org.chocosolver.solver.variables.RealVar;
import org.chocosolver.solver.variables.SetVar;
import java.util.Random;

public class GameModel {

  // define the size of the grid (2x2)
  private static final int N = 2;

  // define the maximum value of a tile (2048)
  private static final int MAX_VALUE = 16;

  // define the probabilities of a new tile being a 2 or a 4
  private static final double PROB_2 = 0.9;
  private static final double PROB_4 = 0.1;

  // random number generator
  private static final Random rand = new Random(694201337);


  private static int spawn_x;
  private static int spawn_y;
  private static int v;


  public static void print_board(IntVar[][] board){
    for(int y = 0; y < N;  y++){
      for(int x = 0; x < N;  x++){
        System.out.print(board[x][y].getValue());
        System.out.print("|");
      }
      System.out.print("\n");
    }
  }
  public static void addNewRandomTile(){
    spawn_x = rand.nextInt(2);
    spawn_y = rand.nextInt(2);

    if(rand.nextDouble() <= PROB_2){
      v = 2;
    }
    else {
      v= 4;
    }
  }

  public static void main(String[] args){
    // create a new Choco model
    Model model = new Model("2048Game");
    // create NxN matrix of integer variables to represent the grid
    IntVar[][] grid = model.intVarMatrix("grid",  N, N, -1, MAX_VALUE);
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
    // Create an array of 1000 moves taking their value in [1, 4]
    IntVar[] moves = model.intVarArray("moves", 1000, 1, 4);





    // on commence avec 2 tiles sur la grille
    addNewRandomTile();

    while(grid[spawn_x][spawn_y].getValue() != -1){
      addNewRandomTile();
    }

    grid[spawn_x][spawn_y] = model.intVar(v);

    addNewRandomTile();

    while(grid[spawn_x][spawn_y].getValue() != -1){
      addNewRandomTile();
    }

    grid[spawn_x][spawn_y] = model.intVar(v);

    print_board(grid);

    // iteration sur chaque move
    for(var move: moves){
      // iteration sur chaque élément de la grille
      int current_move = move.getValue();

      if(current_move == 1){ // UP
        // de gauche à droite
        for(int x = 0; x < N;  x++){
          // de bas en haut
          for(int y = N-1; y > 0;  y--){
            // si deux cases dans la même colonne ont la même valeur et sont pleines
            if(grid[x][y].getValue() == grid[x][y-1].getValue() & grid[x][y].getValue() != -1){
              // intOffsetView -> addition
              // alors on additionne leurs valeurs dans la case du dessus
              grid[x][y-1] = model.intOffsetView(grid[x][y-1], grid[x][y].getValue());
              // et on vide la case de dessous
              grid[x][y] = model.intVar(-1);
            }
            // si la case du dessus est vide mais celle en dessous ne l'est pas
            else if(grid[x][y-1].getValue() == -1 & grid[x][y].getValue() != -1){
              // alors on remplit la case du dessus avec la valeur de celle de dessous
              grid[x][y-1] = grid[x][y];
              // puis on vide celle de dessous
              grid[x][y] = model.intVar(-1);
            }
          }
        }
      }
      else if(current_move == 2){ // DOWN
        // de gauche à droite
        for(int x = 0; x < N;  x++){
          // de haut en bas
          for(int y = 0; y < N;  y++){
            // si deux cases dans la même colonne ont la même valeur et sont pleines
            if(grid[x][y].getValue() == grid[x][y+1].getValue() & grid[x][y].getValue() != -1){
              // intOffsetView -> addition
              // alors on additionne leurs valeurs dans la case du dessous
              grid[x][y+1] = model.intOffsetView(grid[x][y+1], grid[x][y].getValue());
              // et on vide la case de dessus
              grid[x][y] = model.intVar(-1);
            }
            // si la case de dessous est vide mais celle du dessus ne l'est pas
            else if(grid[x][y+1].getValue() == -1 & grid[x][y].getValue() != -1){
              // alors on remplit la case de dessous avec la valeur de celle du dessus
              grid[x][y+1] = grid[x][y];
              // puis on vide celle du dessus
              grid[x][y] = model.intVar(-1);
            }
          }
        }
      }
      else if(current_move == 3){ // LEFT
        // de bas en haut
        for(int y = N-1; y > 0;  y--){
          // de gauche à droite
          for(int x = 0; x < N;  x++){
            // si deux cases dans la même ligne ont la même valeur et sont pleines
            if(grid[x][y].getValue() == grid[x+1][y].getValue() & grid[x][y].getValue() != -1){
              // intOffsetView -> addition
              // alors on additionne leurs valeurs dans la case de droite
              grid[x+1][y] = model.intOffsetView(grid[x+1][y], grid[x][y].getValue());
              // et on vide la case de gauche
              grid[x][y] = model.intVar(-1);
            }
            // si la case de droite est vide mais celle de gauche ne l'est pas
            else if(grid[x+1][y].getValue() == -1 & grid[x][y].getValue() != -1){
              // alors on remplit la case de droite avec la valeur de celle de gauche
              grid[x+1][y] = grid[x][y];
              // puis on vide celle de gauche
              grid[x][y] = model.intVar(-1);
            }
          }
        }
      }
      else{ // RIGHT
        // de haut en bas
        for(int y = 0; y < N;  y++){
          // de gauche à droite
          for(int x = 0; x < N;  x++){
            // si deux cases dans la même ligne ont la même valeur et sont pleines
            if(grid[x+1][y].getValue() == grid[x][y].getValue() & grid[x][y].getValue() != -1){
              // intOffsetView -> addition
              // alors on additionne leurs valeurs dans la case de gauche
              grid[x][y] = model.intOffsetView(grid[x+1][y], grid[x][y].getValue());
              // et on vide la case de droite
              grid[x+1][y] = model.intVar(-1);
            }
            // si la case de gauche est vide mais celle de droite ne l'est pas
            else if(grid[x][y].getValue() == -1 & grid[x+1][y].getValue() != -1){
              // alors on remplit la case de gauche avec la valeur de celle de droite
              grid[x][y] = grid[x+1][y];
              // puis on vide celle du droite
              grid[x+1][y] = model.intVar(-1);
            }
          }
        }
      }

      System.out.println(current_move);

      addNewRandomTile();

      while(grid[spawn_x][spawn_y].getValue() != -1){
        addNewRandomTile();
      }

      grid[spawn_x][spawn_y] = model.intVar(v);

      print_board(grid);
      System.out.print("\n");
    }

    Solution solution = model.getSolver().findSolution();

    if(solution != null){
      System.out.println(solution.toString());
    }
  }

}
