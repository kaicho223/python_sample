import os
import subprocess		# UNIXコマンド実行

'''
言語処理100本ノック
http://www.cl.ecei.tohoku.ac.jp/nlp100/
第2章: UNIXコマンドの基礎
    hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
    以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．
    さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．
@author kaicho223
'''


class PythonKnockPart2:

    path = os.path.dirname(__file__)
    FILE_HIGHTEMP_TXT = path + "/hightemp.txt"

    '''
    10. 行数のカウント
        行数をカウントせよ．確認にはwcコマンドを用いよ．
    '''

    def count_use_unix(self):
        print(os.path.dirname(__file__))
        return subprocess.call('cat ./hightemp.txt | wc -l')


