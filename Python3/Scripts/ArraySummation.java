import java.util.Scanner;

class Solver{
    int minNumber, maxNumber, numSum, numLen, Arr[];
    Solver(int []Arr){
        this.Arr = Arr;
        if (this.Arr[0] > this.Arr[1]){
            this.minNumber = this.Arr[1];
            this.maxNumber = this.Arr[0];
        }else {
            this.minNumber = this.Arr[0];
            this.maxNumber = this.Arr[1];
        }
        this.numLen = (this.maxNumber - this.minNumber)+1;
    }
    int getSum(){
        int maxPlusMin = this.maxNumber + this.minNumber;
        int sum = (this.numLen*maxPlusMin)/2;
        return sum;
    }
}


public class ArraySummation{
    public static void main(String[] args) {
        int []Arr = new int[2];
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the elements:");
        for (int i=0; i < 2; i++) {
            Arr[i] = sc.nextInt();
        }
        long startTime = System.nanoTime();
        Solver solver = new Solver(Arr);
        int sum = solver.getSum();
        long endTime = System.nanoTime();
        System.out.println("The sum is: " + sum);
        System.out.println("Time taken: " + (endTime - startTime)+" nanoSeconds.");
        sc.close();
    }
}