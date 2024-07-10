public class App extends hook {

    public App(String name, int age){
        super(name, age);
    }
    @Override
    public void sayMessage(){
        System.out.println("열심히 할게욤!");
    }
    @Override
    public void saySpecial(){
        System.out.println("난 짱인걸?");
    }
    public static void main(String[] args) throws Exception {
        //hook ho = new App("namHansan",25);
        // ho.introduceSelf();
        Robot rbt = new Robot("Andrew");
        rbt.order(Robot.Command.WALK);
        rbt.order(Robot.Command.STOP);
        rbt.order(Robot.Command.JUMP);

    }
    
}
