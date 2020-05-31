#include<stdio.h>
#include<string.h>

char buf[32];

void func(){
	char local[32];
	fgets(local,128,stdin);
	strcpy(buf,local);
}

int main(int argc,char **argv){
    printf("buffer: 0x%x\n",&buf);
    func();
    return 0;
}
