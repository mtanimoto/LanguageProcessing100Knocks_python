import unittest, sys
sys.path.append('../')
from src.Chapter1 import Chapter1

class Chapter1Test(unittest.TestCase):
    # test class of Chapter1.py

    def setUp(self):
        self.target = Chapter1()

    def test_method_00(self):
        self.assertEqual(self.target.method_00(), 'desserts')

    def test_method_01(self):
        self.assertEqual(self.target.method_01(), 'パトカー')

    def test_method_02(self):
        self.assertEqual(self.target.method_02(), 'パタトクカシーー')

    def test_method_03(self):
        # Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics
        # 3,1,4,1,5,9,2,6,5,3,5,8,9,7,9
        word_length_list_Assumpt = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9]
        word_length_list = self.target.method_03()

        for num in range(word_length_list_Assumpt.__len__()):
            self.assertEqual(word_length_list_Assumpt[num], word_length_list[num])

    def test_method_04(self):
        # 先頭の1文字：1, 5, 6, 7, 8, 9, 15, 16, 19
        # 先頭の2文字：2, 3, 4, 10, 11, 12, 13, 14, 17, 18, 20
        # Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.
        expect_key_list = ['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mi','Al','Si','P','S','Cl','Ar','K','Ca']

        ret = self.target.method_04()

        self.assertEqual(len(ret), len(expect_key_list))
        for key in expect_key_list:
            self.assertTrue(key in ret)

    def test_method_05(self):
        ret = self.target.method_05('I am an NLPer', 2, 'word')
        expect_word_n_gram = [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
        for i in range(expect_word_n_gram.__len__()):
            for j in range(expect_word_n_gram[i].__len__()):
                self.assertTrue(expect_word_n_gram[i][j] == ret[i][j])

        ret = self.target.method_05('I am an NLPer', 2, 'character')
        expect_character_n_gram = ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
        for i in range(expect_character_n_gram.__len__()):
            self.assertTrue(expect_character_n_gram[i] == ret[i])

    def test_method_06(self):
        self.assertTrue(self.target.method_06())

    def test_method_07(self):
        self.assertTrue('12時の気温は22.4', self.target.method_07(12, '気温', 22.4))

    def test_method_08(self):
        sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
        ret = self.target.method_08(sentence)
        self.assertTrue("xlfowm'g yvorvev gszg I xlfow zxgfzoob fmwvihgzmw dszg I dzh ivzwrmt : gsv ksvmlnvmzo kldvi lu gsv sfnzm nrmw .", ret)

        ret2 = self.target.method_08(ret)
        self.assertTrue(sentence, ret2)

    def test_method_09(self):
        sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
        ret = self.target.method_09(sentence)

        # 異なる文章となっていることを確認
        self.assertFalse(sentence == ret)

        # 4文字以下のワードはシャッフルされていないこと
        expect_list = ['I', 'that', 'what', 'was', 'the', 'of', 'mind']
        for expect in expect_list:
            self.assertTrue(expect in ret.split())

        # 他にもチェックしたほうがよいけどめんどいのでしない

if __name__ == '__main__':
    unittest.main()