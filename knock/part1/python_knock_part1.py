import re        # 正規表現
import random    # 乱数

'''
言語処理100本ノック
http://www.cl.ecei.tohoku.ac.jp/nlp100/
第1章: 準備運動
@author kaicho223
'''


class PythonKnockPart1:

    '''
    00. 文字列の逆順
        文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
    '''

    # reversed() を使って並べ替え
    def reverse_str_reversed(self, input_str):
        return ''.join(list(reversed(input_str)))

    # スライスを使って並べ替え
    def reverse_str_slice(self, input_str):
        return input_str[::-1]

    '''
    01. 「パタトクカシーー」
        「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
    '''

    # +=演算子で連結
    def patatokukashi_operator(self, input_str):
        input_str_list = list(input_str)
        new_str = ""
        for i in range(len(input_str)):
            if i % 2 == 0:
                new_str += input_str_list[i]
        return new_str

    # join()で連結
    def patatokukashi_join(self, input_str):
        input_str_list = list(input_str)
        new_str_list = []
        for i in range(len(input_str)):
            if i % 2 == 0:
                new_str_list.append(input_str_list[i])
        return ''.join(new_str_list)

    '''
    02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
        「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
    '''

    # +=演算子で連結
    def policecar_plus_taxi_operator(self, input_str1, input_str2):
        input_str1_list = list(input_str1)
        input_str2_list = list(input_str2)

        new_str = ""
        for i in range(len(input_str1_list)):
            new_str += input_str1_list[i]
            new_str += input_str2_list[i]
        return new_str

    # join()で連結
    def policecar_plus_taxi_join(self, input_str1, input_str2):
        input_str1_list = list(input_str1)
        input_str2_list = list(input_str2)

        new_str_list = []
        for i in range(len(input_str1_list)):
            new_str_list.append(input_str1_list[i])
            new_str_list.append(input_str2_list[i])
        return ''.join(new_str_list)

    '''
    03. 円周率
        "Now I need a drink, alcoholic of course,
        after the heavy lectures involving quantum mechanics."
        という文を単語に分解し，
        各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
    '''

    def pi(self, input_str, regex):
        input_str_list = list(input_str)

        # 辞書にセット（key: アルファベット value: 文字数）
        dic = {}
        for i in range(len(input_str_list)):

            # アルファベットのみカウント
            pattern = re.compile(regex)
            if pattern.match(input_str_list[i]):
                if dic.get(input_str_list[i]) is None:
                    dic[input_str_list[i]] = 1
                else:
                    count = dic[input_str_list[i]]
                    count += 1
                    dic[input_str_list[i]] = count
        return dic

    '''
    04. 元素記号
        "Hi He Lied Because Boron Could Not Oxidize Fluorine.
        New Nations Might Also Sign Peace Security Clause. Arthur King Can."
        という文を単語に分解し，
        1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
        取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
    '''

    def element_symbol(self, input_str, target_list):
        input_str_list = input_str.split(' ')

        # 辞書にセット
        dic = {}
        for i in range(len(input_str_list)):
            str_key = ""
            if i + 1 in target_list:
                str_key = input_str_list[i][0:1]
            else:
                str_key = input_str_list[i][0:2]
            dic[str_key] = i + 1
        return dic

    '''
    05. n-gram
        与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
        この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
    '''

    def n_gram(self, input_str, n):
        # 基準を1文字(単語)ずつ ずらしながらn文字分抜き出す
        str_target_list = []
        for i in range(len(input_str) - n + 1):
            str_target_list.append(input_str[i:i + n])
        return str_target_list

    def n_gram_slim(self, input_str, n):
        # 基準を1文字(単語)ずつ ずらしながらn文字分抜き出す
        return [input_str[i:i + n] for i in range(len(input_str) - n + 1)]

    '''
    06. 集合
        "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
        それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
        さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
    '''

    # 集合を求める前に使用（bigramを作成 -> setに格納）
    def set_bigram(self, func, input_str1, input_str2):    # func: n_gram_slim
        # bigram
        x = func(self, input_str1, 2)
        y = func(self, input_str2, 2)

        # setに格納（[1, 2] -> {1, 2}）
        set_x = set(x)
        set_y = set(y)
        return set_x, set_y

    # 和集合(記号「|」使用) func: set_bigram
    def set_union_symbol(self, func, input_str1, input_str2):
        set_x, set_y = func(PythonKnockPart1.n_gram_slim, input_str1, input_str2)
        return set_x | set_y

    # 和集合(union 関数使用) func: set_bigram
    def set_union_func(self, func, input_str1, input_str2):
        set_x, set_y = func(PythonKnockPart1.n_gram_slim, input_str1, input_str2)
        return set_x.union(set_y)

    # 積集合(記号「&」使用) func: set_bigram
    def set_intersection_symbol(self, func, input_str1, input_str2):
        set_x, set_y = func(PythonKnockPart1.n_gram_slim,
                            input_str1, input_str2)
        return set_x & set_y

    # 積集合(intersection 関数使用) func: set_bigram
    def set_intersection_func(self, func, input_str1, input_str2):
        set_x, set_y = func(PythonKnockPart1.n_gram_slim,
                            input_str1, input_str2)
        return set_x.intersection(set_y)

    # 差集合(記号「-」使用) func: set_bigram
    def set_difference_symbol(self, func, input_str1, input_str2):
        set_x, set_y = func(PythonKnockPart1.n_gram_slim,
                            input_str1, input_str2)
        return set_x - set_y

    # 差集合(difference 関数使用) func: set_bigram
    def set_difference_func(self, func, input_str1, input_str2):
        set_x, set_y = func(PythonKnockPart1.n_gram_slim,
                            input_str1, input_str2)
        return set_x.difference(set_y)

    '''
    07. テンプレートによる文生成
        引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
        さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
    '''

    def create_sentence_by_template(self, x, y, z):
        return "{0}時の{1}は{2}".format(x, y, z)

    '''
    08. 暗号文
        与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
            ・英小文字ならば(219 - 文字コード)の文字に置換
            ・その他の文字はそのまま出力
        この関数を用い，英語のメッセージを暗号化・復号化せよ．
    '''

    def cipher(self, input_str):
        conv_str = "abcdefghijklmnopqrstuvwxyz"
        dic = {}
        for i in range(len(conv_str)):
            dic[conv_str[i]] = str(ord(conv_str[i]))
        return input_str.translate(str.maketrans(dic))

    '''
    09. Typoglycemia
        スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
        それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
        ただし，長さが４以下の単語は並び替えないこととする．
        適当な英語の文（例えば"I couldn't believe that
         I could actually understand what I was reading :
          the phenomenal power of the human mind ."）を与え，
        その実行結果を確認せよ．
    '''

    def randam_sort(self, input_str):
        target_str = input_str[1:len(input_str)-1]
        randam_str = random.sample(target_str, len(target_str))
        return input_str[0] + ''.join(randam_str) + input_str[len(input_str)-1]

    def typoglycemia(self, func, input_str):
        input_str_list = input_str.split(" ")
        new_str = ""
        len_input_str_list = len(input_str_list)
        for i in range(len_input_str_list):
            if (len(input_str_list[i]) > 3):
                new_str += func(input_str_list[i])
            else:
                new_str += input_str_list[i]
            if i < len_input_str_list - 1:
                new_str += " "
        return new_str
