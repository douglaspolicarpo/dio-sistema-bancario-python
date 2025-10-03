from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    page_description = f.read()

setup(
    name="sistema_bancario_poo",
    version="0.0.1",
    author="Douglas Policarpo", # Substitua se necessário
    author_email="douglas.policarpo@outlook.com.br", # Substitua pelo seu email
    description="Refatoração de um sistema bancário para Orientado a Objetos.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/douglaspolicarpo/dio-sistema-bancario-python",
    packages=find_packages(),
    python_requires='>=3.8',
)
