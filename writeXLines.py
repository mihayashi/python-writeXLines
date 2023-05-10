import os,sys, csv

#引数が指定の数あることを確認
if len(sys.argv)!=5:
    print("使い方：writeXLines.py file1 file2 行番号 行数")
    sys.exit()
#変換元のファイルが存在することを確認する
in_file = sys.argv[1]
if not os.path.exists(in_file):
    print("ファイルが存在しません")
    sys.exit()

#変換先のファイルが存在していた場合に上書きするかを確認する
out_file = sys.argv[2]
if os.path.exists(out_file):
    if input("上書きしますか？(y/n):")!="y":
        sys.exit()

#行番号
line_no = int(sys.argv[3])
#行数
lines = int(sys.argv[4])
print("line_no: ", line_no, "から", lines,"行を出力")
#書き出し最終行番号
end_line = line_no + lines
print("end_line: ",end_line)
#カウンター
i = 1


with open(in_file,"r", newline="", encoding="utf_16") as in_f:
    with open(out_file, "w", encoding="utf_16") as out_f:
        #reader = csv.reader(in_f)
        for line in in_f:
            if i >= line_no and i < end_line :
 #               print("line_no: ",i, line, "\n")
                #書き出し用のファイルに出力
                line = line.rstrip("\n")
                out_f.write(line)
                i += 1
                continue
            if i == end_line:
                break
            i += 1
