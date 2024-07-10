public abstract class hook {
    String name;
    int age;
    public hook(String name, int age){
        this.name = name;
        this.age = age;
    }
    public final void introduceSelf(){
        sayName(); sayAge();
        saySpecial(); sayMessage();
    }
    public void sayName(){ System.out.println("하이" + name + "입니다");}
    public void sayAge(){ System.out.println("하이" + age + "입니다");}
    public void saySpecial(){ }
    public abstract void sayMessage();
}
