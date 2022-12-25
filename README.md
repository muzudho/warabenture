# warabenture

わたしのホームページ（＾～＾）

# Git

👇 1回目は、イニシャライズしてクローン  

```shell
# がんばｓって、ディレクトリーを移動してほしい
# cd warabenture/src1

git init

git clone https://github.com/muzudho/warabenture.git
```

👇 2回目以降は、プルしてフェッチ  

```shell
# （慎重）ローカルの変更をすべて破棄したいなら
git restore .

# 取得
git pull https://github.com/muzudho/warabenture.git
git fetch https://github.com/muzudho/warabenture.git
```

# Run

```shell
cd src1

docker-compose up
```

# Test

Open the browser

* 📖 [http://localhost/hello/ver1.0/](http://localhost/hello/ver1.0/) - 練習
* 📖 [http://localhost/](http://localhost/) - ポータル
* 過去バージョン ～ 最新バージョン網羅
    * 📖 [http://localhost/portal/ver1.0/](http://localhost/portal/ver1.0/)
    * 📖 [http://localhost/portal/ver1.1.0/](http://localhost/portal/ver1.1.0/)
    * 📖 [http://localhost/portal/ver1.1.0/](http://localhost/portal/ver1.2.0/)
* 📖 [http://localhost/air-hockey](http://localhost/air-hockey) - エアホッケー
