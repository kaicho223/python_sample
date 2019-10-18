import os
import re

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

    # 現在のディレクトリを取得(ターミナル、atom-runner共に動作可能になるようにしてます)
    PATH = os.path.dirname(os.path.abspath(__file__))
    FILE_HIGHTEMP_TXT = PATH + "/hightemp.txt"

    '''
    10. 行数のカウント
        行数をカウントせよ．確認にはwcコマンドを用いよ．
        $ cat hightemp.txt | wc -l
    '''

    def count_row_num(self):
        return sum([1 for _ in open(PythonKnockPart2.FILE_HIGHTEMP_TXT,
                                    'r',
                                    encoding='utf-8')])

    '''
    11. タブをスペースに置換
        タブ1文字につきスペース1文字に置換せよ．
        確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
        $ cat hightemp.txt | sed -e 's/\t/ /g'
    '''

    def replace_tab_to_space(self):
        f = open(PythonKnockPart2.FILE_HIGHTEMP_TXT, 'r', encoding='utf-8')
        lines = f.read()
        f.close()

        return re.sub(r"\t", " ", lines)

    '''
    12. 1列目をcol1.txtに，2列目をcol2.txtに保存
        各行の1列目だけを抜き出したものをcol1.txtに，
        2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
        確認にはcutコマンドを用いよ．
        $ cut -f 1 hightemp.txt
        $ cut -f 2 hightemp.txt
    '''

    def cut_text(self, col_no):
        f = open(PythonKnockPart2.FILE_HIGHTEMP_TXT, 'r', encoding='utf-8')
        lines = f.readlines()
        f.close

        list_target_col = []
        for line in lines:
            target = line.split("\t")[col_no - 1]
            list_target_col.append(target)

        file_name = PythonKnockPart2.PATH + "/col" + str(col_no) + ".txt"
        f = open(file_name, 'w', encoding='utf-8')
        f.writelines('\n'.join(list_target_col))
        f.close
        print("ファイル作成：" + file_name)
