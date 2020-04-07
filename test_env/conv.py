import os
import re
import pyperclip


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


def main():
    # イベント名
    event_name = 'ABC'

    # 開催番号
    event_num = '{}{}'.format(event_name, '159')

    # 問題番号
    question_num = 'D'

    folder_path = './' + event_name + '/' + event_num + '/'
    file_name = event_num + '_' + question_num + '.py'
    base_file_path = "./test_env/proto.py"
    file_path = os.path.join(folder_path, file_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    with open(file_path, mode='w') as f:
        print(type(f))

    rewrite_ans(base_file_path, file_path)

    # 開催回のフォルダ作成 &　コピペ
    with open(file_path, mode="r") as answer:
        pyperclip.copy(answer.read())


if __name__ == "__main__":
    main()
