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
    # 第1引数: 開催タイトル, 第2引数: 開催回
    event_num = '{}{}'.format('ABC', '089')

    # 問題番号
    question_num = '{}'.format('C')

    folder_path = './' + event_num + '/'
    file_name = event_num + '_' + question_num + '.py'
    base_file_path = "./test_env/proto.py"
    file_path = os.path.join(folder_path, file_name)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

    with open(file_path, mode='w') as f:
        print(type(f))

    rewrite_ans(base_file_path, file_path)

    # 開催回のフォルダ作成 &　コピペ
    with open(file_path, mode="r") as answer:
        pyperclip.copy(answer.read())


if __name__ == "__main__":
    main()