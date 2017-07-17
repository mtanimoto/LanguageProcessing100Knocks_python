"""
第1章: 準備運動
テキストや文字列を扱う題材に取り組みながら，プログラミング言語のやや高度なトピックを復習します．
文字列, ユニコード, リスト型, 辞書型, 集合型, イテレータ, スライス, 乱数
"""
class Chapter1:

    # 00. 文字列の逆順
    # 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
    def method_00(self):
        str = "stressed"
        ret = ""
        for num in range(str.__len__()):
            ret += str[(num + 1) * -1]

        return ret

    # 01. 「パタトクカシーー」
    # 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
    def method_01(self):
        str = "パタトクカシーー"

        return str[0:str.__len__():2]

    # 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
    # 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
    def method_02(self):
        str1 = "パトカー"
        str2 = "タクシー"
        ret = ""

        for num in range(str1.__len__()):
            ret += str1[num] + str2[num]

        return ret

    # 03. 円周率
    # "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，
    # 各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
    def method_03(self):
        sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
        sentence = sentence.replace('.', '').replace(',', '')
        sentence_sprit = sentence.split(" ")
        word_length_list = []
        for word in sentence_sprit:
            word_length_list.append(word.__len__())
        return word_length_list

    # 04. 元素記号
    # "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    # という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19
    # 番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
    def method_04(self):
        first_character_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
        sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
        sentence = sentence.replace('.', '').replace(',', '')
        sentence_sprit = sentence.split(" ")

        ret = {}
        loop_first_num = 1
        loop_end_num = len(sentence_sprit) + 1
        for num in range(loop_first_num, loop_end_num):
            if num in first_character_list:
                ret[sentence_sprit[num - 1][0:1]] = num
            else:
                ret[sentence_sprit[num - 1][0:2]] = num

        return ret

    # 05. n-gram
    # 与えられたシーケンス（文字列やリストなど）からn - gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"
    # という文から単語bi - gram，文字bi - gramを得よ．
    # N-gramとは
    # http://d.hatena.ne.jp/jetbead/20110904/1315147133
    def method_05(self, sequence, n, type):
        ret = []

        if type == 'word':
            # 単語n-gram
            return self.word_n_gram(sequence.split(" "), n)
        if type == 'character':
            # 文字n-gram
            return self.character_n_gram(sequence, n)

    """
    単語n-gram
    """
    def word_n_gram(self, sequence, n):
        ret = []
        for i in range(sequence.__len__() - n + 1):
            gram_list = []
            for j in range(n):
                gram_list.append(sequence[i + j])

            ret.append(gram_list)
        return ret

    """
    文字n-gram
    """
    def character_n_gram(self, sequence, n):
        ret = []
        for i in range(sequence.__len__() - n + 1):
            ret.append(sequence[i : i + n])
        return ret

    """
    06. 集合
    "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
    XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
    """
    def method_06(self):
        word1 = 'paraparaparadise'
        word2 = 'paragraph'
        x = self.method_05(word1, 2, 'character')
        y = self.method_05(word2, 2, 'character')

        print('')
        set_x = set(x)
        set_y = set(y)

        print('x：' + str(set_x))
        print('y：' + str(set_y))

        # 和集合
        print('和集合(x | y)：' + str(set_x | set_y))
        # 積集合
        print('積集合(x & y)：' + str(set_x & set_y))
        # 差集合
        print('差集合(x - y)：' + str(set_x - set_y))
        print('差集合(y - x)：' + str(set_y - set_x))

        # issubset⇒部分集合
        return 'se' in set_x or 'se' in set_y

    """
    07. テンプレートによる文生成
    引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
    """
    def method_07(self, x, y, z):
        return '%d時の%sは%.1f' % (x, y, z)

    """
    08. 暗号文

    与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

    英小文字ならば(219 - 文字コード)の文字に置換
    その他の文字はそのまま出力

    この関数を用い，英語のメッセージを暗号化・復号化せよ．
    """
    def method_08(self, s):
        s = str(s)

        ret = ''
        for c in s:
            ret += chr(219 - ord(c)) if c.isalpha() and c.islower() else c

        return ret

    """
    09. Typoglycemia
    スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
    ただし，長さが４以下の単語は並び替えないこととする．
    適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，
    その実行結果を確認せよ．
    """
    def method_09(self, input):
        import random
        input_split = input.split()

        result = []
        for word in input_split:
            if len(word) > 4:
                char_list = list(word)
                mid_list = char_list[1:-1]
                random.shuffle(mid_list)
                word = word[0] + "".join(mid_list) + word[-1]

            result.append(word)

        return " ".join(result)