import java.util.*;

public class Robot {
    private final String _name;
    public enum Command{ WALK, STOP, JUMP};
    
    public Robot(String name){ _name = name; }

    public void order(Robot.Command cmd){
        if(cmd == Command.WALK){
            System.out.println(_name + " walks.");
        }else if( cmd == Command.STOP){
            System.out.println(_name + " stops.");
        }else if( cmd == Command.JUMP){
            System.out.println(_name + " jumps.");
        }else{
            System.out.println("COMMAND ERROR. COMMAND =" + cmd);
        }
    }
}
