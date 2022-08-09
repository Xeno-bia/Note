# 開発環境
# https://www.python.org/downloads/ # Python
# https://code.visualstudio.com/    # Visual Studio Code

# 型
1          # 整数(int)
1.0        # 小数(float)
"A"        # 文字列(str)
True/False # 真偽値(bool)

# 演算子
+   # 足し算
-   # 引き算
*   # 掛け算
/   # 割り算
==  # イコール
<   # 小なり
<=  # 小なりイコール
>   # 大なり
>=  # 大なりイコール
in  # 含まれる
and # かつ
or  # または
not # ではない

# 分岐
if 条件:   # もし
    処理   #
elif 条件: # でなければもし
    処理   #
else:      # でなければ
    処理   #

# ループ
for i in 回数: # 回数
    処理       #
    continue   # スキップ
    break      # 終了

while 条件:  # 条件
    処理     #
    continue # スキップ
    break    # 終了

# 変数
変数 = 値 # 初期化
変数      # 取得

リスト = [値]             # 初期化
リスト[インデックス] = 値 # 代入
リスト                    # 取得
リスト[インデックス]      # 一部取得

辞書 = {キー:値} # 初期化
辞書[キー] = 値  # 代入
辞書             # 取得
辞書[キー]       # 一部取得

# 関数
def 関数(引数): # 作成
    処理        #
関数(引数)      # 使用

# クラス
class クラス:             # 作成
    変数 = 値             # 変数初期化
    def 関数(self, 引数): # 関数作成
オブジェクト = クラス()   # オブジェクト作成
オブジェクト.変数         # 変数取得
オブジェクト.関数(引数)   # 関数使用

# ライブラリ
# > pip install ライブラリ # インストール
import ライブラリ          # インポート
ライブラリ.変数            # 変数取得
ライブラリ.関数(引数)      # 関数使用

入力
input()

出力
print(...)

整数化
int(...)

小数化
float(...)

文字列化
str(...)

累乗
pow(..., ...)

余り
divmod(..., ...)

現在日時
import datetime
x = datetime.datetime.now()
x.year
x.month
x.day
x.hour
x.minute
x.second

待機
import time
time.sleep(...)

終了
import sys
sys.exit()

乱数
range(begin, end, step)

長さ
len(...)

四捨五入
import decimal
decimal.Decimal(str("...")).quantize(Decimal("dig"), rounding=decimal.ROUND_HALF_UP)

絶対値
abs(...)

切り捨て
import math
floor(...)

切り上げ
import math
ceil(...)

音声
# > pip install playsound
import playsound
playSound.playsound("mp3")

画像
# > pip install opencv-python
import cv2
img = cv2.imread("jpg/png")
cv2.namedWindow('window', cv2.WINDOW_NORMAL)
cv2.imshow('window', img)
cv2.waitKey(0)
