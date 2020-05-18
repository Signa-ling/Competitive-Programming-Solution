import os
import re
import pyperclip


class ProblemAssignment():
    def __init__(self, problem_site):
        self.problem_site = problem_site

    def atcoder_problem(self, e_name, e_num, q_num):
        if e_name=='Other':
            folder_path = './{0}/{1}/{1}_{2}/'.format(self.problem_site, e_name, e_num)
            file_name = '{0}_{1}.py'.format(e_num, q_num)
        else:    
            folder_path = './{0}/{1}/{1}{2}/'.format(self.problem_site, e_name, e_num)
            file_name = '{0}{1}_{2}.py'.format(e_name, e_num, q_num)
        file_path = os.path.join(folder_path, file_name)

        return folder_path, file_path

    def aoj_problem(self, e_name, e_num, q_num):
        folder_path = './{0}/{1}/{1}{2}/'.format(self.problem_site, e_name, e_num)
        file_name = '{0}{1}_{2}.py'.format(e_name, e_num, q_num)
        file_path = os.path.join(folder_path, file_name)

        return folder_path, file_path


# 変換用にファイルの読み込み
def rewrite_ans(base_file_path, file_path):
    with open(base_file_path, mode="r", encoding="utf-8") as prot, open(file_path, mode="w") as answ:
        # ローカル環境の読み込み
        for line in prot:
            # ローカル開発環境専用のキーワードを標準入力のものに置き換え
            tmp = line.replace('inp = open("./test_env/input.txt", mode="r")', '')\
                    .replace('inp.readline()', 'input()')\
                    .replace('inp.close()', '')

            # コメントの削除
            tmp = re.sub(r'#.*', '', tmp)

            # 空白行以外書き出し
            if tmp != '\n':
                answ.write(tmp)


def file_create(folder_path, file_path):
    base_file_path = "./test_env/proto.py"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    with open(file_path, mode='w') as f:
        print("file open")

    rewrite_ans(base_file_path, file_path)

    # 開催回のフォルダ作成 &　コピペ
    with open(file_path, mode="r") as answer:
        pyperclip.copy(answer.read())


def main():
    # サイト
    problem_site = ["AtCoder", "AOJ"]

    while(True):
        num = int(input("数字を入れてね(AtCoder:0, AOJ:1): "))
        if num <= 1: break
        print("指定された数字に対応した問題サイトは未作成です…")

    problem_assign = ProblemAssignment(problem_site[num])

    event_name = 'Other'
    event_num = '第７回日本情報オリンピック 予選（オンライン）'
    question_num = 'E'

    if num == 0:
        folder_path, file_path = problem_assign.atcoder_problem(event_name,
                                                                event_num,
                                                                question_num)
    elif num == 1:
        folder_path, file_path = problem_assign.aoj_problem(event_name,
                                                            event_num,
                                                            question_num)
    file_create(folder_path, file_path)
    print('Finish')


if __name__ == "__main__":
    main()
