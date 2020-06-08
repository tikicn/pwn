set encoding=utf-8
set number
set autoindent
set tabstop=4
set shiftwidth=4
set nobackup
set noswapfile
syntax on


"tabをスペースに
set expandtab

"検索結果を全てハイライト
set hlsearch

"検索時、入力文字列を順次ヒットさせる
set incsearch

"ステータスラインの表示
set laststatus=2

"インサート時の文字削除を柔軟にする
set backspace=indent,eol,start

"括弧の対応付け
set showmatch

"コマンドライン補完
set wildmode=list:longest

"折り返し時に表示行単位で移動する
nnoremap j gj
nnoremap k gk

"Ctrl+j Ctrl+kで段落前後に移動
nnoremap <C-j> }
nnoremap <C-k> {

"Ctrl+hで先頭、Ctrl+lで行末に移動
nnoremap <C-h> 0
nnoremap <C-l> $

"ヤンク、プット時にクリップボードを利用
set clipboard+=unnamed
