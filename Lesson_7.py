import os
import shutil

# task 1
a = ['settings', 'mainapp', 'adminapp', 'authapp']

dir_path = os.path.join('my_project')
if not os.path.exists(dir_path):
    os.mkdir(dir_path)
    os.chdir(dir_path)
    for i in a:
        os.mkdir(i)


# task 3
# a = {'settings': ['__init__.py', 'dev.py', 'prod.py'],
#      'mainapp': ['__init__.py', 'models.py', 'views.py'],
#      'authapp': ['__init__.py', 'models.py', 'views.py']}
#
# dir_path = os.path.join('my_project')
# if not os.path.exists(dir_path):
#     os.mkdir(dir_path)
#     r = os.path.abspath(dir_path)
#     os.chdir(dir_path)
#     for i in a:
#         os.mkdir(i)
#         os.chdir(i)
#         for i_2 in a[i]:
#             file = open(i_2, "x")
#             file.close()
#             if not os.path.exists("templates") and i == "mainapp":
#                 os.mkdir("templates")
#                 os.chdir("templates")
#                 os.mkdir("mainapp")
#                 os.chdir("mainapp")
#                 file = open("base.html", "x")
#                 file.close()
#                 base = os.path.abspath('base.html')
#                 file = open("index.html", "x")
#                 file.close()
#                 index = os.path.abspath('index.html')
#                 os.chdir("..")
#                 os.chdir("..")
#             elif not os.path.exists("templates") and i == "authapp":
#                 os.mkdir("templates")
#                 os.chdir("templates")
#                 os.mkdir("authapp")
#                 os.chdir("authapp")
#                 file = open("base.html", "x")
#                 file.close()
#                 base_1 = os.path.abspath('base.html')
#                 file = open("index.html", "x")
#                 file.close()
#                 index_1 = os.path.abspath('index.html')
#                 os.chdir("..")
#                 os.chdir("..")
#         os.chdir("..")
#
# os.chdir(r)
# os.mkdir("templates")
# os.chdir("templates")
# os.mkdir("mainapp")
# mainapp = os.path.abspath('mainapp')
# os.mkdir("authapp")
# authapp = os.path.abspath('authapp')
# shutil.copy2(base, mainapp)
# shutil.copy2(index, mainapp)
# shutil.copy2(base_1, authapp)
# shutil.copy2(index_1, authapp)
