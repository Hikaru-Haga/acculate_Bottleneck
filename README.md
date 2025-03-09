# PerceptualSimilarity

二次元画像から位相的データ解析ライブラリHomcloudを利用し、パーシステンス図の作成とボトルネック図の計算を行い、データにまとめるプログラム。

# 各プログラムについて
mkdir_datasetは任意のデータセットのディレクトリ全体をコピーする(ディレクトリのみ、ファイルは空で生成される)。グレイスケールに変換した画像とパーシステンス図を保存するディレクトリを生成しておくと管理が容易。

ch_grayはカラー画像をグレイスケールに変換する。np_savetxtでは整数で保存することでファイルを小さくすることが可能。

PH_csvは二次元画像データセットからパーシステンス図を生成する。hc.PDList.from_bitmap_levelsetで"sublevel"を指定、セル複体に関する劣位集合フィルトレーションを考えている。

bottleneck_disはボトルネック距離を計算する。データセットの都合で参照画像とパッチ0、参照画像とパッチ1のボトルネック距離を計算している。他のデータセットに使う場合変更すべし。resultファイルに保存する

acculateは人間判断による類似度とボトルネック距離との比較を行っている。人間判断による類似度については参考資料を参照。

save_npyは各画像の人間判断による類似度判断をまとめてリストに入れて保存する。必要に応じて使用すること。

#　必要ライブラリ
必要ライブラリはHomcloud。インストール手順は以下URLより。バージョンは基本的には最新であれば動作する、以下は筆者環境。
https://homcloud.dev/index.html
* HomCloud 3.6

またデータセットはBAPPSデータセットを使用している。詳しくは以下URLを確認。
https://github.com/richzhang/PerceptualSimilarity

# ライセンス
筆者については特になし。ただしHomCloudライブラリ、BAPPSデータセットの使用にはそれぞれのライセンスを要確認。

# 参考資料
The Unreasonable Effectiveness of Deep Features as a Perceptual Metric
Richard Zhang, Phillip Isola, Alexei A. Efros, Eli Shechtman, Oliver Wang
https://arxiv.org/pdf/1801.03924

# 著者
* 芳賀　光
* 所属　茨城大学大学院　理工学研究科　情報工学専攻
* lightning2000702@gmail.com
