import os

def main():
  #Criando caminho a partir de várias string com os nomes das pastas
  directory = os.path.join("Desktop", "python", "main.py")
  print(directory)

  #Verificando se o caminho existe
  print(os.path.exists(directory))

  #Pegando caminho e nome do arquivo
  abs_path, file = os.path.split(directory)
  print(abs_path, file)

  #Pegando o nome do arquivo e a extensão
  abs_path_2, extension = os.path.splitext(directory)
  print(abs_path_2, extension)

  #Pegando o nome do arquivo do caminho criado anteriormente
  basename = os.path.basename(directory)
  print(basename)

  #Pegando o nome da pasta do caminho criado anteriormente
  basedir = os.path.dirname(directory)
  print(basedir)
if __name__ == "__main__":
  main()