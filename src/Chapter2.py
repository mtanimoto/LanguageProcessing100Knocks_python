import os
from collections import defaultdict

"""
第2章: UNIXコマンドの基礎
研究やデータ分析において便利なUNIXツールを体験します．これらの再実装を通じて，プログラミング能力を高めつつ，既存のツールのエコシステムを体感します．
head, tail, cut, paste, split, sort, uniq, sed, tr, expand
"""
class Chapter2:
    """
    hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．
    以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．
    さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．
    """

    def __init__(self, path):
        base = os.path.dirname(os.path.abspath(__file__))
        self.name = os.path.normpath(os.path.join(base, path))

    # 10. 行数のカウント
    # 行数をカウントせよ．確認にはwcコマンドを用いよ．
    def method_10(self):
        with open(self.name, 'r') as f:
            return len(f.readlines())

    # 11.タブをスペースに置換
    # タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
    def method_11(self):
        with open(self.name, 'r') as f:
            return f.read().replace('\t', ' ')

    # 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
    # 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
    def method_12(self):
        # 上書きする
        with open(self.name, 'r') as f:
            col1 = []
            col2 = []
            for line in f:
                col1.append(line.split()[0] + "\n")
                col2.append(line.split()[1] + "\n")
            with open('../file/col1.txt', 'w') as w1:
                w1.writelines(col1)
            with open('../file/col2.txt', 'w') as w2:
                w2.writelines(col2)

    # 13. col1.txtとcol2.txtをマージ
    # 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
    def method_13(self):
        merge = []
        with open('../file/col1.txt', 'r') as r1:
            for line in r1:
                merge.append(line.replace('\n', '\t'))

        with open('../file/col2.txt', 'r') as r2:
            i = 0
            for line in r2:
                merge[i] += line
                i += 1

        with open('../file/merge.txt', 'w') as w:
            w.writelines(merge)

        # openはカンマ区切りで書ける
        # with open("col1.txt") as f1, open("col2.txt") as f2:
        #     lines1, lines2 = f1.readlines(), f2.readlines()
        #
        # with open("merge.txt", "w") as writer:
        #     for col1, col2 in zip(lines1, lines2):
        #         writer.write("\t".join([col1.rstrip(), col2]))

    # 14. 先頭からN行を出力
    # 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
    def method_14(self, line_number):
        with open(self.name, 'r') as f:
            lines = f.readlines()
            for i in range(0, len(lines)):
                if i >= line_number:
                    break;
                print(lines[i].rstrip("\n"))

    # 15. 末尾のN行を出力
    # 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
    def method_15(self, line_number):
        with open(self.name, 'r') as f:
            lines = f.readlines()
            end = len(lines)
            start = end - line_number if end > line_number else 0
            for i in range(start, end):
                print(lines[i].rstrip("\n"))

    # 16. ファイルをN分割する
    # 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
    def method_16(self, split_by_line):
        with open(self.name, 'r') as f:
            split_count = 1
            content_list = []
            for line in f:
                with open('../file/split_' + str(split_count) + '.txt', 'w') as w:
                    content_list.append(line)

                    if len(content_list) == split_by_line:
                        w.write(''.join(content_list))
                        content_list = []
                        split_count += 1

    # 17. １列目の文字列の異なり
    # 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
    def method_17(self):
        s = set()
        with open(self.name, 'r') as f:
            for line in f:
                s.add(line.split()[0])
        sorted(s)
        for c in s:
            print(c)

    # 18. 各行を3コラム目の数値の降順にソート
    # 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
    # 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
    def method_18(self):
        with open(self.name, 'r') as f:
            lines = f.readlines()

        for line in sorted(lines, key=lambda x: x.split()[2], reverse=True):
            print(line)

    # 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
    # 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
    def method_19(self):
        prefectures = defaultdict(int)

        with open(self.name, 'r') as f:
            for line in f:
                prefectures[line.split()[0]] += 1

        for k, v in sorted(prefectures.items(), key=lambda x: x[1], reverse=True):
            print(k + ":" + str(v))
