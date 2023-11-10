import os
import shutil
import re

# 指定包含子文件夹的父文件夹路径
parent_folder = r'\\mega\xchang\Data\Multi-center_Tuberculosis\drug_resistant\Fu_NaiDuoYao'

# 遍历父文件夹下的所有子文件夹
for folder_name in os.listdir(parent_folder):
    # 构建子文件夹的完整路径
    folder_path = os.path.join(parent_folder, folder_name)

    # 使用正则表达式去掉中文字符（只保留英文字母和数字）
    new_folder_name = re.sub(r'[^\x00-\x7F]+', '', folder_name)

    # 构建新的子文件夹完整路径
    new_folder_path = os.path.join(parent_folder, new_folder_name)

    # 重命名子文件夹
    os.rename(folder_path, new_folder_path)

# 完成后，所有子文件夹将被重命名，去掉了中文字符
