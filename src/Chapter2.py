import os
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
    def wc(self):
        with open(self.name, 'r') as f:
            return len(f.readlines())

    # 11.タブをスペースに置換
    # タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
    def sed(self):
        with open(self.name, 'r') as f:
            print(f.read().replace('\t', ' '))
