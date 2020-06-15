# sneaky - Writeup

## 方針
とりあえずメモリをいじってスコアを書き換えることを目標とする。gdbでアタッチできないのでプロセスを見る。
```
$ ps aux | grep sneaky
ptr      20184  0.0  0.0   1352     4 pts/7    S+   23:44   0:00 ./sneaky
ptr      20185  0.3  0.0   1616  1056 pts/7    S+   23:44   0:00 ./sneaky
```
2つプロセスが立っているので、ptraceを使ってデバッグを妨害していることが推測できる。

IDAで読むと、`__libc_csu_init`から呼ばれる関数にcursesを初期化している関数がある。その中で最初に呼ばれる関数を見ると、明らかにforkしてptraceを走らせている。この関数呼び出しをnopで埋めてパッチを当てるとgdbでアタッチできるようになる。

次にmain関数の最後に呼ばれるゲームのメインループを見る。`"SCORE: %d"`といった書式文字列が使われており、これはゲームの構造体の先頭から0x20バイト先を参照しているため、ここを書き換えればよいことが分かる。ゲームの構造体はmallocで確保され、rbxに退避されるので、`[rbx+0x20]`を大きな整数値に書き換えてcontinueするとフラグが表示される。

バイナリにパッチ当てたり、既存のメモリハックツールを使ってスコアを書き換えても良い。（後者の場合、ゲームオーバーにならないようusleepをいじったりプロセスを一時停止する必要がある。）