
import python_knock_part2 as pk

pkc = pk.PythonKnockPart2()

print("10. 行数のカウント")
print(pkc.count_row_num())
print("")

print("11. タブをスペースに置換")
print(pkc.replace_tab_to_space())
print("")

print("12. 1列目をcol1.txtに，2列目をcol2.txtに保存")
pkc.cut_text(1)
pkc.cut_text(2)
print("")
