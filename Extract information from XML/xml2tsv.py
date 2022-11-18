import pandas as pd
import sys
from lxml import etree
from datetime import datetime, timezone


def get_datalist(tree):  # Grab data from inodes
    data_list = []
    for i in range(len(tree.xpath('/fsimage/INodeSection/inode'))):
        data_list.append(tree.xpath(f'/fsimage/INodeSection/inode[{str(i + 1)}]/*/text()'))
    return data_list


def get_graph(data_list):  # get the parent-child dictionary
    id = [x[0] for x in data_list]
    for i in range(len(tree.xpath('/fsimage/INodeDirectorySection/directory'))):
        graph[tree.xpath(f'/fsimage/INodeDirectorySection/directory[{str(i + 1)}]/parent/text()')[0]] = tree.xpath(
            f'/fsimage/INodeDirectorySection/directory[{str(i + 1)}]/child/text()')
    for i in id:
        if i not in graph.keys():
            graph[i] = []
    return graph


def get_inverse_graph(graph):
    inv_map = {}
    for k, v in graph.items():  # invert the parent-child to child-parent
        for i in v:
            inv_map[i] = k
    return inv_map


def dfs(Graph, node, seq):   # use dfs to find all parents of a certain node
    if node not in seq:
        seq.append(node)
        if node in Graph.keys():
            dfs(Graph, Graph[node], seq)
    return seq


def get_sequence():      # get sequences produced by dfs and combine them into a list
    sequence = []
    for i in ids:
        sequence.append(dfs(inv_map, i, []))
    return sequence


def get_dict_id_name():  # combine ID and names into a dictionary to create path
    names = ['/']
    names.extend(tree.xpath('//name/text()'))
    my_dict = {}
    for i in ids:  # create dictionary to match ids and names
        for j in names:
            my_dict[i] = j
            names.remove(j)
            break
    return my_dict


def get_path(sequence, dictionary):  # get the paths of inodes
    seq_final = []
    paths = []
    for elem in sequence:
        seq_name = []
        for elem1 in elem:
            seq_name.append(dictionary[elem1])
        seq_final.append(seq_name)
    for elem in seq_final:
        path = ""
        elem.reverse()
        if len(elem) == 1:
            paths.append('/')
        else:
            for elem1 in elem[1:]:
                path += '/'
                path += elem1
            paths.append(path)
    return paths


def find_time():  # Find the mtime
    time = tree.xpath('//mtime/text()')
    time_list = [int(i) / 1000 for i in time]
    date_time = list(  # from timestamp get the datetime, and format the datetime
        map(lambda x: datetime.fromtimestamp(x, tz=timezone.utc).strftime("%-m/%-d/%Y %-H:%M"), (x for x in time_list)))
    return date_time


def find_permission():  # Find the permission. Convert the number into code
    permission = tree.xpath('//permission/text()')
    type = tree.xpath('//type/text()')
    permission_1 = [i[-3:] for i in permission]
    convert_standard = ["---", "--x", "-w-", "-wx", "r--", "r-x", "rw-", "rwx"]
    permission_str = []
    for i in range(len(permission_1)):
        str_ele = ""
        if type[i] == "FILE":
            str_ele += "-"
        else:
            str_ele += "d"
        for Str in permission_1[i]:
            str_ele += convert_standard[int(Str)]
        permission_str.append(str_ele)
    return permission_str


def block_count_file_size(data_list):  # Find the block count and file size
    block_count = []
    file_size = []
    for i in range(len(data_list)):
        if data_list[i][1] == 'FILE':
            block_count.append(len(tree.xpath(f'/fsimage/INodeSection/inode[{str(i + 1)}]/blocks/block')))
            file_size.append(sum(int(x) for x in tree.xpath(f'/fsimage/INodeSection/inode[{str(i + 1)}]/blocks/block'
                                                            f'/numBytes/text()')))
        else:
            block_count.append(0)
            file_size.append(0)
    return block_count, file_size


if __name__ == "__main__":
    File = sys.argv[1]
    tsv_out_path = sys.argv[2]
    tree = etree.parse(open(File))
    Seq = []
    graph = {}
    data_list = get_datalist(tree)
    ids = [i[0] for i in data_list]
    graph_new = get_graph(data_list)
    inv_map = get_inverse_graph(graph_new)
    sequence = get_sequence()
    my_dict = get_dict_id_name()
    paths = get_path(sequence, my_dict)
    mtime = find_time()
    permission = find_permission()
    block_count, file_size = block_count_file_size(data_list)
    my_df = pd.DataFrame({'Path': paths, 'Modification Time': mtime, 'BlocksCount': block_count, 'FileSize': file_size, 'Permission': permission})
    my_df.to_csv(tsv_out_path, sep='\t')











