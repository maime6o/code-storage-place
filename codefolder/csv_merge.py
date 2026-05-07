#----利用方法-----
#1.pyファイルを指定のディレクトリに保存してください。
#2.棚卸対象のexcelに01、02とプレフィックスを付与してください。
#3.pandasをインストールしていない場合は、事前にCLI上でpip install pandasでインストールをしてください。また会社で使う場合は、情報システム部門にossを使っても良いのか必ず確認してください。pandasは、規約上商用利用可能なossです。

#pandas、pathlibのインポート
import pandas as pd
from pathlib import Path

#実行中のスクリプトファイルのディレクトリを取得
from pathlib import Path 
current_dir = Path(__file__).resolve().parent

#対象のファイルパスを取得
first_path = next(current_dir.glob("1*.csv"))
second_path = next(current_dir.glob("2*.csv"))

#csvファイルを開く
first_open = pd.read_csv(first_path)
second_open = pd.read_csv(second_path)

#キーとなるカラムが入っている列名をユーザーに指定させる。
print(f"{first_path.name}のcsv内のキーを指定してください。
print(first_open.columns.tolist()
key_column1 = imput("１つ目のファイルからキーとなるカラム名を入力してください。")

#print(f"{second_path.name}csv内のキーを指定してください。
print(second_open.columns.tolist()
key_column2 = imput("２つ目のファイルのキーとなるカラム名を入力してください。")
