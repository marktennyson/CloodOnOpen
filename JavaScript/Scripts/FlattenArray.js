class FlattenArray{
    constructor(){
        this.joinedArray = new Array();
    }
    flatter = (Arr) => {
        for (const index in Arr){
            if (Arr[index] instanceof Array) this.flatter(Arr[index]);
            else this.joinedArray.push(Arr[index]);
        }
        return this.joinedArray;
    }
}

function main() {
    const inp1 = [1, [], [3, [[4]]]];
    const inp2 = [[["a"]], [["b"]]];
    const inp3 =[1, [2], [3, [[4]]]];
    const inp4 =[1, {}, [3, [[4]]]];
    const inpL = [inp1, inp2, inp3, inp4]
    for (let i = 0; i < inpL.length; i++){
        const fa = new FlattenArray();
        const ansArray = fa.flatter(inpL[i]);
        console.log(ansArray);
    }
    
}

main()