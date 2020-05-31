#include<stdio.h>
#include<string.h>

void func(){
    char msg[]="Hello\n";
    char buf[32];
    write(1,msg,strlen(msg));
    read(0,buf,128);
}

int main(int argc,char *argv[]){
    func();
    return 0;
}