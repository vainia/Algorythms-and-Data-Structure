int fibo(int x){
   return fiboSub(x,1,1);
}

int fiboSub(int x, int y, int z){
   if(x==1)return y;
   return fiboSub(x-1,y+z,y)
}

// x        y        z        i
// 10       1        1        0
// 9        2        1        1
// 8        3        2        2
// 7        5        3        3
// 6        8        5        4
// 5        13       8        5
// 4        21       13       6
// 3        34       21       7
// 2        55       34       8
// 1        89       55       9
