import java.util.Scanner;

public class Main {

    private static int coin_change( int N ){
        int ans = 0;
        int[] C = { 10, 5, 1 };
        for( int i=0; i < 3; ++i )
            for(; N >= C[ i ]; N -= C[ i ], ++ans );
        return ans;
    }

    public static void main( String[] args ){
        Scanner input = new Scanner( System.in );
        int N = input.nextInt(),
            ans = coin_change( N );
        System.out.println( ans );
    }
}