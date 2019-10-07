
import python_knock_part1 as pk

pkc = pk.PythonKnockPart1()

print("00. 文字列の逆順")
input_str_00 = "stressed"
print(pkc.reverse_str_reversed(input_str_00))
print(pkc.reverse_str_slice(input_str_00))
print("")

print("01. 「パタトクカシーー」")
input_str_01 = "パタトクカシーー"
print(pkc.patatokukashi_operator(input_str_01))
print(pkc.patatokukashi_join(input_str_01))
print("")

print("02. 「パトカー」＋「タクシー」＝「パタトクカシーー」")
input_str_02_1 = "パトカー"
input_str_02_2 = "タクシー"
print(pkc.policecar_plus_taxi_operator(input_str_02_1, input_str_02_2))
print(pkc.policecar_plus_taxi_join(input_str_02_1, input_str_02_2))
print("")

print("03. 円周率")
input_str_03 = 'Now I need a drink, \
                alcoholic of course, after the heavy \
                lectures involving quantum mechanics.'
regex_03 = "[a-zA-Z]"
result_pi = pkc.pi(input_str_03, regex_03)
for key, value in result_pi.items():
    print("char: %s, count:%d" % (key, value))
print("")

print("04. 元素記号")
input_str_04 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. \
                New Nations Might Also Sign Peace Security Clause. \
                Arthur King Can."
target_list_04 = [1, 5, 6, 7, 8, 9, 15, 16, 19]
result_element_symbol = pkc.element_symbol(input_str_04, target_list_04)
for key, value in result_element_symbol.items():
    print("key: %s, position:%d" % (key, value))
print("")

print("05. n-gram")
input_str_05 = "I am an NLPer"
print("unigram")
print(pkc.n_gram(input_str_05, 1))
print(pkc.n_gram_slim(input_str_05, 1))
print("bigram")
print(pkc.n_gram(input_str_05, 2))
print(pkc.n_gram_slim(input_str_05, 2))
print("trigram")
print(pkc.n_gram(input_str_05, 3))
print(pkc.n_gram_slim(input_str_05, 3))
print("")

print("06. 集合")
input_str_06_1 = "paraparaparadise"
input_str_06_2 = "paragraph"
print("和集合(記号「|」使用)")
print(pkc.set_union_symbol(pkc.set_bigram, input_str_06_1, input_str_06_2))
print("和集合(union 関数使用)")
print(pkc.set_union_func(pkc.set_bigram, input_str_06_1, input_str_06_2))
print("積集合(記号「&」使用)")
print(pkc.set_intersection_symbol(
    pkc.set_bigram, input_str_06_1, input_str_06_2))
print("積集合(intersection 関数使用)")
print(pkc.set_intersection_func(pkc.set_bigram, input_str_06_1, input_str_06_2))
print("差集合(記号「-」使用)")
print(pkc.set_difference_symbol(pkc.set_bigram, input_str_06_1, input_str_06_2))
print("差集合(difference 関数使用)")
print(pkc.set_difference_func(pkc.set_bigram, input_str_06_1, input_str_06_2))
print("")

print("07. テンプレートによる文生成")
print(pkc.create_sentence_by_template(12, "気温", 22.4))
print("")

print("08. 暗号文")
input_str_08 = "aAあbCdいeうFえgおh"
print(input_str_08)
print(pkc.cipher(input_str_08))
print("")

print("09. Typoglycemia")
input_str_09 = "I couldn't believe that I could actually understand \
                what I was reading : the phenomenal power of the human mind."
print(input_str_09)
print(pkc.typoglycemia(pkc.randam_sort, input_str_09))
print("")
