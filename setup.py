# setup.py
from setuptools import setup, find_packages

setup(
    name="chatgusto-py",               # nome do seu pacote
    version="0.1.0",                     # versão inicial
    description="Um pacote legal feito pelo Augusto de 9 anos!",
    author="Augusto",                    # seu nome aqui!
    author_email="augustomiguelfarias7@gmail.com",  # pode colocar qualquer e-mail
    packages=find_packages(),            # acha automaticamente as pastas com código
    python_requires=">=3.6",             # funciona no Python 3.6 ou mais novo
    install_requires=[                   # bibliotecas que seu projeto precisa (se tiver)
        # "requests",                    # exemplo: descomente se precisar
        # "pygame",
    ],
)

# Extras legais que você pode adicionar depois:
#     long_description=open("README.md").read(),
#     long_description_content_type="text/markdown",
#     url="https://github.com/seuusuario/meupacotefoda",
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#     ],
