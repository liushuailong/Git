# -*- coding: utf-8 -*-

# 1.从PDB文件中读取数据；
def read_file():
    file_name = input("please input file_mane:")
    #determine whether the input file is a pdb file;
    if file_name.split(".")[-1] == "pdb":
        try:
            f = open(file_name,'r')
            content = f.read()
            # print(content)
            f.close()
            return (content, file_name)
        except IOError:
            # print("File not Exits")
            return None
        #finally:
            #if f:
                #f.close()
    else:
        # print("the type of file is error.")
        return None

# 2.处理PDB文件，将数据转化成字典型数据；
def data_handle(file_content):
    file_line_list = file_content.split("\n")
    atom_dict_list = []
    # print(file_line_list)
    for line in file_line_list:
        if len(line):
            line_split = line.split()
            # print(line_split)
            atom_dict = {}
            if "ATOM" == line_split[0]:
                atom_dict['atom_num'] = line_split[1]
                atom_dict['atom_x_axis'] = line_split[10]
                atom_dict['atom_y_axis'] = line_split[11]
                atom_dict['atom_z_axis'] = line_split[12]
                atom_dict_list.append(atom_dict)
    print(atom_dict_list)
    return atom_dict_list

# 3.计算两个原子之间的距离；
def square_difference(x1,x2):
    result = pow(float(x1)-float(x2),2)
    return result

def calculate_twoatom_dianstance(atom1,atom2):

    x_label_square = square_difference(atom1["atom_x_axis"],atom2["atom_x_axis"])
    y_label_square = square_difference(atom1["atom_y_axis"],atom2["atom_y_axis"])
    z_label_square = square_difference(atom1["atom_z_axis"],atom2["atom_z_axis"])
    distance = (x_label_square + y_label_square + z_label_square) ** 0.5
    return distance

def calculate_interatomic_distance(atom_coordinate_list):
    atom_num = len(atom_coordinate_list)
    maximum_interatomic_distance = ["atomnum_atomnum",0]
    two_atom_distance_list = []
    for i in range(atom_num):
        print("processe %s"%i)
        for j in range(i+1,atom_num):
            two_atom_distance_tuple = []
            two_atom_distance = calculate_twoatom_dianstance(atom_coordinate_list[i-1],atom_coordinate_list[j-1])

            if two_atom_distance > maximum_interatomic_distance[1]:
                maximum_interatomic_distance[0] = atom_coordinate_list[i-1]["atom_num"]+"_"+atom_coordinate_list[j-1]["atom_num"]
                maximum_interatomic_distance[1] = two_atom_distance
                # print(maximum_interatomic_distance)
            #two_atom_distance_tuple.append(atom_coordinate_list[i-1]["atom_num"]+"_"+atom_coordinate_list[j-1]["atom_num"])
            #two_atom_distance_tuple.append(two_atom_distance)
            # two_atom_distance_list.append(two_atom_distance_tuple)
    #print(two_atom_distance_list)
    #return two_atom_distance_list
    print(maximum_interatomic_distance)
    return maximum_interatomic_distance

# 4.比较两个原子原子之间的距离找出最大的值。
def maximum_interatomic_distance():
    pass


def save_result(result, file_name):
    new_file_name = file_name.split(".")[0] + "_result.txt"
    with open(new_file_name,"w") as f:
        f.write(str(result))

# 5.运行；
def run():
    file_tuple = read_file()
    #file_content, file_name = read_file()
    if file_tuple:
        file_content, file_name = file_tuple
        print("processing")
        atom_coordinate_list = data_handle(file_content)
        result = calculate_interatomic_distance(atom_coordinate_list)
        save_result(result, file_name)
    else:
        print("the type of file is error,or file not exits,or the empty file.")
if __name__ == "__main__":
    run()
    print("END")