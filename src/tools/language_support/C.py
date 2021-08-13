class C():
    def create_file(self):
        with open("main.c",'w') as f:
            st = '''
#include<stdio.h>
#include<stdlib.h>
using namespace std;
int main()
{

    return 0;
}
            '''
            f.write(st)
