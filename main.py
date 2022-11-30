import cv2
import os
from pathlib import Path

def encontrar_imagem():
    nome_arquivo = input("Digite o nome do arquivo da imagem que você quer converter:\n")
    nome_diretorio = input("Digite o caminho completo do diretório que contém a imagem:\n")
    arquivos_encontrados = []
    for caminho, subdiretorios, arquivos in os.walk(nome_diretorio):
        for nome in arquivos:
            if nome_arquivo == nome:
                caminho_arquivo = os.path.join(caminho, nome)
                arquivos_encontrados.append(caminho_arquivo)
                print(arquivos_encontrados[0])
    return arquivos_encontrados[0]

caminho_imagem = Path(encontrar_imagem())

novo_diretorio = caminho_imagem.parent

# C:\Workspace\Python\Converte-cartoon\imagem

os.chdir(novo_diretorio)

cor_imagem = cv2.imread(str(caminho_imagem))

print("Selecione um dos estilos que deseja:")
estilo = int(input("1 - Smooth\n"
                           "2 - Cartoon Normal\n"
                           "3 - Cartoon Especial\n"))

if estilo == 1:
    estilo_smooth = cv2.bilateralFilter(cor_imagem, 50, 250, 250)
    img_resize = cv2.resize(estilo_smooth, (800, 600))
    cv2.imshow("Smooth:", img_resize)
    cv2.waitKey()
    cv2.destroyAllWindows()
elif estilo == 2:
    estilo_cartoon_1 = cv2.stylization(cor_imagem, sigma_s = 50, sigma_r = 0.25)
    img_resize = cv2.resize(estilo_cartoon_1, (800, 600))
    cv2.imshow("Cartoon_1:", img_resize)
    cv2.waitKey()
    cv2.destroyAllWindows()
elif estilo == 3:
    estilo_cartoon_2 = cv2.stylization(cor_imagem, sigma_s = 60, sigma_r = 0.5)
    img_resize = cv2.resize(estilo_cartoon_2, (800, 600))
    cv2.imshow("Cartoon_2:", img_resize)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("Opção inválida")